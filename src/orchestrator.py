import asyncio
import os
import json

from src.agents.surveyor import Surveyor
from src.agents.hydrologist import Hydrologist
from src.agents.semanticist import Semanticist
from src.agents.archivist import Archivist


class Orchestrator:
    """
    Wires the Surveyor + Hydrologist (+ Semanticist when available) in sequence,
    serializes outputs to .cartography/<project_name>/.
    """
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.project_name = os.path.basename(repo_path.rstrip("/"))
        self.surveyor = Surveyor(repo_path)
        self.hydrologist = Hydrologist(repo_path)
        self.archivist = Archivist(self.project_name)
        self.semanticist = Semanticist()

    async def run_full_pipeline(self):
        """Execute the full analysis pipeline: Surveyor → Hydrologist → Archivist."""
        print("Starting Surveyor...")
        self.surveyor.run()
        self.surveyor.save_graph(
            os.path.join(self.archivist.output_dir, "module_graph.json")
        )

        print("Starting Hydrologist...")
        self.hydrologist.run()
        self.hydrologist.save_graph(
            os.path.join(self.archivist.output_dir, "lineage_graph.json")
        )

        print("Generating Artifacts...")
        module_data = [data for _, data in self.surveyor.graph.nodes(data=True)]

        # Semanticist provides Day-One answers when API key is set
        day_one_answers = {}
        if self.semanticist.enabled:
            pass  # Future: LLM synthesis

        self.archivist.generate_codebase_md(self.surveyor.graph)
        self.archivist.generate_interactive_graph(self.surveyor.graph)
        self.archivist.generate_onboarding_brief(module_data, day_one_answers)

        print("Analysis complete. Artifacts in .cartography/")
