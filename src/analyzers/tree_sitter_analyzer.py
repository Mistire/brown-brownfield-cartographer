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
        elif ext == ".sql":
            return self._analyze_sql(content, tree, path)
        elif ext in [".yaml", ".yml"]:
            return self._analyze_yaml(content, tree, path)
        
        return {"path": path, "status": "unsupported_language_analysis", "language": self.router.EXTENSION_MAP.get(ext, "unknown")}

    def _get_captures(self, query: tree_sitter.Query, node: tree_sitter.Node) -> List[Any]:
        """Helper to handle tree-sitter 0.21 vs 0.22+ capture API."""
        if hasattr(query, "captures"):
            return query.captures(node)
        else:
            from tree_sitter import QueryCursor
            return QueryCursor().captures(query, node)

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
        
        import_query = language.query("""
            (import_from_statement module_name: (dotted_name) @mod)
            (import_from_statement module_name: (relative_import) @mod)
            (import_statement name: (dotted_name) @mod)
        """)
        
        function_query = language.query("""
            (function_definition name: (identifier) @name) @func
        """)
        
        class_query = language.query("""
            (class_definition name: (identifier) @name) @class
        """)
        
        docstring_query = language.query("""
            (module (expression_statement (string) @doc))
            (function_definition body: (block (expression_statement (string) @doc)))
            (class_definition body: (block (expression_statement (string) @doc)))
        """)

        decorator_query = language.query("""
            (decorator) @dec
        """)

        complexity_query = language.query("""
            (if_statement) @if
            (for_statement) @for
            (while_statement) @while
            (with_statement) @with
            (try_statement) @try
            (except_clause) @except
            (boolean_operator) @logic
        """)

        type_hint_query = language.query("""
            (type_hint) @hint
            (type_alias) @alias
        """)

        results = {
            "path": path,
            "imports": [],
            "functions": [],
            "classes": [],
            "decorators": [],
            "type_hints": [],
            "docstring": None,
            "complexity_score": 1.0,
            "language": "python"
        }

        # Docstring (just the module-level one for now)
        for node, _ in self._get_captures(docstring_query, tree.root_node):
            if node.parent.type == "module":
                results["docstring"] = content[node.start_byte:node.end_byte].decode("utf-8").strip('"\' \n')
                break

        # Imports
        for node, _ in self._get_captures(import_query, tree.root_node):
            name = content[node.start_byte:node.end_byte].decode("utf-8")
            if name == "*":
                # Flag star import in metadata if we can, 
                # for now just add a special marker to imports
                if "STAR_IMPORT" not in results["imports"]:
                    results["imports"].append("STAR_IMPORT")
                continue
            if name not in results["imports"]:
                results["imports"].append(name)

        # Functions
        for node, tag in self._get_captures(function_query, tree.root_node):
            if tag == "name":
                results["functions"].append(content[node.start_byte:node.end_byte].decode("utf-8"))

        # Classes
        for node, tag in self._get_captures(class_query, tree.root_node):
            if tag == "name":
                results["classes"].append(content[node.start_byte:node.end_byte].decode("utf-8"))

        # Decorators
        for node, _ in self._get_captures(decorator_query, tree.root_node):
            dec_text = content[node.start_byte:node.end_byte].decode("utf-8").strip()
            if dec_text not in results["decorators"]:
                results["decorators"].append(dec_text)

        # Type Hints
        for node, _ in self._get_captures(type_hint_query, tree.root_node):
            hint_text = content[node.start_byte:node.end_byte].decode("utf-8").strip()
            if hint_text not in results["type_hints"]:
                results["type_hints"].append(hint_text)

        # Complexity
        results["complexity_score"] += len(self._get_captures(complexity_query, tree.root_node))
        return results

    def _analyze_sql(self, content: bytes, tree: tree_sitter.Tree, path: str) -> Dict[str, Any]:
        language = get_language("sql")
        
        # Simpler queries to avoid version-specific node type errors
        # Focus on identifiers used as table names or CTE names
        relation_query = language.query("""
            (identifier) @id
        """)
        
        results = {
            "path": path,
            "imports": [], 
            "ctes": [],
            "complexity_score": 1.0,
            "language": "sql"
        }
        
        # We'll filter ids by looking at their parents in a follow-up if needed,
        # but for now, just capturing identifiers is a good start for building the map.
        for node, _ in self._get_captures(relation_query, tree.root_node):
            name = content[node.start_byte:node.end_byte].decode("utf-8")
            # Heuristic: Uppercase or snake_case might be tables
            if name.islower() and "_" in name or name.isupper():
                if name not in results["imports"]:
                    results["imports"].append(name)
                    
        return results

    def _analyze_yaml(self, content: bytes, tree: tree_sitter.Tree, path: str) -> Dict[str, Any]:
        language = get_language("yaml")
        
        # Simplified YAML query to just find keys
        key_query = language.query("""
            (block_mapping_pair key: (_) @key)
        """)
        
        results = {
            "path": path,
            "keys": [],
            "imports": [],
            "complexity_score": 1.0,
            "language": "yaml"
        }
        
        for node, _ in self._get_captures(key_query, tree.root_node):
            key = content[node.start_byte:node.end_byte].decode("utf-8").strip().replace(":", "")
            if key not in results["keys"]:
                results["keys"].append(key)
        
        results["complexity_score"] += len(results["keys"]) * 0.5
        return results
