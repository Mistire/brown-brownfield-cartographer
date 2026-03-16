from typing import Annotated, TypedDict, List, Dict, Any, Optional
import networkx as nx
import json
import os
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool
from dotenv import load_dotenv
from graph.knowledge_graph import KnowledgeGraph
from utils.paths import get_cartography_dir

load_dotenv()
from agents.semanticist import Semanticist
from agents.semantic_index import SemanticIndex
from agents.archivist import Archivist
from agents.hydrologist import Hydrologist
from agents.semanticist import select_model

class AgentState(TypedDict):
    messages: List[BaseMessage]
    context: Dict[str, Any]

class Navigator:
    """
    LangGraph agent that provides a query interface to the codebase knowledge graph.
    """
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.project_name = os.path.basename(repo_path.rstrip("/"))
        self.output_dir = os.path.join(get_cartography_dir(), self.project_name)
        
        self.kg = KnowledgeGraph.load(self.output_dir)
        self.archivist = Archivist(self.project_name)
        self.semanticist = Semanticist()
        self.semanticist.output_dir = self.output_dir
        self.semantic_index = SemanticIndex(self.output_dir)
        self.archivist.output_dir = self.output_dir
        self.hydrologist = Hydrologist(self.repo_path, graph=self.kg.lineage_graph)
        
        load_dotenv()
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        # Navigator needs tool-calling support; use env override or auto-select
        # the smallest free tool-capable model (falls back to largest if needed)
        if self.api_key:
            nav_model = os.getenv("NAVIGATOR_MODEL") or select_model(4096, require_tools=True)
            self.llm = ChatOpenAI(
                model_name=nav_model,
                openai_api_key=self.api_key,
                openai_api_base="https://openrouter.ai/api/v1",
                temperature=0,
            )
        else:
            self.llm = ChatOpenAI(
                model_name=os.getenv("NAVIGATOR_MODEL", "gpt-4o"),
                temperature=0,
            )

        # Tools
        @tool
        async def find_implementation(concept: str) -> str:
            """Semantically find where a concept is implemented in the codebase using vector search."""
            # Use vector index if available
            if self.semanticist.enabled and self.semantic_index.embeddings is not None:
                query_emb = await self.semanticist.get_embeddings(concept)
                results = self.semantic_index.search(query_emb, top_k=5)
                if results:
                    matches = [f"- `{r['path']}` (Score: {r['score']:.2f}): {r['purpose']}" for r in results]
                    return ("Semantic Search Results (Inference: LLM, Confidence: High):\n" + "\n".join(matches))
            
            # Fallback to keyword search
            matches = []
            for node, data in self.kg.module_graph.nodes(data=True):
                purpose = data.get("purpose_statement", "").lower()
                if concept.lower() in purpose or concept.lower() in node.lower():
                    matches.append(f"- `{node}`: {purpose}")
            
            if not matches:
                return f"No direct implementation found for '{concept}'. (Inference: Static Analysis)"
            return ("Keyword Search Results (Inference: Static Analysis, Confidence: 1.0):\n" + "\n".join(matches[:5]))

        @tool
        async def trace_lineage(dataset: str, direction: str = "upstream") -> str:
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
            
            res = [f"{msg} (Inference: Static Analysis, Confidence: 1.0)"]
            for n in nodes:
                data = self.kg.lineage_graph.nodes.get(n, {})
                citation = f"{data.get('source_file', 'unknown')}:{data.get('line', '?')}"
                purpose = data.get("purpose_statement", "N/A")
                res.append(f"- `{n}` (Citation: {citation}): {purpose}")
            
            return "\n".join(res)

        @tool
        async def blast_radius(module_path: str) -> str:
            """Identify all modules that depend on the given module (downstream)."""
            if module_path not in self.kg.module_graph:
                # Try partial match
                matches = [n for n in self.kg.module_graph.nodes if module_path in n]
                if not matches:
                    return f"Module '{module_path}' not found. (Inference: Static Analysis)"
                module_path = matches[0]

            dependents = list(nx.descendants(self.kg.module_graph, module_path))
            if not dependents:
                return f"No downstream dependents for `{module_path}`. Change impact is local. (Inference: Static Analysis, Confidence: 1.0)"
            
            dependents_sorted = sorted(dependents)
            return (f"Blast radius of `{module_path}` ({len(dependents)} modules). (Inference: Static Analysis, Confidence: 1.0):\n" + 
                   "\n".join([f"- `{d}`" for d in dependents_sorted[:10]]))

        @tool
        async def explain_module(path: str) -> str:
            """Provides a summary/explanation of a specific module."""
            if path not in self.kg.module_graph:
                # Try partial match
                matches = [n for n in self.kg.module_graph.nodes if path in n]
                if not matches:
                    return f"Module '{path}' not found. (Inference: Static Analysis)"
                path = matches[0]
            
            data = self.kg.module_graph.nodes[path]
            return (f"**Module:** `{path}`\n"
                    f"**Purpose:** {data.get('purpose_statement', 'N/A')}\n"
                    f"**Complexity:** {data.get('complexity_score', 0)}\n"
                    f"**Centrality (PageRank):** {data.get('pagerank', 0):.4f}\n"
                    f"**Inference:** {data.get('inference_type', 'LLM Inference')}\n"
                    f"**Confidence:** {data.get('confidence', 0.5)}")

        self.tools_list = [find_implementation, trace_lineage, blast_radius, explain_module]
        self.tools = {t.name: t for t in self.tools_list}
        
        if self.llm:
            self.llm_with_tools = self.llm.bind_tools(self.tools_list)
        else:
            self.llm_with_tools = None

        # StateGraph
        workflow = StateGraph(AgentState)
        
        workflow.add_node("agent", self.agent)
        workflow.add_node("tools", ToolNode(self.tools_list))
        
        workflow.set_entry_point("agent")
        workflow.add_conditional_edges("agent", tools_condition)
        workflow.add_edge("tools", "agent")
        
        self.app = workflow.compile()

    def agent(self, state: AgentState):
        if not self.llm_with_tools:
            return {"messages": [AIMessage(content="LLM is disabled. I cannot navigate the codebase.")]}
        
        # System instructions for "Master Thinker" quality
        system_msg = {
            "role": "system",
            "content": "You are the Navigator, a master software architect. Analyze the codebase using tools. "
                       "CRITICAL: When tracing lineage or identifying implementation, EXPLICITLY provide 'file:line' citations. "
                       "This is essential for the Mastery Demo Step 2 & 4. Be technical, precise, and cited."
        }
        
        # Insert system msg at the start if not present
        messages = state["messages"]
        if not any(m.type == "system" for m in messages):
             messages = [SystemMessage(content=system_msg["content"])] + messages

        response = self.llm_with_tools.invoke(messages)
        
        # Log LLM's decision in trace
        if hasattr(response, 'tool_calls') and response.tool_calls:
            self.archivist.log_trace("navigator_tool_call", {
                "tool": response.tool_calls[0].get('name'),
                "args": response.tool_calls[0].get('args')
            })
            
        return {"messages": [response]}

    async def query(self, text: str):
        self.archivist.log_trace("navigator_query", {"query": text})
        inputs = {"messages": [HumanMessage(content=text)], "context": {}}
        config = {"configurable": {"thread_id": "navigator_session"}}
        state = await self.app.ainvoke(inputs, config=config)
        
        final_response = state["messages"][-1].content
        self.archivist.log_trace("navigator_response", {"response_teaser": final_response[:100]})
        return final_response
