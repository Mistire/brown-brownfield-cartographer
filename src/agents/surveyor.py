import subprocess
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import networkx as nx
from models.graph import ModuleNode, Edge
from analyzers.tree_sitter_analyzer import SurveyorAnalyzer
from utils.resolver import PathResolver

class GitVelocityAnalyzer:
    """
    Analyzes git history to identify which files change most frequently.
    """
    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def get_velocity(self, days: int = 30) -> Dict[str, int]:
        since_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        
        try:
            cmd = ["git", "log", f"--since={since_date}", "--name-only", "--pretty=format:"]
            result = subprocess.run(cmd, cwd=self.repo_path, capture_output=True, text=True, check=True)
            files = result.stdout.splitlines()
            velocity = {}
            for f in files:
                f = f.strip()
                if f: velocity[f] = velocity.get(f, 0) + 1
            return velocity
        except Exception as e:
            print(f"Error extracting git velocity: {e}")
            return {}

class Surveyor:
    def __init__(self, repo_path: str, graph: nx.DiGraph = None):
        self.repo_path = repo_path
        self.analyzer = SurveyorAnalyzer()
        self.velocity_analyzer = GitVelocityAnalyzer(repo_path)
        self.resolver = PathResolver(repo_path)
        self.graph = graph if graph is not None else nx.DiGraph()

    def run(self, files_to_scan: Optional[List[str]] = None, on_progress: Optional[callable] = None):
        """
        Executes the survey phase. If files_to_scan is provided, only those are analyzed (incremental mode).
        """
        velocity = self.velocity_analyzer.get_velocity()
        
        if files_to_scan:
             print(f"Incremental scan: Analyzing {len(files_to_scan)} changed files.")
             total_files = len(files_to_scan)
             iterate_over = files_to_scan
        else:
            total_files = 0
            iterate_over = []
            for root, _, files in os.walk(self.repo_path):
                if any(d in root for d in [".git", ".venv", "__pycache__", ".cartography", "node_modules", "dist", "build", ".next", ".dbt"]): continue
                for f in files:
                    if f.endswith((".py", ".sql", ".yaml", ".yml", ".ipynb")):
                        total_files += 1
                        iterate_over.append(os.path.join(root, f))
            
        processed_count = 0
        print(f"Index scan: Found {total_files} relevant files.")

        for full_path in iterate_over:
            rel_path = os.path.relpath(full_path, self.repo_path)
            processed_count += 1
            
            if on_progress:
                on_progress("surveyor_progress", f"[{processed_count}/{total_files}] Surveying {rel_path}...")

            if processed_count % 10 == 0 or processed_count == total_files:
                print(f"[{processed_count}/{total_files}] Surveying {rel_path}...")

            try:
                analysis = self.analyzer.analyze_module(full_path)
                if "error" in analysis:
                    continue
                
                # Add node to graph
                self.graph.add_node(rel_path, **analysis)
                
                # Add import edges
                for imp in analysis.get("imports", []):
                    resolved_path = self.resolver.resolve_import(imp, full_path)
                    if resolved_path:
                        self.graph.add_edge(rel_path, resolved_path, type="dependency")
                
                # Enrich with velocity
                if rel_path in velocity:
                    self.graph.nodes[rel_path]["change_velocity_30d"] = velocity[rel_path]
                    
            except Exception as e:
                print(f"Error surveying {rel_path}: {e}")

    def save_graph(self, output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data = nx.node_link_data(self.graph)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
