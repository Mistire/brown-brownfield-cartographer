# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-11 16:27

### 1.1 System Map (Mermaid)
```mermaid
graph TD
    "tests/test_resolver.py" --> "pytest"
    "tests/test_resolver.py" --> "os"
    "tests/test_resolver.py" --> "src/utils/resolver.py"
    "src/utils/resolver.py" --> "os"
    "src/utils/resolver.py" --> "typing"
    "tests/test_hydrologist_ml.py" --> "pytest"
    "tests/test_hydrologist_ml.py" --> "os"
    "tests/test_hydrologist_ml.py" --> "src/analyzers/python_dataflow.py"
    "src/analyzers/python_dataflow.py" --> "tree_sitter"
    "src/analyzers/python_dataflow.py" --> "typing"
    "src/analyzers/python_dataflow.py" --> "src/analyzers/tree_sitter_analyzer.py"
    "src/analyzers/python_dataflow.py" --> "tree_sitter_languages"
    "tests/test_analyzer.py" --> "pytest"
    "tests/test_analyzer.py" --> "os"
    "tests/test_analyzer.py" --> "src/analyzers/tree_sitter_analyzer.py"
    "src/analyzers/tree_sitter_analyzer.py" --> "os"
    "src/analyzers/tree_sitter_analyzer.py" --> "json"
    "src/analyzers/tree_sitter_analyzer.py" --> "typing"
    "src/analyzers/tree_sitter_analyzer.py" --> "tree_sitter"
    "src/analyzers/tree_sitter_analyzer.py" --> "tree_sitter_languages"
    "src/cli.py" --> "argparse"
    "src/cli.py" --> "asyncio"
    "src/cli.py" --> "os"
    "src/cli.py" --> "sys"
    "src/cli.py" --> "src/agents/surveyor.py"
    "src/cli.py" --> "src/agents/hydrologist.py"
    "src/cli.py" --> "src/agents/semanticist.py"
    "src/cli.py" --> "src/agents/archivist.py"
    "src/agents/surveyor.py" --> "subprocess"
    "src/agents/surveyor.py" --> "os"
    "src/agents/surveyor.py" --> "json"
    "src/agents/surveyor.py" --> "datetime"
    "src/agents/surveyor.py" --> "typing"
    "src/agents/surveyor.py" --> "src/models/graph.py"
    "src/agents/surveyor.py" --> "src/analyzers/tree_sitter_analyzer.py"
    "src/agents/surveyor.py" --> "src/utils/resolver.py"
    "src/agents/hydrologist.py" --> "os"
    "src/agents/hydrologist.py" --> "typing"
    "src/agents/hydrologist.py" --> "src/models/graph.py"
    "src/agents/hydrologist.py" --> "src/analyzers/python_dataflow.py"
    "src/agents/hydrologist.py" --> "src/analyzers/sql_lineage.py"
    "src/agents/semanticist.py" --> "typing"
    "src/agents/semanticist.py" --> "os"
    "src/agents/semanticist.py" --> "google"
    "src/agents/semanticist.py" --> "src/models/graph.py"
    "src/agents/archivist.py" --> "os"
    "src/agents/archivist.py" --> "json"
    "src/agents/archivist.py" --> "datetime"
    "src/agents/archivist.py" --> "typing"
    "src/agents/archivist.py" --> "pyvis.network"
    "src/models/graph.py" --> "datetime"
    "src/models/graph.py" --> "typing"
    "src/models/graph.py" --> "pydantic"
    "src/analyzers/sql_lineage.py" --> "typing"
    "src/analyzers/sql_lineage.py" --> "sqlglot"
    "src/analyzers/sql_lineage.py" --> "re"
    "src/agents/navigator.py" --> "typing"
    "src/agents/navigator.py" --> "json"
    "src/agents/navigator.py" --> "os"
    "src/agents/navigator.py" --> "langgraph.graph"
    "src/agents/navigator.py" --> "langchain_core.messages"
    "src/agents/navigator.py" --> "src/agents/surveyor.py"
    "src/agents/navigator.py" --> "src/agents/hydrologist.py"
```

## 2. Module Purpose Index
### `tests/test_resolver.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/utils/resolver.py`
**Purpose:** None
**Complexity:** 9.0 | **Velocity:** 0 changes/30d

### `tests/test_hydrologist_ml.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `src/analyzers/python_dataflow.py`
**Purpose:** None
**Complexity:** 11.0 | **Velocity:** 1 changes/30d

### `tests/test_analyzer.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `src/analyzers/tree_sitter_analyzer.py`
**Purpose:** None
**Complexity:** 27.0 | **Velocity:** 1 changes/30d

### `src/cli.py`
**Purpose:** None
**Complexity:** 3.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/agents/surveyor.py`
**Purpose:** None
**Complexity:** 14.0 | **Velocity:** 1 changes/30d

### `src/agents/hydrologist.py`
**Purpose:** None
**Complexity:** 12.0 | **Velocity:** 1 changes/30d

### `src/agents/semanticist.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 1 changes/30d

### `src/agents/archivist.py`
**Purpose:** None
**Complexity:** 13.0 | **Velocity:** 1 changes/30d

### `src/brownfield_cartographer/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

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

### `src/models/graph.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/analyzers/sql_lineage.py`
**Purpose:** None
**Complexity:** 6.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `src/agents/navigator.py`
**Purpose:** None
**Complexity:** 7.0 | **Velocity:** 1 changes/30d

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

### `src/models/__init__.py`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 1 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/pnpm-workspace.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/pnpm-lock.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/docker-compose.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/nextjs/pnpm-workspace.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/nextjs/pnpm-lock.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/stateless/pnpm-workspace.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/stateless/pnpm-lock.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/expo/pnpm-workspace.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/expo/pnpm-lock.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/oidc-client/pnpm-workspace.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/oidc-client/pnpm-lock.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/electron/pnpm-workspace.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/electron/electron-builder.yml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/electron/pnpm-lock.yaml`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/packages/cli/test/__snapshots__/migrations-uuid.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/packages/cli/test/__snapshots__/migrations.sql`
**Purpose:** None
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

## 3. Data Lineage Summary
Total Modules: 51
Total Dependencies: 63
