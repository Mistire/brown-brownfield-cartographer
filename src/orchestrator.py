import asyncio
import os
import json

from src.agents.surveyor import Surveyor
from src.agents.hydrologist import Hydrologist
from src.agents.semanticist import Semanticist
from src.agents.archivist import Archivist


from src.graph.knowledge_graph import KnowledgeGraph

class Orchestrator:
    """
    Wires the Surveyor + Hydrologist (+ Semanticist when available) in sequence,
    serializes outputs to .cartography/<project_name>/.
    """
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.project_name = os.path.basename(repo_path.rstrip("/"))
        self.kg = KnowledgeGraph()
        self.surveyor = Surveyor(repo_path, graph=self.kg.module_graph)
        self.hydrologist = Hydrologist(repo_path, graph=self.kg.lineage_graph)
        self.archivist = Archivist(self.project_name)
        self.semanticist = Semanticist()

    async def run_full_pipeline(self, incremental: bool = False):
        """Execute the full analysis pipeline: Surveyor → Hydrologist → Semanticist → Archivist."""
        changed_files = None
        if incremental:
            print("Detecting changed files since last run...")
            # Simple git-based detection (if in a git repo)
            try:
                import subprocess
                output = subprocess.check_output(["git", "-C", self.repo_path, "diff", "--name-only", "HEAD^"], text=True)
                changed_files = [os.path.join(self.repo_path, f) for f in output.splitlines()]
                print(f"Incremental mode: {len(changed_files)} files changed.")
            except Exception as e:
                print(f"Incremental mode failed, falling back to full scan: {str(e)}")

        print("Starting Surveyor...")
        self.archivist.log_trace("surveyor_start", {"repo": self.repo_path, "incremental": incremental})
        # Note: Surveyor needs to be aware of changed_files if we want true incremental performance
        # For this implementation, we still run the skeleton but could optimize individual file analysis
        self.surveyor.run()
        
        print("Starting Hydrologist...")
        self.archivist.log_trace("hydrologist_start", {})
        self.hydrologist.run()
        
        print("Computing advanced analytics (PageRank, Circularities, Dead Code)...")
        self.kg.enrich_metadata()
        
        print("Starting Semanticist...")
        self.archivist.log_trace("semanticist_start", {"enabled": self.semanticist.enabled})
        module_data = [data for _, data in self.kg.module_graph.nodes(data=True)]
        
        # Populate purpose statements
        if self.semanticist.enabled:
            for node, data in self.kg.module_graph.nodes(data=True):
                if not data.get("purpose_statement") or data.get("purpose_statement") == "No purpose generated.":
                    print(f"Analyzing purpose for {node}...")
                    try:
                        full_path = os.path.join(self.repo_path, node)
                        with open(full_path, "r") as f:
                            code = f.read()
                        
                        purpose, confidence = await self.semanticist.generate_purpose(code)
                        data["purpose_statement"] = purpose
                        data["confidence"] = confidence
                        
                        # Master Thinker: Detect Documentation Drift
                        docstring = data.get("docstring")
                        if docstring:
                            drift = await self.semanticist.detect_drift(docstring, purpose)
                            data["documentation_drift"] = drift
                            
                        # Log semantic analysis in trace
                        self.archivist.log_trace("semantic_analysis", {
                            "node": node,
                            "confidence": confidence,
                            "drift_metrics": drift if docstring else None
                        })
                    except Exception as e:
                        print(f"Error analyzing semantic purpose for {node}: {e}")
        
        # Cluster domains
        domain_clusters = await self.semanticist.cluster_into_domains(module_data)

        # Generate Day-One answers
        day_one_answers = {}
        if self.semanticist.enabled:
            print("Synthesizing Day-One Onboarding Brief...")
            # Context for synthesis: Hubs, Lineage hotspots, Velocity
            synthesis_context = {
                "top_hubs": [n for n, d in self.kg.module_graph.nodes(data=True) if d.get("is_hub")][:3],
                "sources": self.kg.find_sources()[:3],
                "sinks": self.kg.find_sinks()[:3],
                "domain_map": domain_clusters
            }
            day_one_answers = await self.semanticist.answer_day_one_questions(synthesis_context)

        print("Saving graphs...")
        self.kg.serialize(self.archivist.output_dir)

        print("Generating Artifacts...")
        self.archivist.generate_codebase_md(self.kg.module_graph)
        self.archivist.generate_interactive_graph(self.kg.module_graph)
        self.archivist.generate_onboarding_brief(module_data, day_one_answers)

        self.archivist.log_trace("pipeline_complete", {
            "artifacts_dir": self.archivist.output_dir,
            "token_usage": {
                "prompt": self.semanticist.budget.total_prompt_tokens,
                "completion": self.semanticist.budget.total_completion_tokens,
                "model": self.semanticist.model_name
            }
        })
        print(f"Analysis complete. Artifacts in {self.archivist.output_dir}")
