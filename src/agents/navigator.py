from typing import Annotated, TypedDict, List, Dict, Any, Optional
import networkx as nx
import json
import os
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from src.graph.knowledge_graph import KnowledgeGraph

class AgentState(TypedDict):
    messages: List[BaseMessage]
    context: Dict[str, Any]

class Navigator:
    """
    LangGraph agent that provides a query interface to the codebase knowledge graph.
    """
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.kg = KnowledgeGraph.load(os.path.join(".cartography", os.path.basename(repo_path.rstrip("/"))))
        
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if self.api_key:
            self.llm = ChatOpenAI(
                model=os.getenv("LLM_MODEL", "qwen/qwen-2.5-72b-instruct:free"),
                openai_api_key=self.api_key,
                openai_api_base=os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1"),
                temperature=0
            )
        else:
            self.llm = None

        # Tools
        @tool
        def find_implementation(concept: str) -> str:
            """Semantically find where a concept is implemented in the codebase."""
            # Simple keyword search over purpose statements for now
            matches = []
            for node, data in self.kg.module_graph.nodes(data=True):
                purpose = data.get("purpose_statement", "").lower()
                if concept.lower() in purpose or concept.lower() in node.lower():
                    matches.append(f"- `{node}`: {purpose}")
            
            if not matches:
                return f"No direct implementation found for '{concept}'."
            return "Possible locations:\n" + "\n".join(matches[:5])

        @tool
        def trace_lineage(dataset: str, direction: str = "upstream") -> str:
            """Trace data lineage for a dataset. Direction can be 'upstream' or 'downstream'."""
            if dataset not in self.kg.lineage_graph:
                return f"Dataset '{dataset}' not found in lineage graph."
            
            if direction == "upstream":
                nodes = nx.ancestors(self.kg.lineage_graph, dataset)
                msg = f"Upstream sources for '{dataset}':"
            else:
                nodes = nx.descendants(self.kg.lineage_graph, dataset)
                msg = f"Downstream dependents of '{dataset}':"
            
            if not nodes:
                return f"No {direction} dependencies found for '{dataset}'."
            return msg + "\n" + "\n".join([f"- `{n}`" for n in nodes])

        @tool
        def blast_radius(module_path: str) -> str:
            """Identify all modules that depend on the given module (downstream)."""
            if module_path not in self.kg.module_graph:
                # Try partial match
                matches = [n for n in self.kg.module_graph.nodes if module_path in n]
                if not matches:
                    return f"Module '{module_path}' not found."
                module_path = matches[0]

            dependents = nx.descendants(self.kg.module_graph, module_path)
            if not dependents:
                return f"No downstream dependents for `{module_path}`. Change impact is local."
            
            return f"Blast radius of `{module_path}` ({len(dependents)} modules):\n" + \
                   "\n".join([f"- `{d}`" for d in list(dependents)[:10]])

        @tool
        def explain_module(path: str) -> str:
            """Provides a summary/explanation of a specific module."""
            if path not in self.kg.module_graph:
                # Try partial match
                matches = [n for n in self.kg.module_graph.nodes if path in n]
                if not matches:
                    return f"Module '{path}' not found."
                path = matches[0]
            
            data = self.kg.module_graph.nodes[path]
            return (f"**Module:** `{path}`\n"
                    f"**Purpose:** {data.get('purpose_statement', 'N/A')}\n"
                    f"**Complexity:** {data.get('complexity_score', 0)}\n"
                    f"**Centrality (PageRank):** {data.get('pagerank', 0):.4f}")

        self.tools = {
            "find_implementation": find_implementation,
            "trace_lineage": trace_lineage,
            "blast_radius": blast_radius,
            "explain_module": explain_module
        }

        workflow = StateGraph(AgentState)
        workflow.add_node("navigator", self.navigate)
        workflow.set_entry_point("navigator")
        workflow.add_edge("navigator", END)
        self.app = workflow.compile()

    async def query(self, text: str):
        inputs = {"messages": [HumanMessage(content=text)], "context": {}}
        state = await self.app.ainvoke(inputs)
        return state["messages"][-1].content

    def navigate(self, state: AgentState):
        query = state["messages"][-1].content.lower()
        
        # Improved heuristic "router"
        if any(kw in query for kw in ["lineage", "produce", "source", "sink", "upstream", "downstream"]):
            # Find a path-like or table-like string
            potential_targets = [word.strip("?.,") for word in query.split() if "_" in word or "/" in word or "." in word]
            dataset = potential_targets[0] if potential_targets else "customers"
            direction = "downstream" if "downstream" in query or "dependents" in query else "upstream"
            response = self.tools["trace_lineage"].invoke({"dataset": dataset, "direction": direction})
        elif any(kw in query for kw in ["break", "radius", "impact", "change"]):
            potential_targets = [word.strip("?.,`/") for word in query.split() if "/" in word or ".sql" in word]
            module = potential_targets[0] if potential_targets else "models/staging/stg_orders.sql"
            response = self.tools["blast_radius"].invoke({"module_path": module})
        elif any(kw in query for kw in ["where", "implementation", "find", "locate"]):
            concept = query.split()[-1].strip("? .")
            response = self.tools["find_implementation"].invoke({"concept": concept})
        elif "explain" in query:
            potential_targets = [word.strip("?.,`/") for word in query.split() if "/" in word or ".sql" in word]
            path = potential_targets[0] if potential_targets else "models/customers.sql"
            response = self.tools["explain_module"].invoke({"path": path})
        else:
            response = "I can help you navigate the codebase. Try asking:\n- 'What produces the customers table?'\n- 'What breaks if I change models/staging/stg_orders.sql?'\n- 'Explain models/customers.sql'"
            
        return {"messages": state["messages"] + [AIMessage(content=str(response))]}
