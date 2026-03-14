import tree_sitter
from typing import List, Dict, Any, Set
from analyzers.tree_sitter_analyzer import LanguageRouter
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
                    attribute: (identifier) @method (#match? @method "^(read_|to_|load|save|read|write)")
                )
                arguments: (argument_list
                    [
                        (string) @path
                        (pair
                            key: (identifier) @arg_name (#match? @arg_name "^(path|filepath|uri|url|table_name)$")
                            value: (string) @path
                        )
                    ]
                )
            ) @call

            (call
                function: (attribute
                    object: (identifier) @obj
                    attribute: (identifier) @method (#match? @method "^(fit|predict|score|transform)$")
                )
            ) @ml_call
        """)

    def extract_io(self, file_path: str) -> List[Dict[str, Any]]:
        parser = self.router.get_parser(file_path)
        if not parser:
            return []
            
        with open(file_path, "rb") as f:
            content = f.read()
            tree = parser.parse(content)
            
        ios = []
        if hasattr(self.io_query, "captures"):
            all_captures = self.io_query.captures(tree.root_node)
        else:
            from tree_sitter import QueryCursor
            all_captures = QueryCursor().captures(self.io_query, tree.root_node)
        
        # Group captures by call
        calls = {}
        processed_ml = set()
        
        for node, tag in all_captures:
            if tag == "ml_call":
                if node.id in processed_ml: continue
                processed_ml.add(node.id)
                method_node = node.child_by_field_name("function").child_by_field_name("attribute")
                method = content[method_node.start_byte:method_node.end_byte].decode("utf-8")
                ios.append({"method": method, "type": "transformation", "line": node.start_point[0] + 1})
                continue
                
            call_node = node if tag == "call" else node.parent
            while call_node and call_node.type != "call":
                call_node = call_node.parent
            if not call_node: continue
            
            call_id = call_node.id
            if call_id not in calls: calls[call_id] = {}
            calls[call_id][tag] = node

        for call_id, nodes in calls.items():
            if "method" not in nodes or "path" not in nodes: continue
            method_node = nodes["method"]
            path_node = nodes["path"]
            
            method = content[method_node.start_byte:method_node.end_byte].decode("utf-8")
            path = content[path_node.start_byte:path_node.end_byte].decode("utf-8").strip("'\"")
            
            # Heuristic for source vs sink
            io_type = "source"
            if method.startswith(("to_", "save", "write")) or "write" in method:
                io_type = "sink"
            
            ios.append({
                "method": method,
                "path": path,
                "type": io_type,
                "line": path_node.start_point[0] + 1
            })
        
        return ios
