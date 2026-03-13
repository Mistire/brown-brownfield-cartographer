# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-14 01:44

### 1.1 System Map (Mermaid)
```mermaid
graph TD
    "orchestrator.py" --> "agents/surveyor.py"
    "orchestrator.py" --> "agents/hydrologist.py"
    "orchestrator.py" --> "agents/semanticist.py"
    "orchestrator.py" --> "agents/archivist.py"
    "orchestrator.py" --> "graph/knowledge_graph.py"
    "agents/surveyor.py" --> "models/graph.py"
    "agents/surveyor.py" --> "analyzers/tree_sitter_analyzer.py"
    "agents/surveyor.py" --> "utils/resolver.py"
    "agents/hydrologist.py" --> "models/graph.py"
    "agents/hydrologist.py" --> "analyzers/python_dataflow.py"
    "agents/hydrologist.py" --> "analyzers/sql_lineage.py"
    "agents/hydrologist.py" --> "analyzers/dag_config_parser.py"
    "agents/semanticist.py" --> "models/graph.py"
    "agents/archivist.py" --> "utils/paths.py"
    "cli.py" --> "orchestrator.py"
    "cli.py" --> "agents/navigator.py"
    "agents/navigator.py" --> "graph/knowledge_graph.py"
    "agents/navigator.py" --> "utils/paths.py"
    "agents/navigator.py" --> "agents/archivist.py"
    "analyzers/python_dataflow.py" --> "analyzers/tree_sitter_analyzer.py"
```

## 2. Critical Architectural Hubs (PageRank)
- **`src/utils/paths.py`**: Centrality Score 0.1082
- **`src/models/graph.py`**: Centrality Score 0.1031
- **`src/analyzers/tree_sitter_analyzer.py`**: Centrality Score 0.0936

## 3. Architectural Debt & Risks

### 3.2 Dead Code Candidates
> [!NOTE]
> These modules have zero in-degree (no detected imports). Verify if they are entry points or unused.

- `src/__init__.py`
- `src/cli.py`
- `src/models/__init__.py`

## 4. Module Purpose Index
### `src/__init__.py`
**Purpose:** The code defines a simple function that returns a greeting string, likely serving as a basic test or placeholder for a larger system.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `src/orchestrator.py`
**Purpose:** Orchestrates a multi-stage software analysis pipeline that analyzes codebases to extract structural and semantic insights, including dependency graphs, code purpose statements, and documentation drift detection, then generates comprehensive artifacts like interactive visualizations and onboarding briefs.
**Complexity:** 14.0 | **Velocity:** 0 changes/30d

### `src/agents/surveyor.py`
**Purpose:** This code analyzes a software repository to build a dependency graph of modules, capturing their relationships and change frequency over time. It scans source files, extracts import dependencies using a tree-sitter analyzer, and enriches nodes with git velocity data to identify frequently changing files.
**Complexity:** 20.0 | **Velocity:** 0 changes/30d

### `src/agents/hydrologist.py`
**Purpose:** The Hydrologist class analyzes Python, SQL, and YAML files to extract data lineage information, building a directed graph that maps how datasets flow between sources, transformations, and sinks. It supports both incremental and full repository scans, identifying data dependencies and relationships across the codebase.
**Complexity:** 24.0 | **Velocity:** 0 changes/30d

### `src/agents/semanticist.py`
**Purpose:** The Semanticist class provides LLM-powered analysis capabilities for brownfield software projects, including generating purpose statements from code, detecting documentation drift, clustering modules into business domains, and synthesizing onboarding briefs. It acts as an intelligent analysis layer that uses OpenAI models to extract architectural insights and business context from codebases.
**Complexity:** 21.0 | **Velocity:** 0 changes/30d

### `src/agents/archivist.py`
**Purpose:** Generates comprehensive architectural documentation and interactive visualizations for a software system, including a structured CODEBASE.md report with system maps, architectural hubs, debt analysis, and module metadata, plus an interactive HTML graph for exploration.
**Complexity:** 31.0 | **Velocity:** 0 changes/30d

### `src/graph/knowledge_graph.py`
**Purpose:** This class provides a centralized graph-based knowledge management system for tracking both software module dependencies and data lineage relationships, enabling analysis of system architecture through metrics like PageRank centrality, circular dependencies, and blast radius calculations.
**Complexity:** 13.0 | **Velocity:** 0 changes/30d

### `src/cli.py`
**Purpose:** This code provides a command-line interface for analyzing and querying software repositories, enabling users to generate artifacts from repository analysis or interactively query previously analyzed repositories. It orchestrates the analysis pipeline through an Orchestrator class and facilitates repository querying via a Navigator class.
**Complexity:** 9.0 | **Velocity:** 0 changes/30d

### `src/agents/navigator.py`
**Purpose:** The Navigator class provides a query interface to a codebase knowledge graph, allowing users to semantically search for implementations, trace data lineage, identify module dependencies, and explain specific modules using a LangGraph agent with LLM-powered tool selection.
**Complexity:** 19.0 | **Velocity:** 0 changes/30d

### `src/models/graph.py`
**Purpose:** Defines data models for representing software architecture components and their relationships in a codebase analysis system, including modules, functions, datasets, and transformations.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `src/analyzers/tree_sitter_analyzer.py`
**Purpose:** This code analyzes source code files to extract structural and semantic information such as imports, functions, classes, decorators, type hints, and complexity metrics using tree-sitter parsers for multiple programming languages.
**Complexity:** 42.0 | **Velocity:** 0 changes/30d

### `src/utils/resolver.py`
**Purpose:** The PathResolver class resolves import strings and relative paths to absolute filesystem paths within a repository, supporting both absolute imports (e.g., src.utils.auth) and relative imports (e.g., ..common.utils) by converting dot notation to path separators and checking for .py, .sql, or directory/__init__.py files.
**Complexity:** 9.0 | **Velocity:** 0 changes/30d

### `src/analyzers/python_dataflow.py`
**Purpose:** Extracts data flow patterns from Python source code by identifying I/O operations (file reads/writes, data loading/saving) and machine learning method calls (fit, predict, score, transform) using tree-sitter AST queries.
**Complexity:** 11.0 | **Velocity:** 0 changes/30d

### `src/analyzers/sql_lineage.py`
**Purpose:** Extracts table dependencies and lineage from SQL queries by parsing the SQL structure to identify source tables, target tables, and transformation types. It handles both standard SQL dialects and dbt-specific patterns, providing structured lineage data for data pipeline analysis.
**Complexity:** 17.0 | **Velocity:** 0 changes/30d

### `src/analyzers/dag_config_parser.py`
**Purpose:** Extracts and consolidates pipeline topology metadata from dbt schema files, dbt project configurations, and Airflow DAG files to provide a unified view of data pipeline structure and dependencies.
**Complexity:** 30.0 | **Velocity:** 0 changes/30d

### `src/utils/paths.py`
**Purpose:** This module provides utility functions to determine key directory paths within the project structure, specifically the project root and a .cartography subdirectory.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `src/models/__init__.py`
**Purpose:** The code appears to be a configuration or setup module for a larger system, likely defining constants, default values, or initialization parameters for other components to use.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

## 5. Data Sources & Sinks
### 5.1 Primary Sources (Ingestion)
No distinct sources identified.

### 5.2 Primary Sinks (Output)
No distinct sinks identified.

## 6. High-Velocity Core (Maintenance Hotspots)
> [!TIP]
> These files have the highest change frequency in the last 30 days.


## 7. System Statistics
Total Modules: 17
Total Dependencies: 20
