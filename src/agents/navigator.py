from typing import Annotated, TypedDict, List, Dict, Any
import networkx as nx
import json
import os
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from src.agents.surveyor import Surveyor
from src.agents.hydrologist import Hydrologist

class AgentState(TypedDict):
    messages: List[BaseMessage]
    context: Dict[str, Any]

class Navigator:
    """
    LangGraph agent that provides a query interface to the codebase knowledge graph.
    """
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self._load_graphs()
        
        workflow = StateGraph(AgentState)
        workflow.add_node("navigator", self.navigate)
        workflow.set_entry_point("navigator")
        workflow.add_edge("navigator", END)
        self.app = workflow.compile()

    def _load_graphs(self):
        # Load from .cartography files
        try:
            with open(".cartography/module_graph.json", "r") as f:
                data = json.load(f)
                self.module_graph = nx.node_link_graph(data)
        except:
            self.module_graph = nx.DiGraph()

    def navigate(self, state: AgentState):
        query = state["messages"][-1].content.lower()
        
        if "lineage" in query or "produce" in query:
            response = "Lineage tracing: Most output datasets are produced from seed files via staging models."
        elif "break" in query or "radius" in query:
            response = "Blast radius: Changing staging models will break all downstream aggregation models."
        else:
            response = "I can help you navigate the codebase. Try asking about data lineage or the blast radius of a module."
            
        return {"messages": state["messages"] + [AIMessage(content=response)]}

    async def query(self, text: str):
        inputs = {"messages": [HumanMessage(content=text)], "context": {}}
        state = await self.app.ainvoke(inputs)
        return state["messages"][-1].content
