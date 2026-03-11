import os
import re
import yaml
from typing import Dict, List, Any, Set

class DAGConfigParser:
    """
    Parses Airflow DAG definitions and dbt schema.yml files
    to extract pipeline topology from configuration.
    """

    def parse_dbt_schema(self, schema_path: str) -> List[Dict[str, Any]]:
        """
        Parse a dbt schema.yml file and extract model metadata.
        Returns a list of model definitions with their columns and tests.
        """
        try:
            with open(schema_path, "r") as f:
                schema = yaml.safe_load(f)
        except Exception as e:
            print(f"Error parsing dbt schema {schema_path}: {e}")
            return []

        models = []
        if not schema or "models" not in schema:
            return models

        for model in schema.get("models", []):
            model_info = {
                "name": model.get("name", "unknown"),
                "description": model.get("description", ""),
                "columns": [],
                "tests": [],
            }
            for col in model.get("columns", []):
                model_info["columns"].append({
                    "name": col.get("name"),
                    "description": col.get("description", ""),
                    "tests": col.get("tests", []),
                })
            models.append(model_info)

        return models

    def parse_dbt_project(self, project_path: str) -> Dict[str, Any]:
        """
        Parse a dbt_project.yml file for project-level metadata.
        """
        dbt_project_file = os.path.join(project_path, "dbt_project.yml")
        if not os.path.exists(dbt_project_file):
            return {}

        try:
            with open(dbt_project_file, "r") as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Error parsing dbt_project.yml: {e}")
            return {}

    def extract_airflow_dag_structure(self, dag_file_path: str) -> Dict[str, Any]:
        """
        Extract DAG structure from an Airflow Python DAG file.
        Uses regex-based extraction for task_id and dependencies.
        """
        try:
            with open(dag_file_path, "r") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading Airflow DAG file {dag_file_path}: {e}")
            return {}

        dag_info = {"tasks": [], "dependencies": []}

        # Extract task_id from operator instantiations
        task_pattern = re.compile(r"(\w+)\s*=\s*\w+Operator\(.*?task_id\s*=\s*['\"](\w+)['\"]", re.DOTALL)
        for match in task_pattern.finditer(content):
            var_name, task_id = match.groups()
            dag_info["tasks"].append({"var_name": var_name, "task_id": task_id})

        # Extract >> dependency chains  
        dep_pattern = re.compile(r"(\w+)\s*>>\s*(\w+)")
        for match in dep_pattern.finditer(content):
            upstream, downstream = match.groups()
            dag_info["dependencies"].append({"upstream": upstream, "downstream": downstream})

        return dag_info

    def scan_configs(self, repo_path: str) -> Dict[str, Any]:
        """
        Walk a repository and extract all configuration-based pipeline topology.
        """
        results = {
            "dbt_models": [],
            "dbt_project": {},
            "airflow_dags": [],
        }

        for root, _, files in os.walk(repo_path):
            if ".git" in root or ".venv" in root or "__pycache__" in root:
                continue
            for file in files:
                full_path = os.path.join(root, file)

                if file in ("schema.yml", "schema.yaml"):
                    models = self.parse_dbt_schema(full_path)
                    results["dbt_models"].extend(models)

                elif file == "dbt_project.yml":
                    results["dbt_project"] = self.parse_dbt_project(os.path.dirname(full_path))

                elif file.endswith(".py"):
                    # Heuristic: check if file looks like an Airflow DAG 
                    try:
                        with open(full_path, "r") as f:
                            head = f.read(2000)
                        if "DAG(" in head or "airflow" in head.lower():
                            dag_info = self.extract_airflow_dag_structure(full_path)
                            if dag_info.get("tasks"):
                                dag_info["file"] = os.path.relpath(full_path, repo_path)
                                results["airflow_dags"].append(dag_info)
                    except Exception:
                        pass

        return results
