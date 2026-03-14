import os
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
import networkx as nx
from pyvis.network import Network

from utils.paths import get_cartography_dir

class Archivist:
    """
    Generates and maintains the living context (CODEBASE.md) and other artifacts.
    """
    def __init__(self, project_name: str, base_dir: Optional[str] = None):
        if base_dir is None:
            base_dir = get_cartography_dir()
        self.output_dir = os.path.join(base_dir, project_name)
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_codebase_md(self, graph: nx.DiGraph):
        path = os.path.join(self.output_dir, "CODEBASE.md")
        
        nodes = [data for n, data in graph.nodes(data=True)]
        
        with open(path, "w") as f:
            f.write("# CODEBASE.md: System Architecture Map\n\n")
            f.write("## 1. Architecture Overview\n")
            f.write("Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n\n")
            f.write("> [!IMPORTANT]\n")
            f.write("> This is a live, queryable map of the system's architecture and data flows.\n\n")
            
            f.write("### 1.1 System Map (Mermaid)\n")
            f.write("```mermaid\ngraph TD\n")
            for u, v, data in graph.edges(data=True):
                # Quote names for Mermaid
                f.write(f'    "{u}" --> "{v}"\n')
            f.write("```\n\n")
            
            f.write("## 2. Critical Path & Architectural Hubs\n")
            hubs = sorted([m for m in nodes if m.get("is_hub")], key=lambda x: x.get("pagerank", 0), reverse=True)
            for hub in hubs:
                f.write(f"- **`{hub.get('path', 'external_dependency')}`**: PageRank {hub.get('pagerank', 0):.4f}\n")
            f.write("\n")
            
            f.write("## 3. Data Sources & Sinks\n")
            # In a real lineage graph, sources have in-degree 0 in the LINEAGE graph
            # Here we are using the module graph, so we look for dataset nodes
            sources = [n for n, d in graph.nodes(data=True) if d.get("node_type") == "dataset" and graph.in_degree(n) == 0]
            sinks = [n for n, d in graph.nodes(data=True) if d.get("node_type") == "dataset" and graph.out_degree(n) == 0]
            
            f.write("### 3.1 Known Inputs (Sources)\n")
            for s in sources: f.write(f"- `{s}`\n")
            if not sources: f.write("No distinct sources identified via static analysis.\n")
            
            f.write("\n### 3.2 Known Outputs (Sinks)\n")
            for s in sinks: f.write(f"- `{s}`\n")
            if not sinks: f.write("No distinct sinks identified via static analysis.\n")
            
            f.write("\n## 4. Technical Debt & Safety Risks\n")
            circular = [m for m in nodes if m.get("in_circular_dep")]
            if circular:
                f.write("### 4.1 Circular Dependencies\n")
                f.write("> [!WARNING]\n")
                f.write("> Circular imports identified. These can cause silent initialization failures.\n\n")
                for c in circular:
                    f.write(f"- `{c.get('path', 'external_dependency')}` (SCC ID: {c.get('scc_id')})\n")
            
            dead = [m for m in nodes if m.get("is_dead_candidate")]
            if dead:
                f.write("\n### 4.2 Dead Code Candidates\n")
                f.write("> [!NOTE]\n")
                f.write("> Zero detected incoming references. Candidate for removal if not an entry point.\n\n")
                for d in dead:
                    f.write(f"- `{d.get('path', 'external_dependency')}`\n")
                    
            f.write("\n## 5. Recent Change Velocity (90-Day Map)\n")
            f.write("> [!TIP]\n")
            f.write("> High velocity files often indicate areas of high complexity or ongoing refactoring.\n\n")
            hotspots = sorted(nodes, key=lambda x: x.get("change_velocity_30d", 0), reverse=True)[:5]
            for h in hotspots:
                if h.get("change_velocity_30d", 0) > 0:
                    f.write(f"- `{h.get('path')}`: **{h.get('change_velocity_30d')}** changes in last 30 days\n")

            f.write("\n## 6. Module Purpose Index\n")
            for mod in nodes:
                path = mod.get('path', 'external_dependency')
                if mod.get("node_type") == "dataset": continue
                f.write(f"### `{path}`\n")
                f.write(f"**Purpose:** {mod.get('purpose_statement', 'No purpose generated.')}\n")
                
                drift = mod.get("documentation_drift")
                if drift and drift.get("drift_detected"):
                    f.write(f"> [!CAUTION]\n")
                    f.write(f"> **Doc Drift!** {drift.get('mismatch_reason')}\n\n")
                
                f.write(f"**Complexity:** {mod.get('complexity_score', 0.0)} | **Domain:** {mod.get('domain_cluster', 'N/A')}\n\n")

            f.write("\n## 7. System Statistics\n")
            f.write(f"Total Modules: {len(nodes)}\n")
            f.write(f"Total Dependencies: {graph.number_of_edges()}\n")

    def generate_interactive_graph(self, graph: nx.DiGraph):
        """Generates a standalone interactive HTML graph using pyvis."""
        # Use height="100vh" for full screen coverage and force CDN for JS/CSS
        net = Network(height="100vh", width="100%", bgcolor="#0f172a", font_color="white", directed=True, cdn_resources='remote')
        
        # Disable physics permanently for maximum performance and stability
        net.toggle_physics(False)
        
        for n, data in graph.nodes(data=True):
            label = n.split("/")[-1] if "/" in n else n
            title = (f"Path: {n}\n"
                     f"Complexity: {data.get('complexity_score', 0)}\n"
                     f"PageRank: {data.get('pagerank', 0):.4f}\n"
                     f"Purpose: {data.get('purpose_statement', 'N/A')}\n")
            
            if data.get("in_circular_dep"):
                title += "⚠️ CIRCULAR DEPENDENCY\n"
            if data.get("is_dead_candidate"):
                title += "👻 DEAD CODE CANDIDATE\n"
            
            # Premium color palette (Tailwind-like colors)
            complexity = data.get("complexity_score", 0)
            color = "#10b981" # Emerald 500
            if complexity > 10: color = "#f59e0b" # Amber 500
            if complexity > 25: color = "#ef4444" # Red 500
            
            # Highlight hubs with a border
            border_width = 4 if data.get("is_hub") else 2
            
            net.add_node(n, label=label, title=title, color=color, 
                         borderWidth=border_width, 
                         font={"size": 14, "face": "Inter, sans-serif"})
            
        for u, v, data in graph.edges(data=True):
            net.add_edge(u, v, color="#334155")
            
        output_path = os.path.join(self.output_dir, "interactive_graph.html")
        
        # Use a more premium look by enabling the selection menu and interaction features
        net.set_options("""
        var options = {
          "physics": {
            "enabled": false,
            "stabilization": false
          },
          "interaction": {
            "hover": true,
            "navigationButtons": true,
            "multiselect": true
          },
          "nodes": {
            "borderWidth": 2,
            "borderWidthSelected": 4,
            "shadow": true
          },
          "edges": {
            "color": { "inherit": true },
            "smooth": { "type": "continuous" },
            "shadow": true
          }
        }
        """)
        net.save_graph(output_path)

    def generate_onboarding_brief(self, module_data: List[Dict[str, Any]], day_one_answers: Dict[str, str]):
        """Generates the structured FDE Day-One Brief."""
        path = os.path.join(self.output_dir, "onboarding_brief.md")
        
        with open(path, "w") as f:
            f.write("# FDE Day-One Onboarding Brief\n\n")
            f.write("> [!IMPORTANT]\n")
            f.write("> This document is synthesized by the Brownfield Cartographer to accelerate FDE onboarding within the first 72 hours.\n\n")
            
            f.write("## 1. The Five Day-One Answers\n")
            questions = [
                "What is the primary data ingestion path?",
                "What are the 3-5 most critical output datasets/endpoints?",
                "What is the blast radius if the most critical module fails?",
                "Where is the business logic concentrated vs. distributed?",
                "What has changed most frequently in the last 90 days?"
            ]
            
            for i, q in enumerate(questions):
                key = f"q{i+1}"
                ans = day_one_answers.get(key, "Analysis inconclusive.")
                f.write(f"### Q{i+1}: {q}\n")
                f.write(f"{ans}\n\n")
            
            f.write("## 2. High-Velocity Hotspots (Maintenance Map)\n")
            valid_modules = [m for m in module_data if 'path' in m]
            sorted_mods = sorted(valid_modules, key=lambda x: x.get('change_velocity_30d', 0), reverse=True)[:5]
            for mod in sorted_mods:
                f.write(f"- `{mod['path']}`: **{mod.get('change_velocity_30d', 0)}** changes/30d. (Area of likely technical debt or high feature flux)\n")
            f.write("\n")
            
            f.write("## 3. High Complexity Risk Modules\n")
            sorted_comp = sorted(valid_modules, key=lambda x: x.get('complexity_score', 0), reverse=True)[:5]
            for mod in sorted_comp:
                f.write(f"- `{mod['path']}`: Complexity Score **{mod.get('complexity_score', 0)}**. (Recommended for refactoring or deep-dive testing)\n")

    def log_trace(self, action: str, details: Dict[str, Any]):
        trace_path = os.path.join(self.output_dir, "cartography_trace.jsonl")
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            **details
        }
        with open(trace_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
