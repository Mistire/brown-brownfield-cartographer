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
        Returns a list of dictionaries with:
        - source: table name (input)
        - target: table name (output)
        - type: transformation type (e.g., SELECT, INSERT, CREATE)
        """
        lineage = []
        try:
            # First, extract dbt-only patterns that might not parse perfectly in standard dialects
            dbt_refs = self.extract_dbt_refs(sql)
            
            # Use sqlglot for structured parsing
            for expression in sqlglot.parse(sql, read=self.dialect):
                if not expression: continue
                
                # Identify targets (e.g., CREATE TABLE X, INSERT INTO Y)
                targets = []
                if isinstance(expression, exp.Create):
                    targets.append(expression.this.this.name)
                elif isinstance(expression, exp.Insert):
                    targets.append(expression.this.this.name)
                
                # Identify sources (e.g., FROM A, JOIN B)
                sources = set()
                # Exclude CTEs from sources
                ctes = {cte.alias: True for cte in expression.find_all(exp.CTE)}
                
                for table in expression.find_all(exp.Table):
                    table_name = table.name
                    if table_name and table_name not in ctes:
                        sources.add(table_name)
                
                # Merge dbt refs into sources
                for ref in dbt_refs:
                    sources.add(ref)

                # Identify columns
                columns = []
                for projection in expression.find_all(exp.Alias):
                    columns.append(projection.alias)
                for projection in expression.find_all(exp.Column):
                    if projection.name not in columns:
                        columns.append(projection.name)
                if expression.find(exp.Star):
                    columns.append("*")

                # Generate lineage items
                for source in sources:
                    for target in (targets if targets else ["result_set"]):
                        lineage.append({
                            "source": source,
                            "target": target,
                            "type": expression.key.upper() if expression.key else "SELECT",
                            "columns": columns
                        })

        except Exception as e:
            # Fallback for complex Jinja or unsupported dialects: regex extraction
            print(f"SQL Parser Error (using regex fallback): {e}")
            refs = self.extract_dbt_refs(sql)
            for ref in refs:
                lineage.append({
                    "source": ref,
                    "target": "inferred_sink",
                    "type": "REGEX_FALLBACK"
                })
        
        return lineage

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
