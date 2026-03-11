import subprocess
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any
import networkx as nx
from src.models.graph import ModuleNode, Edge
from src.analyzers.tree_sitter_analyzer import SurveyorAnalyzer

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
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.analyzer = SurveyorAnalyzer()
        self.velocity_analyzer = GitVelocityAnalyzer(repo_path)
        self.graph = nx.DiGraph()

    def run(self):
        velocity = self.velocity_analyzer.get_velocity()
        
        for root, _, files in os.walk(self.repo_path):
            if ".git" in root or ".venv" in root:
                continue
            for file in files:
                if file.endswith((".py", ".sql", ".yaml", ".yml")):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.repo_path)
                    
                    analysis = self.analyzer.analyze_module(full_path)
                    if "error" in analysis:
                        continue
                        
                    node = ModuleNode(
                        path=rel_path,
                        language=analysis.get("language", "unknown"),
                        change_velocity_30d=velocity.get(rel_path, 0)
                    )
                    
                    self.graph.add_node(rel_path, **node.model_dump())
                    
                    # Add imports as edges (very basic resolution)
                    for imp in analysis.get("imports", []):
                        # This needs better resolution logic for real repos
                        self.graph.add_edge(rel_path, imp, type="IMPORTS")

    def save_graph(self, output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        data = nx.node_link_data(self.graph)
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
