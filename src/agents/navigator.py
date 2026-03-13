from typing import Annotated, TypedDict, List, Dict, Any, Optional
import networkx as nx
import json
import os
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from dotenv import load_dotenv
from src.graph.knowledge_graph import KnowledgeGraph

load_dotenv()
from src.agents.archivist import Archivist

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
        self.kg = KnowledgeGraph.load(os.path.join(".cartography", self.project_name))
        self.archivist = Archivist(self.project_name)
        
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
                       "EXPLICITLY cite the modules or datasets you find. "
                       "If information is missing, admit it. Be precise and technical."
        }
        
        # Insert system msg at the start if not present
        messages = state["messages"]
        if not any(m.type == "system" for m in messages):
             messages = [AIMessage(content=system_msg["content"])] + messages

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
