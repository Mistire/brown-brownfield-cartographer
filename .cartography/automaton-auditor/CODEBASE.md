# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-11 16:42

### 1.1 System Map (Mermaid)
```mermaid
graph TD
    "main.py" --> "os"
    "main.py" --> "json"
    "main.py" --> "sys"
    "main.py" --> "dotenv"
    "main.py" --> "src/graph.py"
    "main.py" --> "src/state.py"
    "main.py" --> "argparse"
    "src/graph.py" --> "langgraph.graph"
    "src/graph.py" --> "src/state.py"
    "src/graph.py" --> "src/nodes/detectives.py"
    "src/graph.py" --> "src/nodes/judges.py"
    "src/graph.py" --> "src/nodes/justice.py"
    "src/state.py" --> "operator"
    "src/state.py" --> "typing"
    "src/state.py" --> "typing_extensions"
    "src/state.py" --> "pydantic"
    "test_local.py" --> "os"
    "test_local.py" --> "sys"
    "test_local.py" --> "dotenv"
    "test_local.py" --> "json"
    "test_local.py" --> "src/graph.py"
    "test_local.py" --> "traceback"
    "test_llm.py" --> "os"
    "test_llm.py" --> "dotenv"
    "test_llm.py" --> "src/tools/llm_tools.py"
    "src/tools/llm_tools.py" --> "os"
    "src/tools/llm_tools.py" --> "langchain_google_genai"
    "src/tools/llm_tools.py" --> "langchain_openai"
    "src/nodes/detectives.py" --> "src/tools/llm_tools.py"
    "src/nodes/detectives.py" --> "langchain_core.messages"
    "src/nodes/detectives.py" --> "base64"
    "src/nodes/detectives.py" --> "os"
    "src/nodes/detectives.py" --> "typing"
    "src/nodes/detectives.py" --> "src/state.py"
    "src/nodes/detectives.py" --> "src/tools/__init__.py"
    "src/nodes/judges.py" --> "json"
    "src/nodes/judges.py" --> "os"
    "src/nodes/judges.py" --> "typing"
    "src/nodes/judges.py" --> "langchain_google_genai"
    "src/nodes/judges.py" --> "langchain_openai"
    "src/nodes/judges.py" --> "src/state.py"
    "src/nodes/judges.py" --> "src/tools/llm_tools.py"
    "src/nodes/justice.py" --> "datetime"
    "src/nodes/justice.py" --> "typing"
    "src/nodes/justice.py" --> "json"
    "src/nodes/justice.py" --> "src/state.py"
    "src/nodes/justice.py" --> "os"
    "src/tools/safety.py" --> "re"
    "src/tools/safety.py" --> "subprocess"
    "src/tools/safety.py" --> "typing"
    "src/tools/safety.py" --> "urllib.parse"
    "src/tools/repo_tools.py" --> "os"
    "src/tools/repo_tools.py" --> "tempfile"
    "src/tools/repo_tools.py" --> "ast"
    "src/tools/repo_tools.py" --> "re"
    "src/tools/repo_tools.py" --> "typing"
    "src/tools/repo_tools.py" --> "pathlib"
    "src/tools/repo_tools.py" --> "src/state.py"
    "src/tools/repo_tools.py" --> "src/tools/__init__.py"
    "src/tools/repo_tools.py" --> "shutil"
    "src/tools/doc_tools.py" --> "re"
    "src/tools/doc_tools.py" --> "fitz"
    "src/tools/doc_tools.py" --> "pathlib"
    "src/tools/doc_tools.py" --> "typing"
    "src/tools/doc_tools.py" --> "src/state.py"
    "src/tools/doc_tools.py" --> "src/tools/llm_tools.py"
    "src/tools/doc_tools.py" --> "docling.document_converter"
    "src/tools/doc_tools.py" --> "json"
    "src/tools/doc_tools.py" --> "tempfile"
    "src/tools/doc_tools.py" --> "os"
```

## 2. Module Purpose Index
### `main.py`
**Purpose:** None
**Complexity:** 16.0 | **Velocity:** 4 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/graph.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 7 changes/30d

### `src/state.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 6 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `test_local.py`
**Purpose:** None
**Complexity:** 7.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `test_llm.py`
**Purpose:** None
**Complexity:** 4.0 | **Velocity:** 1 changes/30d

### `src/tools/llm_tools.py`
**Purpose:** None
**Complexity:** 5.0 | **Velocity:** 2 changes/30d

### `src/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/nodes/detectives.py`
**Purpose:** None
**Complexity:** 36.0 | **Velocity:** 10 changes/30d

### `src/nodes/judges.py`
**Purpose:** None
**Complexity:** 10.0 | **Velocity:** 6 changes/30d

### `src/nodes/justice.py`
**Purpose:** None
**Complexity:** 22.0 | **Velocity:** 8 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/tools/safety.py`
**Purpose:** None
**Complexity:** 11.0 | **Velocity:** 2 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/tools/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `src/tools/repo_tools.py`
**Purpose:** None
**Complexity:** 94.0 | **Velocity:** 7 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/tools/doc_tools.py`
**Purpose:** None
**Complexity:** 27.0 | **Velocity:** 5 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/nodes/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

## 3. Data Lineage Summary
Total Modules: 40
Total Dependencies: 70
