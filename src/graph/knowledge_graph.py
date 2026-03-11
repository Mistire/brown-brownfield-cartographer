import os
import json
import networkx as nx
from typing import Dict, Any, Optional, List

class KnowledgeGraph:
    """
    Centralized NetworkX wrapper for the Brownfield Cartographer.
    Manages both the module dependency graph and data lineage graph,
    providing serialization and query methods.
    """
    def __init__(self):
        self.module_graph = nx.DiGraph()
        self.lineage_graph = nx.DiGraph()

    def add_module(self, path: str, **attrs):
        self.module_graph.add_node(path, **attrs)

    def add_dataset(self, name: str, **attrs):
        self.lineage_graph.add_node(name, node_type="dataset", **attrs)

    def add_edge(self, source: str, target: str, edge_type: str, graph: str = "module", **attrs):
        g = self.module_graph if graph == "module" else self.lineage_graph
        g.add_edge(source, target, type=edge_type, **attrs)

    def get_pagerank(self) -> Dict[str, float]:
        return nx.pagerank(self.module_graph)

    def get_strongly_connected(self) -> List[set]:
        return [c for c in nx.strongly_connected_components(self.module_graph) if len(c) > 1]

    def blast_radius(self, node: str, graph: str = "lineage") -> set:
        g = self.lineage_graph if graph == "lineage" else self.module_graph
        if node not in g:
            return set()
        return set(nx.descendants(g, node))

    def find_sources(self) -> List[str]:
        return [n for n in self.lineage_graph.nodes() if self.lineage_graph.in_degree(n) == 0]

    def find_sinks(self) -> List[str]:
        return [n for n in self.lineage_graph.nodes() if self.lineage_graph.out_degree(n) == 0]

    def serialize(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        
        module_path = os.path.join(output_dir, "module_graph.json")
        with open(module_path, "w") as f:
            json.dump(nx.node_link_data(self.module_graph), f, indent=2, default=str)
        
        lineage_path = os.path.join(output_dir, "lineage_graph.json")
        with open(lineage_path, "w") as f:
            json.dump(nx.node_link_data(self.lineage_graph), f, indent=2, default=str)

    @classmethod
    def load(cls, input_dir: str) -> "KnowledgeGraph":
        kg = cls()
        
        module_path = os.path.join(input_dir, "module_graph.json")
        if os.path.exists(module_path):
            with open(module_path, "r") as f:
                kg.module_graph = nx.node_link_graph(json.load(f))
        
        lineage_path = os.path.join(input_dir, "lineage_graph.json")
        if os.path.exists(lineage_path):
            with open(lineage_path, "r") as f:
                kg.lineage_graph = nx.node_link_graph(json.load(f))
        
        return kg
