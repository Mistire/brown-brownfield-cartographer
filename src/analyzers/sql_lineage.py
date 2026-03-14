from typing import List, Set, Dict, Any
import sqlglot
from sqlglot import exp

class SQLLineageAnalyzer:
    """
    Extracts table dependencies and lineage from SQL queries using sqlglot.
    Distinguishes between sources and targets and identifies transformation types.
    """
    def __init__(self, dialect: str = "postgres"):
        self.dialect = dialect

    def extract_lineage(self, sql: str) -> List[Dict[str, Any]]:
        """
        Extracts structured lineage from a SQL string.
        Returns a list of dictionaries with source, target, type, and columns.
        """
        lineage = []
        try:
            # Pre-processing for common dbt/template patterns
            processed_sql = self._preprocess_sql(sql)
            dbt_refs = self.extract_dbt_refs(sql)
            
            # Use sqlglot to parse and analyze
            for expression in sqlglot.parse(processed_sql, read=self.dialect):
                if not expression: continue
                
                # Identify targets
                targets = []
                if isinstance(expression, exp.Create):
                    if expression.this and hasattr(expression.this, 'this') and hasattr(expression.this.this, 'name'):
                        targets.append(expression.this.this.name)
                elif isinstance(expression, exp.Insert):
                    if expression.this and hasattr(expression.this, 'this') and hasattr(expression.this.this, 'name'):
                        targets.append(expression.this.this.name)
                
                # Identify sources
                sources = set()
                ctes = {cte.alias: True for cte in expression.find_all(exp.CTE)}
                
                for table in expression.find_all(exp.Table):
                    table_name = table.name
                    if table_name and table_name not in ctes:
                        sources.add(table_name)
                
                # Merge dbt refs
                for ref in dbt_refs:
                    sources.add(ref)

                # Identify columns (projections)
                columns = []
                for select in expression.find_all(exp.Select):
                    for projection in select.expressions:
                        if isinstance(projection, exp.Alias):
                            columns.append(projection.alias)
                        elif isinstance(projection, exp.Column):
                            columns.append(projection.name)
                        elif isinstance(projection, exp.Star):
                            columns.append("*")

                # Generate lineage items
                final_targets = targets if targets else ["result_set"]
                for source in sources:
                    for target in final_targets:
                        lineage.append({
                            "source": source,
                            "target": target,
                            "type": expression.key.upper() if expression.key else "SELECT",
                            "columns": list(set(columns))
                        })

        except Exception as e:
            print(f"SQL Parser Error (using regex fallback): {e}")
            refs = self.extract_dbt_refs(sql)
            for ref in refs:
                lineage.append({
                    "source": ref,
                    "target": "inferred_sink",
                    "type": "REGEX_FALLBACK"
                })
        
        return lineage

    def _preprocess_sql(self, sql: str) -> str:
        """Cleans up SQL of jinja templates so sqlglot can parse it."""
        import re
        # Replace {{ ... }} with a placeholder that sqlglot can handle as a literal or identifier
        cleaned = re.sub(r"\{\{.*?\}\}", "TEMPLATE_VAR", sql)
        # Replace {% ... %} with empty space
        cleaned = re.sub(r"\{%.*?%\}", " ", cleaned)
        return cleaned

    def extract_dbt_refs(self, sql: str) -> Set[str]:
        """Specific extractor for dbt ref() and source() calls."""
        import re
        refs = re.findall(r"\{\{\s*ref\(['\"](.+?)['\"]\)\s*\}\}", sql)
        sources = re.findall(r"\{\{\s*source\(['\"].+?['\"]\s*,\s*['\"](.+?)['\"]\)\s*\}\}", sql)
        return set(refs) | set(sources)

    def extract_dependencies(self, sql: str) -> Set[str]:
        """Legacy method for backward compatibility."""
        items = self.extract_lineage(sql)
        return {item["source"] for item in items}
