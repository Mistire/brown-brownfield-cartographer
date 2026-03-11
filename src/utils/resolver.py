import os
from typing import Optional, List

class PathResolver:
    """
    Resolves import strings and relative paths to absolute filesystem paths.
    """
    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def resolve_import(self, import_str: str, current_file_path: Optional[str] = None) -> Optional[str]:
        """
        Attempts to resolve an import string to a file path within the repo.
        Supported patterns:
        - Absolute: src.utils.auth -> src/utils/auth.py
        - Relative (if current_file_path provided): ..common.utils -> ../common/utils.py
        """
        if not import_str:
            return None

        # Convert dots to path separators
        parts = import_str.split('.')
        
        # Handle relative imports (leading dots)
        leading_dots = 0
        for part in parts:
            if part == '':
                leading_dots += 1
            else:
                break
        
        if leading_dots > 0 and current_file_path:
            # Relative resolution
            base_dir = os.path.dirname(current_file_path)
            for _ in range(leading_dots - 1):
                base_dir = os.path.dirname(base_dir)
            
            relative_parts = parts[leading_dots:]
            potential_path = os.path.join(base_dir, *relative_parts)
        else:
            # Absolute resolution from repo root
            potential_path = os.path.join(self.repo_path, *parts)

        # Check for .py, .sql, or directory/__init__.py
        candidates = [
            potential_path + ".py",
            potential_path + ".sql",
            os.path.join(potential_path, "__init__.py")
        ]
        
        for cand in candidates:
            if os.path.exists(cand):
                return os.path.relpath(cand, self.repo_path)
        
        return None
