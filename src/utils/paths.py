"""
This module handles AWS S3 data lake paths and credential management.
"""
import os

def get_project_root() -> str:
    """Returns the absolute path to the project root directory."""
    # Since this file is at src/utils/paths.py,
    # the root is two levels up.
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def get_cartography_dir() -> str:
    """Returns the absolute path to the .cartography directory in the project root."""
    return os.path.join(get_project_root(), ".cartography")
