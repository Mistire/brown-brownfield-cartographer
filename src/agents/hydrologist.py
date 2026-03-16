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

    def run(self, files_to_scan: Optional[List[str]] = None, on_progress: Optional[callable] = None):
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
                if any(d in root for d in [".git", ".venv", "__pycache__", ".cartography", "node_modules", "dist", "build", ".next", ".dbt"]): continue
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
            if on_progress:
                on_progress("hydrologist_progress", f"[{processed_count}/{total_files}] Mapping lineage in {rel_path}...")

            if processed_count % 10 == 0 or processed_count == total_files:
                print(f"[{processed_count}/{total_files}] Mapping lineage in {rel_path}...")
                
            try:
                if file_name.endswith(".py"):
                    ios = self.python_analyzer.extract_io(full_path)
                    for io in ios:
                        dataset_name = io.get("path")
                        if not dataset_name: continue
                        
                        # Add DatasetNode
                        self.lineage_graph.add_node(
                            dataset_name, 
                            type="dataset", 
                            storage_type="file" if "." in dataset_name else "table",
                            inference_type="Static Analysis",
                            confidence=1.0
                        )
                        
                        # Add Transformation metadata
                        if io.get("type") == "source":
                            self.lineage_graph.add_edge(
                                dataset_name, rel_path, 
                                type="CONSUMES", 
                                line=io.get("line"),
                                inference_type="Static Analysis",
                                confidence=1.0
                            )
                        else:
                            self.lineage_graph.add_edge(
                                rel_path, dataset_name, 
                                type="PRODUCES", 
                                line=io.get("line"),
                                inference_type="Static Analysis",
                                confidence=1.0
                            )
                
                elif file_name.endswith(".sql"):
                    with open(full_path, "r") as f:
                        sql = f.read()
                    lineage = self.sql_analyzer.extract_lineage(sql)
                    for item in lineage:
                        source = item.get("source")
                        target = item.get("target")
                        if source and target:
                            self.lineage_graph.add_node(
                                source, type="dataset", storage_type="table",
                                inference_type="Static Analysis",
                                confidence=1.0
                            )
                            self.lineage_graph.add_node(
                                target, type="dataset", storage_type="table",
                                inference_type="Static Analysis",
                                confidence=1.0
                            )
                            self.lineage_graph.add_edge(
                                source, target, 
                                type="LINEAGE", 
                                source_file=rel_path,
                                transformation_type="SQL",
                                inference_type="Static Analysis",
                                confidence=1.0
                            )
                        
                elif file_name.endswith((".yml", ".yaml")):
                    if file_name in ("schema.yml", "schema.yaml"):
                        models = self.config_parser.parse_dbt_schema(full_path)
                        for model in models:
                            sink = model.get("name")
                            if sink:
                                self.lineage_graph.add_node(
                                    sink, type="dataset", storage_type="table", 
                                    owner=model.get("owner"),
                                    inference_type="Static Analysis",
                                    confidence=1.0
                                )
                                
            except Exception as e:
                print(f"Error mapping lineage in {rel_path}: {e}")

        # Enrichment: Label Sources and Sinks — called ONCE after all files processed
        self._enrich_lineage_metadata()

    def _enrich_lineage_metadata(self):
        """Identifies and labels sources and sinks in the lineage graph."""
        for node in self.lineage_graph.nodes():
            in_degree = self.lineage_graph.in_degree(node)
            out_degree = self.lineage_graph.out_degree(node)
            
            # Label as Source if no predecessors
            if in_degree == 0 and out_degree > 0:
                self.lineage_graph.nodes[node]["is_source"] = True
            
            # Label as Sink if no successors
            if out_degree == 0 and in_degree > 0:
                self.lineage_graph.nodes[node]["is_sink"] = True

    def blast_radius(self, node_name: str) -> Set[str]:
        if node_name not in self.lineage_graph:
            return set()
        return set(nx.descendants(self.lineage_graph, node_name))

    def find_sources(self) -> Set[str]:
        return {n for n, d in self.lineage_graph.nodes(data=True) if d.get("is_source")}

    def find_sinks(self) -> Set[str]:
        return {n for n, d in self.lineage_graph.nodes(data=True) if d.get("is_sink")}

    def save_graph(self, output_path: str):
        import json
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data = nx.node_link_data(self.lineage_graph)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2, default=str)
