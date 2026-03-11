import subprocess
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any
import networkx as nx
from src.models.graph import ModuleNode, Edge
from src.analyzers.tree_sitter_analyzer import SurveyorAnalyzer
from src.utils.resolver import PathResolver

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

    def run(self):
        velocity = self.velocity_analyzer.get_velocity()
        
        # Count files for progress tracking
        total_files = 0
        for root, _, files in os.walk(self.repo_path):
            if any(d in root for d in [".git", ".venv", "__pycache__", ".cartography"]): continue
            total_files += len([f for f in files if f.endswith((".py", ".sql", ".yaml", ".yml", ".ipynb"))])
        
        processed_count = 0
        print(f"Index scan: Found {total_files} relevant files.")

        for root, _, files in os.walk(self.repo_path):
            if any(d in root for d in [".git", ".venv", "__pycache__", ".cartography"]):
                continue
            for file in files:
                if file.endswith((".py", ".sql", ".yaml", ".yml", ".ipynb")):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.repo_path)
                    
                    processed_count += 1
                    if processed_count % 10 == 0 or processed_count == total_files:
                        print(f"[{processed_count}/{total_files}] Surveying {rel_path}...")

                    try:
                        analysis = self.analyzer.analyze_module(full_path)
                        if "error" in analysis:
                            print(f"Warning: Skipping {rel_path} - {analysis['error']}")
                            continue
                            
                        node = ModuleNode(
                            path=rel_path,
                            language=analysis.get("language", "unknown"),
                            complexity_score=analysis.get("complexity_score", 0.0),
                            change_velocity_30d=velocity.get(rel_path, 0)
                        )
                        
                        self.graph.add_node(rel_path, **node.model_dump())
                        
                        # Resolve imports semantically
                        for imp_str in analysis.get("imports", []):
                            resolved_path = self.resolver.resolve_import(imp_str, full_path)
                            target = resolved_path if resolved_path else imp_str
                            self.graph.add_edge(rel_path, target, type="IMPORTS", raw_string=imp_str)
                    except Exception as e:
                        print(f"Error analyzing {rel_path}: {e}")
                        continue

    def save_graph(self, output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data = nx.node_link_data(self.graph)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
