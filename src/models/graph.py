from datetime import datetime
from typing import List, Optional, Dict, Literal, Any
from pydantic import BaseModel, Field

class ModuleNode(BaseModel):
    path: str
    language: str
    purpose_statement: Optional[str] = None
    domain_cluster: Optional[str] = None
    complexity_score: float = 0.0
    change_velocity_30d: int = 0
    is_dead_code_candidate: bool = False
    docstring: Optional[str] = None
    documentation_drift: Optional[Dict[str, Any]] = None
    last_modified: Optional[datetime] = None

class DatasetNode(BaseModel):
    name: str
    storage_type: Literal["table", "file", "stream", "api"]
    schema_snapshot: Optional[Dict[str, str]] = None
    freshness_sla: Optional[str] = None
    owner: Optional[str] = None
    is_source_of_truth: bool = False

class FunctionNode(BaseModel):
    qualified_name: str
    parent_module: str
    signature: str
    purpose_statement: Optional[str] = None
    call_count_within_repo: int = 0
    is_public_api: bool = True

class TransformationNode(BaseModel):
    source_datasets: List[str]
    target_datasets: List[str]
    transformation_type: str
    source_file: str
    line_range: tuple[int, int]
    sql_query_if_applicable: Optional[str] = None

class Edge(BaseModel):
    source: str
    target: str
    type: Literal["IMPORTS", "PRODUCES", "CONSUMES", "CALLS", "CONFIGURES"]
    metadata: Dict[str, Any] = Field(default_factory=dict)
