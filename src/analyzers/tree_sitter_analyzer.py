import os
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
                # Reverting to 0.21.x signature
                self.parsers[lang_name] = get_parser(lang_name)
            except Exception as e:
                print(f"Error loading parser for {lang_name}: {e}")
                return None
        
        return self.parsers[lang_name]

class SurveyorAnalyzer:
    def __init__(self):
        self.router = LanguageRouter()

    def analyze_module(self, path: str) -> Dict[str, Any]:
        parser = self.router.get_parser(path)
        if not parser:
            return {"error": f"No parser for {path}"}
        
        with open(path, "rb") as f:
            content = f.read()
            tree = parser.parse(content)
        
        ext = os.path.splitext(path)[1].lower()
        if ext == ".py":
            return self._analyze_python(content, tree, path)
        
        return {"path": path, "status": "unsupported_language_analysis"}

    def _analyze_python(self, content: bytes, tree: tree_sitter.Tree, path: str) -> Dict[str, Any]:
        language = get_language("python")
        
        # Queries for imports, functions, and classes
        import_query = language.query("""
            (import_statement) @import
            (import_from_statement) @import_from
        """)
        
        function_query = language.query("""
            (function_definition
                name: (identifier) @name
                parameters: (parameters) @params
            ) @func
        """)
        
        class_query = language.query("""
            (class_definition
                name: (identifier) @name
                superclasses: (argument_list)? @bases
            ) @class
        """)

        results = {
            "path": path,
            "imports": [],
            "functions": [],
            "classes": [],
            "language": "python"
        }

        # Extract Imports
        captures = import_query.captures(tree.root_node)
        for node, tag in captures:
            results["imports"].append(content[node.start_byte:node.end_byte].decode("utf-8"))

        # Extract Functions
        captures = function_query.captures(tree.root_node)
        for node, tag in captures:
            if tag == "name":
                results["functions"].append(content[node.start_byte:node.end_byte].decode("utf-8"))

        # Extract Classes
        captures = class_query.captures(tree.root_node)
        for node, tag in captures:
            if tag == "name":
                results["classes"].append(content[node.start_byte:node.end_byte].decode("utf-8"))

        return results
