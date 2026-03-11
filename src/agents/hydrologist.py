import os
import networkx as nx
from typing import Set
from src.models.graph import DatasetNode, TransformationNode
from src.analyzers.python_dataflow import PythonDataFlowAnalyzer
from src.analyzers.sql_lineage import SQLLineageAnalyzer
from src.analyzers.dag_config_parser import DAGConfigParser

class Hydrologist:
    def __init__(self, repo_path: str, graph: nx.DiGraph = None):
        self.repo_path = repo_path
        self.python_analyzer = PythonDataFlowAnalyzer()
        self.sql_analyzer = SQLLineageAnalyzer()
        self.config_parser = DAGConfigParser()
        self.lineage_graph = graph if graph is not None else nx.DiGraph()

    def run(self):
        # Progress tracking
        total_files = 0
        for root, _, files in os.walk(self.repo_path):
            if ".cartography" in root: continue
            total_files += len([f for f in files if f.endswith((".py", ".sql", ".yml", ".yaml"))])
            
        processed_count = 0
        print(f"Lineage scan: Mapping flows across {total_files} files.")

        for root, _, files in os.walk(self.repo_path):
            if ".cartography" in root: continue
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.repo_path)
                
                if file.endswith((".py", ".sql", ".yml", ".yaml")):
                    processed_count += 1
                    if processed_count % 10 == 0 or processed_count == total_files:
                        print(f"[{processed_count}/{total_files}] Mapping lineage in {rel_path}...")
                
                try:
                    if file.endswith(".py"):
                        ios = self.python_analyzer.extract_io(full_path)
                        for io in ios:
                            if "path" not in io:
                                continue
                                
                            dataset_name = io["path"]
                            self.lineage_graph.add_node(dataset_name, type="dataset")
                            
                            if io["type"] == "source":
                                self.lineage_graph.add_edge(dataset_name, rel_path, type="CONSUMES")
                            else:
                                self.lineage_graph.add_edge(rel_path, dataset_name, type="PRODUCES")
                                
                    elif file.endswith(".sql"):
                        with open(full_path, "r") as f:
                            sql = f.read()
                            
                        lineage_items = self.sql_analyzer.extract_lineage(sql)
                        for item in lineage_items:
                            source = item["source"]
                            target = item["target"]
                            
                            self.lineage_graph.add_node(source, type="dataset")
                            self.lineage_graph.add_node(target, type="dataset")
                            
                            self.lineage_graph.add_edge(
                                source, 
                                target, 
                                type="LINEAGE",
                                transformation_type=item["type"],
                                source_file=rel_path,
                                logic_engine="sqlglot"
                            )
                                
                    elif file.endswith((".yml", ".yaml")):
                        if file in ("schema.yml", "schema.yaml"):
                            models = self.config_parser.parse_dbt_schema(full_path)
                            for model in models:
                                self.lineage_graph.add_node(model["name"], type="dataset", subtype="dbt_model")
                except Exception as e:
                    print(f"Error mapping lineage for {rel_path}: {e}")
                    continue
        
        # Post-process Airflow DAG structure
        config_results = self.config_parser.scan_configs(self.repo_path)
        for dag in config_results.get("airflow_dags", []):
            dag_file = dag["file"]
            for dep in dag.get("dependencies", []):
                # Map var_names to task_ids
                upstream_task = next((t["task_id"] for t in dag["tasks"] if t["var_name"] == dep["upstream"]), dep["upstream"])
                downstream_task = next((t["task_id"] for t in dag["tasks"] if t["var_name"] == dep["downstream"]), dep["downstream"])
                self.lineage_graph.add_edge(upstream_task, downstream_task, type="FLOW", file=dag_file)

    def blast_radius(self, node_name: str) -> Set[str]:
        if node_name not in self.lineage_graph:
            return set()
        return set(nx.descendants(self.lineage_graph, node_name))

    def find_sources(self) -> Set[str]:
        """Find nodes with zero in-degree (data entry points)."""
        return {n for n in self.lineage_graph.nodes() if self.lineage_graph.in_degree(n) == 0}

    def find_sinks(self) -> Set[str]:
        """Find nodes with zero out-degree (data exit points)."""
        return {n for n in self.lineage_graph.nodes() if self.lineage_graph.out_degree(n) == 0}

    def save_graph(self, output_path: str):
        """Serialize the lineage graph to JSON."""
        import json
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data = nx.node_link_data(self.lineage_graph)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2, default=str)
