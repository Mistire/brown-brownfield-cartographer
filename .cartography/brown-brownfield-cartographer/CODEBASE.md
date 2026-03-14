# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-14 20:28

> [!IMPORTANT]
> This is a live, queryable map of the system's architecture and data flows.

### 1.1 System Map (Mermaid)
```mermaid
graph TD
```

## 2. Critical Path & Architectural Hubs

## 3. Data Sources & Sinks
### 3.1 Known Inputs (Sources)
No distinct sources identified via static analysis.

### 3.2 Known Outputs (Sinks)
No distinct sinks identified via static analysis.

## 4. Technical Debt & Safety Risks

### 4.2 Dead Code Candidates
> [!NOTE]
> Zero detected incoming references. Candidate for removal if not an entry point.

- `targets/brown-brownfield-cartographer/tests/test_resolver.py`
- `targets/brown-brownfield-cartographer/tests/test_hydrologist_ml.py`
- `targets/brown-brownfield-cartographer/tests/test_analyzer.py`
- `targets/brown-brownfield-cartographer/scripts/verify_context_injection.py`
- `targets/brown-brownfield-cartographer/src/__init__.py`
- `targets/brown-brownfield-cartographer/src/orchestrator.py`
- `targets/brown-brownfield-cartographer/src/cli.py`
- `targets/brown-brownfield-cartographer/src/graph/knowledge_graph.py`
- `targets/brown-brownfield-cartographer/src/agents/surveyor.py`
- `targets/brown-brownfield-cartographer/src/agents/semanticist.py`
- `targets/brown-brownfield-cartographer/src/agents/hydrologist.py`
- `targets/brown-brownfield-cartographer/src/agents/archivist.py`
- `targets/brown-brownfield-cartographer/src/agents/navigator.py`
- `targets/brown-brownfield-cartographer/src/analyzers/sql_lineage.py`
- `targets/brown-brownfield-cartographer/src/analyzers/python_dataflow.py`
- `targets/brown-brownfield-cartographer/src/analyzers/tree_sitter_analyzer.py`
- `targets/brown-brownfield-cartographer/src/analyzers/dag_config_parser.py`
- `targets/brown-brownfield-cartographer/src/utils/paths.py`
- `targets/brown-brownfield-cartographer/src/utils/resolver.py`
- `targets/brown-brownfield-cartographer/src/models/__init__.py`
- `targets/brown-brownfield-cartographer/src/models/graph.py`

## 5. Recent Change Velocity (90-Day Map)
> [!TIP]
> High velocity files often indicate areas of high complexity or ongoing refactoring.

- `targets/brown-brownfield-cartographer/src/agents/semanticist.py`: **8** changes in last 30 days
- `targets/brown-brownfield-cartographer/src/agents/navigator.py`: **8** changes in last 30 days
- `targets/brown-brownfield-cartographer/src/orchestrator.py`: **7** changes in last 30 days
- `targets/brown-brownfield-cartographer/src/agents/surveyor.py`: **6** changes in last 30 days
- `targets/brown-brownfield-cartographer/src/analyzers/tree_sitter_analyzer.py`: **6** changes in last 30 days

## 6. Module Purpose Index
### `targets/brown-brownfield-cartographer/tests/test_resolver.py`
**Purpose:** The code tests a path resolution utility that resolves module import paths to file system paths within a repository, handling both absolute and relative imports.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/tests/test_hydrologist_ml.py`
**Purpose:** The code tests a Python data flow analyzer's ability to detect and classify input/output operations in a machine learning script, specifically verifying that it correctly identifies data sources, transformations, and sinks like CSV reads/writes and model training/prediction calls.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/tests/test_analyzer.py`
**Purpose:** The code tests a Python code analysis tool by verifying it correctly identifies language, imports, classes, and functions in a given Python module.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/scripts/verify_context_injection.py`
**Purpose:** This code verifies context injection by loading a codebase documentation file, priming an AI agent with its contents, and querying it about circular dependencies and associated risks in the architecture. It serves as a validation tool to ensure the AI can accurately analyze and provide insights on the system's structural integrity.
**Complexity:** 5.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/__init__.py`
**Purpose:** The code defines a simple function that returns a greeting message, likely serving as a basic health check or placeholder for a larger system.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/orchestrator.py`
**Purpose:** The Orchestrator class coordinates a multi-stage software analysis pipeline that processes code repositories through sequential agents (Surveyor, Hydrologist, Semanticist, Archivist) to extract structural, semantic, and documentation insights, then generates comprehensive artifacts including knowledge graphs, onboarding briefs, and interactive visualizations.
**Complexity:** 14.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/cli.py`
**Purpose:** This code provides a command-line interface for analyzing and querying software repositories, enabling users to generate artifacts from repository analysis or interactively query previously analyzed repositories. It orchestrates the analysis pipeline through an Orchestrator class and facilitates repository querying via a Navigator class.
**Complexity:** 9.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/graph/knowledge_graph.py`
**Purpose:** The KnowledgeGraph class manages and analyzes module dependencies and data lineage using NetworkX graphs, providing methods to add nodes and edges, compute centrality metrics like PageRank, identify circular dependencies and dead code, and serialize/deserialize the graph state for persistence.
**Complexity:** 13.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/agents/surveyor.py`
**Purpose:** This code analyzes a software repository to build a dependency graph of modules, capturing their relationships and change frequency. It scans source files, extracts import dependencies, and enriches nodes with git velocity data to identify frequently changing files.
**Complexity:** 20.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/agents/semanticist.py`
**Purpose:** The Semanticist class orchestrates LLM-powered analysis of brownfield codebases, generating purpose statements, detecting documentation drift, clustering modules into domains, and synthesizing onboarding briefs. It acts as an intelligent analysis layer that uses OpenAI-compatible APIs to extract architectural insights from code evidence.
**Complexity:** 21.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/agents/hydrologist.py`
**Purpose:** The code analyzes Python, SQL, and YAML files in a repository to extract data lineage information, building a directed graph that maps how datasets flow between files and transformations. It identifies data sources, sinks, and dependencies, then provides methods to query blast radius, sources, and sinks, and save the lineage graph.
**Complexity:** 24.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/agents/archivist.py`
**Purpose:** Generates comprehensive architectural documentation and interactive visualizations from a dependency graph, including a structured CODEBASE.md report with system maps, debt analysis, and module metadata, plus an interactive HTML graph for exploration.
**Complexity:** 31.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/agents/navigator.py`
**Purpose:** The Navigator class provides a query interface to a codebase knowledge graph, allowing users to semantically search for implementations, trace data lineage, identify module dependencies, and explain specific modules using a LangGraph agent with LLM-powered tool selection.
**Complexity:** 19.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/analyzers/sql_lineage.py`
**Purpose:** Extracts table dependencies and transformation lineage from SQL queries by parsing the query structure to identify source tables, target tables, and transformation types, then returns this information as structured data for downstream analysis.
**Complexity:** 17.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/analyzers/python_dataflow.py`
**Purpose:** Extracts data flow patterns from Python source code by analyzing ASTs to identify I/O operations (file reads/writes, data loading/saving) and machine learning method calls (fit, predict, score, transform). The analyzer parses Python files, queries the AST for specific patterns using tree-sitter, and returns structured information about data sources, sinks, and transformations found in the code.
**Complexity:** 11.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/analyzers/tree_sitter_analyzer.py`
**Purpose:** Analyzes source code files to extract structural and semantic information such as imports, functions, classes, decorators, type hints, and complexity metrics using tree-sitter parsers, supporting Python, SQL, YAML, and Jupyter notebooks.
**Complexity:** 42.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/analyzers/dag_config_parser.py`
**Purpose:** Extracts and consolidates pipeline topology metadata from dbt schema.yml files and Airflow DAG Python files to enable analysis of data pipeline structure and dependencies.
**Complexity:** 30.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/utils/paths.py`
**Purpose:** This module provides utility functions to determine key directory paths within the project structure, specifically the project root and a .cartography subdirectory.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/utils/resolver.py`
**Purpose:** Resolves import strings and relative paths to absolute filesystem paths within a repository, supporting both absolute imports (e.g., src.utils.auth) and relative imports (e.g., ..common.utils) by converting them to valid file paths and checking for .py, .sql, or __init__.py files.
**Complexity:** 9.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/models/__init__.py`
**Purpose:** The code appears to be a configuration or setup component for a larger system, likely defining parameters or initializing services for a pipeline or application.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/brown-brownfield-cartographer/src/models/graph.py`
**Purpose:** Defines data models for representing software architecture components and their relationships in a codebase analysis system, including modules, functions, datasets, transformations, and connections between them.
**Complexity:** 1.0 | **Domain:** N/A


## 7. System Statistics
Total Modules: 21
Total Dependencies: 0
