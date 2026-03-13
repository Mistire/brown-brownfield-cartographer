import argparse
import asyncio
import os
import sys

# Add the src directory to sys.path for CLI execution
# Since cli.py is at src/cli.py, we need to go up one level to get to src/
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from orchestrator import Orchestrator
from agents.navigator import Navigator
from dotenv import load_dotenv



async def main():
    parser = argparse.ArgumentParser(description="The Brownfield Cartographer")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Analyze Command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a repository and generate artifacts")
    analyze_parser.add_argument("repo_path", help="Path to the repository to analyze")
    analyze_parser.add_argument("--incremental", action="store_true", help="Only analyze changed files")

    # Query Command
    query_parser = subparsers.add_parser("query", help="Query the analyzed repository")
    query_parser.add_argument("repo_path", help="Path to the repository (to resolve artifact location)")

    args = parser.parse_args()

    if args.command == "analyze":
        orchestrator = Orchestrator(args.repo_path)
        await orchestrator.run_full_pipeline(incremental=args.incremental)
    elif args.command == "query":
        navigator = Navigator(args.repo_path)
        print(f"Entering Navigator mode for {args.repo_path}. Type 'exit' to quit.")
        while True:
            try:
                query_text = input("\n[Navigator] > ")
                if query_text.lower() in ["exit", "quit"]:
                    break
                response = await navigator.query(query_text)
                print(f"\n{response}")
            except KeyboardInterrupt:
                break
    else:
        parser.print_help()


def run_main():
    """Entry point for project.scripts in pyproject.toml"""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run_main()
