import os
import networkx as nx
from typing import Set
from src.models.graph import DatasetNode, TransformationNode
from src.analyzers.python_dataflow import PythonDataFlowAnalyzer
from src.analyzers.sql_lineage import SQLLineageAnalyzer
from src.analyzers.dag_config_parser import DAGConfigParser

class Hydrologist:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.python_analyzer = PythonDataFlowAnalyzer()
        self.sql_analyzer = SQLLineageAnalyzer()
        self.config_parser = DAGConfigParser()
        self.lineage_graph = nx.DiGraph()

    def run(self):
        for root, _, files in os.walk(self.repo_path):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, self.repo_path)
                
                if file.endswith(".py"):
                    ios = self.python_analyzer.extract_io(full_path)
                    for io in ios:
                        if "path" not in io:
                            # Internal transformation (e.g., fit/predict)
                            # For now, we just skip as we don't have a dataset node to link to
                            continue
                            
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
                            
                elif file.endswith((".yml", ".yaml")):
                    if file in ("schema.yml", "schema.yaml"):
                        models = self.config_parser.parse_dbt_schema(full_path)
                        for model in models:
                            self.lineage_graph.add_node(model["name"], type="dataset", subtype="dbt_model")
        
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

    def save_graph(self, output_path: str):
        """Serialize the lineage graph to JSON."""
        import json
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data = nx.node_link_data(self.lineage_graph)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2, default=str)
