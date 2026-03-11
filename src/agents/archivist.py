import os
import json
from datetime import datetime
from typing import Dict, Any, List
from src.models.graph import ModuleNode

class Archivist:
    """
    Generates and maintains the living context (CODEBASE.md) and other artifacts.
    """
    def __init__(self, output_dir: str = ".cartography"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_codebase_md(self, module_data: List[Dict[str, Any]], lineage_data: Dict[str, Any]):
        path = os.path.join(self.output_dir, "CODEBASE.md")
        
        with open(path, "w") as f:
            f.write("# CODEBASE.md: System Architecture Map\n\n")
            f.write("## 1. Architecture Overview\n")
            f.write("Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n\n")
            
            f.write("## 2. Module Purpose Index\n")
            for mod in module_data:
                f.write(f"### `{mod['path']}`\n")
                f.write(f"**Purpose:** {mod.get('purpose_statement', 'No purpose generated.')}\n")
                f.write(f"**Language:** {mod['language']} | **Velocity:** {mod['change_velocity_30d']} changes/30d\n\n")
                
            f.write("## 3. Data Lineage Summary\n")
            f.write(f"Total Nodes: {len(lineage_data.get('nodes', []))}\n")
            f.write(f"Total Edges: {len(lineage_data.get('links', []))}\n")

    def log_trace(self, action: str, details: Dict[str, Any]):
        trace_path = os.path.join(self.output_dir, "cartography_trace.jsonl")
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            **details
        }
        with open(trace_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
