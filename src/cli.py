import argparse
import asyncio
import os
import sys

# Add the project root to sys.path for CLI execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.surveyor import Surveyor
from src.agents.hydrologist import Hydrologist
from src.agents.semanticist import Semanticist
from src.agents.archivist import Archivist

class Orchestrator:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.surveyor = Surveyor(repo_path)
        self.hydrologist = Hydrologist(repo_path)
        self.archivist = Archivist()
        self.semanticist = Semanticist()

    async def run_full_pipeline(self):
        print("Starting Surveyor...")
        self.surveyor.run()
        self.surveyor.save_graph(".cartography/module_graph.json")
        
        print("Starting Hydrologist...")
        self.hydrologist.run()
        # self.hydrologist.save_graph(".cartography/lineage_graph.json") # TODO: Implement save
        
        print("Generating CODEBASE.md...")
        # Simplistic gathering for now
        module_data = [data for n, data in self.surveyor.graph.nodes(data=True)]
        lineage_data = {"nodes": [], "links": []} # TODO: link with hydrologist graph
        
        self.archivist.generate_codebase_md(module_data, lineage_data)
        print("Analysis complete. Artifacts in .cartography/")

async def main():
    parser = argparse.ArgumentParser(description="The Brownfield Cartographer")
    parser.add_argument("repo_path", help="Path to the repository to analyze")
    args = parser.parse_args()
    
    orchestrator = Orchestrator(args.repo_path)
    await orchestrator.run_full_pipeline()

if __name__ == "__main__":
    asyncio.run(main())
