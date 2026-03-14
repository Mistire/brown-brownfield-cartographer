# FDE Day-One Onboarding Brief

> [!IMPORTANT]
> This document is synthesized by the Brownfield Cartographer to accelerate FDE onboarding within the first 72 hours.

## 1. The Five Day-One Answers
### Q1: What is the primary data ingestion path?
The primary data ingestion path is through the staging models in the ingestion domain, specifically the files: targets/jaffle_shop_duckdb/models/staging/stg_payments.sql, targets/jaffle_shop_duckdb/models/staging/stg_customers.sql, and targets/jaffle_shop_duckdb/models/staging/stg_orders.sql. These models ingest from sources stg_payments, stg_customers, and stg_orders as defined in targets/jaffle_shop_duckdb/models/staging/schema.yml. Note: The sources list includes 'TEMPLATE_VAR', which appears to be a placeholder and is not reflected in the ingestion files.

### Q2: What are the 3-5 most critical output datasets/endpoints?
The 3 most critical output datasets/endpoints are the sinks: customers, orders, and result_set, as they represent the final outputs of the data pipeline.

### Q3: What is the blast radius if the most critical module fails?
Analysis inconclusive. The provided evidence lacks a dependency graph or PageRank scores to quantify blast radius. Based on the domain_map, modules like orders.sql and customers.sql produce sinks, but without edge data, the impact of failure cannot be determined.

### Q4: Where is the business logic concentrated vs. distributed?
Business logic is concentrated in the transformation domain, specifically in targets/jaffle_shop_duckdb/models/orders.sql and targets/jaffle_shop_duckdb/models/customers.sql. The ingestion domain (staging models) handles minimal transformations, and the infra domain is configuration-only, indicating a clustered rather than distributed logic pattern.

### Q5: What has changed most frequently in the last 90 days?
Analysis inconclusive. Git velocity or change frequency data for the last 90 days is not provided in the architectural evidence.

## 2. High-Velocity Hotspots (Maintenance Map)
- `targets/jaffle_shop_duckdb/dbt_project.yml`: **1** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/jaffle_shop_duckdb/models/schema.yml`: **1** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/jaffle_shop_duckdb/models/staging/schema.yml`: **1** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/jaffle_shop_duckdb/profiles.yml`: **0** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/jaffle_shop_duckdb/models/orders.sql`: **0** changes/30d. (Area of likely technical debt or high feature flux)

## 3. High Complexity Risk Modules
- `targets/jaffle_shop_duckdb/dbt_project.yml`: Complexity Score **10.5**. (Recommended for refactoring or deep-dive testing)
- `targets/jaffle_shop_duckdb/models/schema.yml`: Complexity Score **7.0**. (Recommended for refactoring or deep-dive testing)
- `targets/jaffle_shop_duckdb/models/staging/schema.yml`: Complexity Score **5.0**. (Recommended for refactoring or deep-dive testing)
- `targets/jaffle_shop_duckdb/profiles.yml`: Complexity Score **4.5**. (Recommended for refactoring or deep-dive testing)
- `targets/jaffle_shop_duckdb/models/orders.sql`: Complexity Score **1.0**. (Recommended for refactoring or deep-dive testing)
