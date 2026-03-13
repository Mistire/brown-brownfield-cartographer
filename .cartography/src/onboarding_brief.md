# FDE Day-One Onboarding Brief

> [!NOTE]
> This document is generated to accelerate the first 72 hours of embedding.

## 1. The Five Day-One Answers
### Q1: What is the primary data ingestion path?
The primary data ingestion path flows through: src/agents/surveyor.py (initial scanning), src/agents/hydrologist.py (data collection), and src/analyzers/tree_sitter_analyzer.py (AST parsing). These three files form the core ingestion pipeline, with surveyor.py initiating the process, hydrologist.py handling data extraction, and tree_sitter_analyzer.py performing the initial analysis.

### Q2: What are the 3-5 most critical output datasets/endpoints?
Analysis inconclusive - The provided context shows empty 'sources' and 'sinks' arrays with no identified output datasets or endpoints.

### Q3: What is the blast radius if the most critical module fails?
Analysis inconclusive - The provided context lacks PageRank metrics and edge relationship data needed to determine blast radius impact.

### Q4: Where is the business logic concentrated vs. distributed?
Business logic is concentrated in the 'logic' domain cluster, specifically in src/orchestrator.py (coordination), src/graph/knowledge_graph.py (core graph operations), src/cli.py (interface), src/agents/navigator.py (navigation logic), and src/agents/archivist.py (storage logic). This represents a centralized logic architecture rather than distributed logic.

### Q5: What has changed most frequently in the last 90 days?
Analysis inconclusive - The provided context contains no Git velocity data or change frequency information for the last 90 days.

## 2. High-Velocity Hotspots
- `src/__init__.py` (0 changes/30d)
- `src/orchestrator.py` (0 changes/30d)
- `src/agents/surveyor.py` (0 changes/30d)
- `src/agents/hydrologist.py` (0 changes/30d)
- `src/agents/semanticist.py` (0 changes/30d)

## 3. Top Complexity Risks
- `src/analyzers/tree_sitter_analyzer.py` (Complexity: 42.0)
- `src/agents/archivist.py` (Complexity: 31.0)
- `src/analyzers/dag_config_parser.py` (Complexity: 30.0)
- `src/agents/hydrologist.py` (Complexity: 24.0)
- `src/agents/semanticist.py` (Complexity: 21.0)
