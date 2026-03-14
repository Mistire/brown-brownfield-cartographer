import asyncio
import os
import json
from typing import Optional, Any, List

from agents.surveyor import Surveyor
from agents.hydrologist import Hydrologist
from agents.semanticist import Semanticist
from agents.archivist import Archivist


from graph.knowledge_graph import KnowledgeGraph

class Orchestrator:
    """
    Wires the Surveyor + Hydrologist (+ Semanticist when available) in sequence,
    serializes outputs to .cartography/<project_name>/.
    """
    def __init__(self, repo_path: str, on_progress: Optional[callable] = None):
        self.repo_path = repo_path
        self.project_name = os.path.basename(repo_path.rstrip("/"))
        self.kg = KnowledgeGraph()
        self.surveyor = Surveyor(repo_path, graph=self.kg.module_graph)
        self.hydrologist = Hydrologist(repo_path, graph=self.kg.lineage_graph)
        self.archivist = Archivist(self.project_name)
        self.semanticist = Semanticist()
        self.index = None
        self.on_progress = on_progress

    def _log(self, step: str, details: Any):
        if self.on_progress:
            self.on_progress(step, details)
        print(f"[{step}] {details}")

    async def run_full_pipeline(self, incremental: bool = False):
        """Execute the full analysis pipeline: Surveyor → Hydrologist → Semanticist → Archivist."""
        changed_files = None
        current_commit = None
        
        # Step 0: Robust Incremental Detection
        try:
            import subprocess
            current_commit = subprocess.check_output(["git", "-C", self.repo_path, "rev-parse", "HEAD"], text=True).strip()
            
            if incremental:
                last_commit_path = os.path.join(self.archivist.output_dir, "last_run_commit.txt")
                if os.path.exists(last_commit_path):
                    with open(last_commit_path, "r") as f:
                        last_commit = f.read().strip()
                    
                    if last_commit:
                        print(f"Detecting changes since {last_commit[:7]}...")
                        output = subprocess.check_output(
                            ["git", "-C", self.repo_path, "diff", "--name-only", last_commit], 
                            text=True
                        )
                        changed_files = [os.path.join(self.repo_path, f or ".") for f in output.splitlines()]
                        print(f"Incremental mode: {len(changed_files)} files changed.")
                else:
                    print("No previous commit record found. Performing full scan.")
        except Exception as e:
            if incremental:
                print(f"Incremental detection failed: {e}. Falling back to full scan.")

        self._log("surveyor_start", {"repo": self.repo_path, "incremental": incremental})
        # Execute blocking surveyor in thread to keep loop free for WS progress
        await asyncio.to_thread(self.surveyor.run, changed_files, self.on_progress)
        
        self._log("hydrologist_start", {})
        await asyncio.to_thread(self.hydrologist.run, changed_files, self.on_progress)
        
        self._log("analytics_start", "Computing advanced analytics (PageRank, Circularities, Dead Code)...")
        self.kg.enrich_metadata()
        
        self._log("semanticist_start", {"enabled": self.semanticist.enabled})
        module_data = [data for _, data in self.kg.module_graph.nodes(data=True)]
        
        # Populate purpose statements and index
        if self.semanticist.enabled:
            from agents.semantic_index import SemanticIndex
            self.index = SemanticIndex(self.archivist.output_dir)
            
            for node, data in self.kg.module_graph.nodes(data=True):
                if not data.get("purpose_statement") or data.get("purpose_statement") == "No purpose generated.":
                    self._log("semantic_analysis", f"Analyzing purpose for {node}...")
                    try:
                        full_path = os.path.join(self.repo_path, node)
                        if not os.path.isfile(full_path):
                            continue
                            
                        with open(full_path, "r") as f:
                            code = f.read()
                        
                        purpose, confidence = await self.semanticist.generate_purpose(code)
                        data["purpose_statement"] = purpose
                        data["confidence"] = confidence
                        
                        # Master Thinker: Generate and store embedding
                        embedding = await self.semanticist.get_embeddings(purpose)
                        self.index.add_entry(node, purpose, embedding)
                        
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
            
            self._log("semantic_index_save", "Saving Semantic Index...")
            self.index.save()
        
        # Cluster domains
        self._log("domain_clustering", "Clustering modules into semantic domains...")
        domain_clusters = await self.semanticist.cluster_into_domains(module_data)

        # Generate Day-One answers
        day_one_answers = {}
        if self.semanticist.enabled:
            self._log("onboarding_synthesis", "Synthesizing Day-One Onboarding Brief...")
            # Context for synthesis: Hubs, Lineage hotspots, Velocity
            hubs_list = [n for n, d in self.kg.module_graph.nodes(data=True) if d.get("is_hub")]
            sources_list = self.kg.find_sources()
            sinks_list = self.kg.find_sinks()
            
            synthesis_context = {
                "top_hubs": list(hubs_list)[:3],
                "sources": list(sources_list)[:3],
                "sinks": list(sinks_list)[:3],
                "domain_map": domain_clusters
            }
            day_one_answers = await self.semanticist.answer_day_one_questions(synthesis_context)

        self._log("graphics_save", "Saving graphs...")
        self.kg.serialize(self.archivist.output_dir)

        self._log("artifacts_gen", "Generating high-fidelity artifacts...")
        self.archivist.generate_codebase_md(self.kg.module_graph)
        self.archivist.generate_interactive_graph(self.kg.module_graph)
        self.archivist.generate_onboarding_brief(module_data, day_one_answers)

        self._log("pipeline_complete", "Analysis complete. System ready.")

        self.archivist.log_trace("pipeline_complete", {
            "artifacts_dir": self.archivist.output_dir,
            "token_usage": self.semanticist.budget.get_summary()
        })
        
        # Save current commit for next incremental run
        if current_commit:
            last_commit_path = os.path.join(self.archivist.output_dir, "last_run_commit.txt")
            with open(last_commit_path, "w") as f:
                f.write(current_commit)
                
        print(f"Analysis complete. Artifacts in {self.archivist.output_dir}")
