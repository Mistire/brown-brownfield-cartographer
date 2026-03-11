import os
import networkx as nx
from typing import Set
from src.models.graph import DatasetNode, TransformationNode
from src.analyzers.python_dataflow import PythonDataFlowAnalyzer
from src.analyzers.sql_lineage import SQLLineageAnalyzer

class Hydrologist:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.python_analyzer = PythonDataFlowAnalyzer()
        self.sql_analyzer = SQLLineageAnalyzer()
        self.lineage_graph = nx.DiGraph()

    def run(self):
        for root, _, files in os.walk(self.repo_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.repo_path)
                
                if file.endswith(".py"):
                    ios = self.python_analyzer.extract_io(full_path)
                    for io in ios:
                        # Add dataset nodes and edges
                        dataset_name = io["path"]
                        self.lineage_graph.add_node(dataset_name, type="dataset")
                        
                        if io["type"] == "source":
                            self.lineage_graph.add_edge(dataset_name, rel_path, type="CONSUMES")
                        else:
                            self.lineage_graph.add_edge(rel_path, dataset_name, type="PRODUCES")
                            
                elif file.endswith(".sql"):
                    with open(full_path, "r") as f:
                        sql = f.read()
                        
                    # Handle dbt refs
                    refs = self.sql_analyzer.extract_dbt_refs(sql)
                    for ref in refs:
                        self.lineage_graph.add_edge(ref, rel_path, type="CONSUMES")
                    
                    # Handle standard SQL tables
                    deps = self.sql_analyzer.extract_dependencies(sql)
                    for dep in deps:
                        if dep not in refs:
                            self.lineage_graph.add_edge(dep, rel_path, type="CONSUMES")

    def blast_radius(self, node_name: str) -> Set[str]:
        if node_name not in self.lineage_graph:
            return set()
        return set(nx.descendants(self.lineage_graph, node_name))
