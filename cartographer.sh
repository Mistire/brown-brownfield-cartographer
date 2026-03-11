#!/bin/bash

# Brownfield Cartographer Helper Script
# Usage: ./cartographer.sh [map|view|list] [args]

COMMAND=$1
TARGET=$2

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGETS_DIR="$BASE_DIR/targets"
CARTOGRAPHY_DIR="$BASE_DIR/.cartography"

mkdir -p "$TARGETS_DIR"

case $COMMAND in
    "map")
        if [[ -z "$TARGET" ]]; then
            echo "Usage: ./cartographer.sh map <github_url_or_local_path>"
            exit 1
        fi

        # Check if Target is a URL
        if [[ "$TARGET" == http* ]]; then
            REPO_NAME=$(basename "$TARGET" .git)
            FINAL_PATH="$TARGETS_DIR/$REPO_NAME"
            if [ ! -d "$FINAL_PATH" ]; then
                echo "Cloning $TARGET into $TARGETS_DIR..."
                git clone "$TARGET" "$FINAL_PATH"
            else
                echo "Repository $REPO_NAME already exists in targets/."
            fi
        else
            FINAL_PATH="$TARGET"
        fi

        echo "Running analysis on $FINAL_PATH..."
        uv run python "$BASE_DIR/src/cli.py" "$FINAL_PATH"
        ;;

    "view")
        if [[ -z "$TARGET" ]]; then
            echo "Usage: ./cartographer.sh view <project_name>"
            echo "Available projects:"
            ls -1 "$CARTOGRAPHY_DIR"
            exit 1
        fi

        # If user passes a URL to view, extract the name and hint at mapping
        if [[ "$TARGET" == http* ]]; then
            EXTRACTED_NAME=$(basename "$TARGET" .git)
            echo "Note: You passed a URL to 'view'. Looking for project: $EXTRACTED_NAME"
            TARGET=$EXTRACTED_NAME
        fi

        PROJECT_DIR="$CARTOGRAPHY_DIR/$TARGET"
        if [ ! -d "$PROJECT_DIR" ]; then
            echo "Error: Project '$TARGET' not found."
            echo "Maybe you need to run: ./cartographer.sh map <url_or_path> first?"
            echo ""
            echo "Analyzed projects available:"
            ls -1 "$CARTOGRAPHY_DIR"
            exit 1
        fi

        echo "Cleaning up port 8000..."
        fuser -k 8000/tcp 2>/dev/null
        sleep 1
        
        echo "Starting server for $TARGET at http://localhost:8000"
        echo "Press Ctrl+C to stop."
        cd "$PROJECT_DIR" && python3 -m http.server 8000
        ;;

    "clean")
        echo "Cleaning up legacy root artifacts..."
        rm -f "$CARTOGRAPHY_DIR"/*.md "$CARTOGRAPHY_DIR"/*.html "$CARTOGRAPHY_DIR"/*.json "$CARTOGRAPHY_DIR"/*.jsonl
        echo "Done. Only project subfolders remain in .cartography/"
        ;;

    "list")
        echo "Generated Project Artifacts:"
        ls -1 "$CARTOGRAPHY_DIR"
        ;;

    *)
        echo "Brownfield Cartographer CLI"
        echo "---------------------------"
        echo "Usage: ./cartographer.sh [command]"
        echo ""
        echo "Commands:"
        echo "  map <url/path>   Clone (if URL) and analyze a repository"
        echo "  view <project>   Start the interactive dashboard for a project"
        echo "  list             List all analyzed projects"
        ;;
esac
