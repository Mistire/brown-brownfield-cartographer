import argparse
import asyncio
import os
import sys

# Add the project root to sys.path for CLI execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.orchestrator import Orchestrator


async def main():
    parser = argparse.ArgumentParser(description="The Brownfield Cartographer")
    parser.add_argument("repo_path", help="Path to the repository to analyze")
    args = parser.parse_args()

    orchestrator = Orchestrator(args.repo_path)
    await orchestrator.run_full_pipeline()


if __name__ == "__main__":
    asyncio.run(main())
