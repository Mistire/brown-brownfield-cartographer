import os
import json
from typing import Dict, Any, Optional, List
import tree_sitter
from tree_sitter_languages import get_language, get_parser

class LanguageRouter:
    """
    Routes files to the correct tree-sitter parser based on extension.
    """
    EXTENSION_MAP = {
        ".py": "python",
        ".sql": "sql",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".ipynb": "python",
        ".js": "javascript",
        ".ts": "typescript"
    }

    def __init__(self):
        self.parsers = {}

    def get_parser(self, file_path: str) -> Optional[tree_sitter.Parser]:
        ext = os.path.splitext(file_path)[1].lower()
        lang_name = self.EXTENSION_MAP.get(ext)
        if not lang_name:
            return None
        
        if lang_name not in self.parsers:
            try:
                self.parsers[lang_name] = get_parser(lang_name)
            except Exception as e:
                print(f"Error loading parser for {lang_name}: {e}")
                return None
        
        return self.parsers[lang_name]

class SurveyorAnalyzer:
    def __init__(self):
        self.router = LanguageRouter()

    def analyze_module(self, path: str) -> Dict[str, Any]:
        ext = os.path.splitext(path)[1].lower()
        parser = self.router.get_parser(path)
        
        if ext == ".ipynb":
            content = self._extract_notebook_code(path)
            if not content:
                return {"error": "Empty or invalid notebook"}
        else:
            if not parser:
                return {"error": f"No parser for {path}"}
            with open(path, "rb") as f:
                content = f.read()
        
        if not parser:
            return {"error": f"No parser for {path}"}

        tree = parser.parse(content)
        
        if ext in [".py", ".ipynb"]:
            return self._analyze_python(content, tree, path)
        
        return {"path": path, "status": "unsupported_language_analysis", "language": self.router.EXTENSION_MAP.get(ext, "unknown")}

    def _extract_notebook_code(self, path: str) -> bytes:
        """Extracts and concatenates Python code from notebook cells."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                nb = json.load(f)
            
            code_lines = []
            for cell in nb.get("cells", []):
                if cell.get("cell_type") == "code":
                    source = cell.get("source", [])
                    if isinstance(source, list):
                        code_lines.extend(source)
                        code_lines.append("\n")
                    else:
                        code_lines.append(source)
                        code_lines.append("\n")
            
            return "".join(code_lines).encode("utf-8")
        except Exception as e:
            print(f"Error parsing notebook {path}: {e}")
            return b""

    def _analyze_python(self, content: bytes, tree: tree_sitter.Tree, path: str) -> Dict[str, Any]:
        language = get_language("python")
        
        # Queries for imports, functions, and classes
        import_query = language.query("""
            (import_from_statement 
                module_name: (dotted_name) @mod)
            (import_from_statement 
                module_name: (relative_import) @mod)
            (import_statement 
                name: (dotted_name) @mod)
        """)
        
        function_query = language.query("""
            (function_definition
                name: (identifier) @name
            ) @func
        """)
        
        class_query = language.query("""
            (class_definition
                name: (identifier) @name
            ) @class
        """)
        
        # For complexity, count control flow nodes
        complexity_query = language.query("""
            (if_statement) @if
            (for_statement) @for
            (while_statement) @while
            (with_statement) @with
            (try_statement) @try
            (except_clause) @except
            (boolean_operator) @logic
        """)

        results = {
            "path": path,
            "imports": [],
            "functions": [],
            "classes": [],
            "complexity_score": 1.0, # Baseline
            "language": "python"
        }

        # Extract Imports
        if hasattr(import_query, "captures"):
            captures = import_query.captures(tree.root_node)
        else:
            from tree_sitter import QueryCursor
            captures = QueryCursor().captures(import_query, tree.root_node)

        for node, tag in captures:
            imp_name = content[node.start_byte:node.end_byte].decode("utf-8")
            if imp_name not in results["imports"]:
                results["imports"].append(imp_name)

        # Extract Functions
        if hasattr(function_query, "captures"):
            captures = function_query.captures(tree.root_node)
        else:
            from tree_sitter import QueryCursor
            captures = QueryCursor().captures(function_query, tree.root_node)

        for node, tag in captures:
            if tag == "name":
                results["functions"].append(content[node.start_byte:node.end_byte].decode("utf-8"))

        # Extract Classes
        if hasattr(class_query, "captures"):
            captures = class_query.captures(tree.root_node)
        else:
            from tree_sitter import QueryCursor
            captures = QueryCursor().captures(class_query, tree.root_node)

        for node, tag in captures:
            if tag == "name":
                results["classes"].append(content[node.start_byte:node.end_byte].decode("utf-8"))

        # Calculate Complexity
        if hasattr(complexity_query, "captures"):
            control_nodes = complexity_query.captures(tree.root_node)
        else:
            from tree_sitter import QueryCursor
            control_nodes = QueryCursor().captures(complexity_query, tree.root_node)

        results["complexity_score"] += len(control_nodes)

        return results
