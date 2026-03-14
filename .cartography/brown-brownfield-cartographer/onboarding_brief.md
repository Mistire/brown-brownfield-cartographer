# FDE Day-One Onboarding Brief

> [!IMPORTANT]
> This document is synthesized by the Brownfield Cartographer to accelerate FDE onboarding within the first 72 hours.

## 1. The Five Day-One Answers
### Q1: What is the primary data ingestion path?
tests/test_hydrologist_ml.py, src/agents/archivist.py

### Q2: What are the 3-5 most critical output datasets/endpoints?
Analysis inconclusive

### Q3: What is the blast radius if the most critical module fails?
Analysis inconclusive

### Q4: Where is the business logic concentrated vs. distributed?
Analysis inconclusive

### Q5: What has changed most frequently in the last 90 days?
Analysis inconclusive

## 2. High-Velocity Hotspots (Maintenance Map)
- `targets/brown-brownfield-cartographer/src/agents/semanticist.py`: **8** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/brown-brownfield-cartographer/src/agents/navigator.py`: **8** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/brown-brownfield-cartographer/src/orchestrator.py`: **7** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/brown-brownfield-cartographer/src/agents/surveyor.py`: **6** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/brown-brownfield-cartographer/src/analyzers/tree_sitter_analyzer.py`: **6** changes/30d. (Area of likely technical debt or high feature flux)

## 3. High Complexity Risk Modules
- `targets/brown-brownfield-cartographer/src/analyzers/tree_sitter_analyzer.py`: Complexity Score **42.0**. (Recommended for refactoring or deep-dive testing)
- `targets/brown-brownfield-cartographer/src/agents/archivist.py`: Complexity Score **31.0**. (Recommended for refactoring or deep-dive testing)
- `targets/brown-brownfield-cartographer/src/analyzers/dag_config_parser.py`: Complexity Score **30.0**. (Recommended for refactoring or deep-dive testing)
- `targets/brown-brownfield-cartographer/src/agents/hydrologist.py`: Complexity Score **24.0**. (Recommended for refactoring or deep-dive testing)
- `targets/brown-brownfield-cartographer/src/agents/semanticist.py`: Complexity Score **21.0**. (Recommended for refactoring or deep-dive testing)
