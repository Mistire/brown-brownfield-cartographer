import tree_sitter
from typing import List, Dict, Any, Set
from src.analyzers.tree_sitter_analyzer import LanguageRouter
from tree_sitter_languages import get_language

class PythonDataFlowAnalyzer:
    """
    Extracts data flow patterns (pandas read/write, etc.) from Python AST.
    """
    def __init__(self):
        self.router = LanguageRouter()
        self.language = get_language("python")
        
        # Consistent with tree-sitter 0.22+ query API
        self.io_query = self.language.query("""
            (call
                function: (attribute
                    object: (identifier) @obj
                    attribute: (identifier) @method
                )
                arguments: (argument_list
                    (string) @path
                )
            ) @call
        """)

    def extract_io(self, file_path: str) -> List[Dict[str, Any]]:
        parser = self.router.get_parser(file_path)
        if not parser:
            return []
            
        with open(file_path, "rb") as f:
            content = f.read()
            tree = parser.parse(content)
            
        ios = []
        captures = self.io_query.captures(tree.root_node)
        
        # Group captures by call
        calls = {}
        for node, tag in captures:
            call_id = id(node) if tag == "call" else id(node.parent)
            if call_id not in calls: calls[call_id] = {}
            calls[call_id][tag] = node

        for call_id, nodes in calls.items():
            method = content[nodes["method"].start_byte:nodes["method"].end_byte].decode("utf-8")
            path = content[nodes["path"].start_byte:nodes["path"].end_byte].decode("utf-8").strip("'\"")
            
            if method.startswith(("read_", "to_", "load", "save")):
                ios.append({
                    "method": method,
                    "path": path,
                    "type": "source" if method.startswith("read_") else "sink"
                })
        
        return ios
