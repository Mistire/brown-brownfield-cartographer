from typing import List, Set
import sqlglot
from sqlglot import exp

class SQLLineageAnalyzer:
    """
    Extracts table dependencies from SQL queries using sqlglot.
    """
    def __init__(self, dialect: str = "postgres"):
        self.dialect = dialect

    def extract_dependencies(self, sql: str) -> Set[str]:
        dependencies = set()
        try:
            # Parse the SQL and find all Table expressions
            for expression in sqlglot.parse(sql, read=self.dialect):
                for table in expression.find_all(exp.Table):
                    # In dbt, tables are often in {{ ref('...') }} which might not parse as a clean table name
                    # but sqlglot handles standard SQL well.
                    table_name = table.name
                    if table_name:
                        dependencies.add(table_name)
        except Exception as e:
            print(f"Error parsing SQL: {e}")
        
        return dependencies

    def extract_dbt_refs(self, sql: str) -> Set[str]:
        """
        Specific extractor for dbt ref() calls.
        """
        import re
        # Simple regex for {{ ref('...') }} or {{ ref("...") }}
        refs = re.findall(r"\{\{\s*ref\(['\"](.+?)['\"]\)\s*\}\}", sql)
        return set(refs)
