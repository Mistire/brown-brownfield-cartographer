import os
import networkx as nx
from typing import Set, List, Optional
from models.graph import DatasetNode, TransformationNode
from analyzers.python_dataflow import PythonDataFlowAnalyzer
from analyzers.sql_lineage import SQLLineageAnalyzer
from analyzers.dag_config_parser import DAGConfigParser

class Hydrologist:
    def __init__(self, repo_path: str, graph: nx.DiGraph = None):
        self.repo_path = repo_path
        self.python_analyzer = PythonDataFlowAnalyzer()
        self.sql_analyzer = SQLLineageAnalyzer()
        self.config_parser = DAGConfigParser()
        self.lineage_graph = graph if graph is not None else nx.DiGraph()

    def run(self, files_to_scan: Optional[List[str]] = None):
        """
        Executes the lineage phase. If files_to_scan is provided, only those are analyzed (incremental mode).
        """
        if files_to_scan:
            print(f"Incremental lineage scan: Mapping {len(files_to_scan)} changed files.")
            total_files = len(files_to_scan)
            iterate_over = files_to_scan
        else:
            total_files = 0
            iterate_over = []
            for root, _, files in os.walk(self.repo_path):
                if any(d in root for d in [".git", ".venv", "__pycache__", ".cartography"]): continue
                for f in files:
                    if f.endswith((".py", ".sql", ".yml", ".yaml")):
                        total_files += 1
                        iterate_over.append(os.path.join(root, f))
            
        processed_count = 0
        print(f"Lineage scan: Mapping flows across {total_files} files.")

        for full_path in iterate_over:
            rel_path = os.path.relpath(full_path, self.repo_path)
            file_name = os.path.basename(full_path)
            
            processed_count += 1
            if processed_count % 10 == 0 or processed_count == total_files:
                print(f"[{processed_count}/{total_files}] Mapping lineage in {rel_path}...")
                
            try:
                if file_name.endswith(".py"):
                    ios = self.python_analyzer.extract_io(full_path)
                    for io in ios:
                        dataset_name = io.get("path")
                        if not dataset_name: continue
                        self.lineage_graph.add_node(dataset_name, type="dataset")
                        if io.get("type") == "source":
                            self.lineage_graph.add_edge(dataset_name, rel_path, type="CONSUMES")
                        else:
                            self.lineage_graph.add_edge(rel_path, dataset_name, type="PRODUCES")
                
                elif file_name.endswith(".sql"):
                    with open(full_path, "r") as f:
                        sql = f.read()
                    lineage = self.sql_analyzer.extract_lineage(sql)
                    for item in lineage:
                        source = item.get("source")
                        target = item.get("target")
                        if source and target:
                            self.lineage_graph.add_node(source, type="dataset")
                            self.lineage_graph.add_node(target, type="dataset")
                            self.lineage_graph.add_edge(source, target, type="LINEAGE", source_file=rel_path)
                        
                elif file_name.endswith((".yml", ".yaml")):
                    if file_name in ("schema.yml", "schema.yaml"):
                        models = self.config_parser.parse_dbt_schema(full_path)
                        for model in models:
                            sink = model.get("name")
                            if sink:
                                self.lineage_graph.add_node(sink, type="dataset")
                                # Sources in dbt schema are harder to trace without project-level context,
                                # but usually they are defined in 'sources' or 'ref' in models.
                                
            except Exception as e:
                print(f"Error mapping lineage in {rel_path}: {e}")

    def blast_radius(self, node_name: str) -> Set[str]:
        if node_name not in self.lineage_graph:
            return set()
        return set(nx.descendants(self.lineage_graph, node_name))

    def find_sources(self) -> Set[str]:
        return {n for n in self.lineage_graph.nodes() if self.lineage_graph.in_degree(n) == 0}

    def find_sinks(self) -> Set[str]:
        return {n for n in self.lineage_graph.nodes() if self.lineage_graph.out_degree(n) == 0}

    def save_graph(self, output_path: str):
        import json
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data = nx.node_link_data(self.lineage_graph)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2, default=str)
