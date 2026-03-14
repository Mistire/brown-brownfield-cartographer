# FDE Day-One Onboarding Brief

> [!IMPORTANT]
> This document is synthesized by the Brownfield Cartographer to accelerate FDE onboarding within the first 72 hours.

## 1. The Five Day-One Answers
### Q1: What is the primary data ingestion path?
The primary data ingestion path is through the staging models in the ingestion domain: targets/jaffle_shop/models/staging/stg_payments.sql, targets/jaffle_shop/models/staging/stg_customers.sql, and targets/jaffle_shop/models/staging/stg_orders.sql. These correspond to the sources stg_payments, stg_customers (implied from domain_map), and stg_orders, with TEMPLATE_VAR likely being a variable placeholder not directly tied to a file.

### Q2: What are the 3-5 most critical output datasets/endpoints?
The most critical output datasets/endpoints are the sinks: result_set, customers, and orders. These represent the final outputs of the data pipeline.

### Q3: What is the blast radius if the most critical module fails?
Analysis inconclusive. The provided evidence lacks PageRank scores or dependency edges to assess blast radius; top_hubs is empty and no graph structure is given.

### Q4: Where is the business logic concentrated vs. distributed?
Business logic is concentrated in the transformation domain files: targets/jaffle_shop/models/orders.sql and targets/jaffle_shop/models/customers.sql. The logic domain (schema.yml files) distributes semantic definitions and metadata, but core transformation logic resides in the transformation models.

### Q5: What has changed most frequently in the last 90 days?
Analysis inconclusive. No git history or change frequency data is provided to identify velocity hotspots over the last 90 days.

## 2. High-Velocity Hotspots (Maintenance Map)
- `targets/jaffle_shop/dbt_project.yml`: **0** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/jaffle_shop/models/orders.sql`: **0** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/jaffle_shop/models/customers.sql`: **0** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/jaffle_shop/models/schema.yml`: **0** changes/30d. (Area of likely technical debt or high feature flux)
- `targets/jaffle_shop/models/staging/stg_payments.sql`: **0** changes/30d. (Area of likely technical debt or high feature flux)

## 3. High Complexity Risk Modules
- `targets/jaffle_shop/dbt_project.yml`: Complexity Score **9.0**. (Recommended for refactoring or deep-dive testing)
- `targets/jaffle_shop/models/schema.yml`: Complexity Score **6.5**. (Recommended for refactoring or deep-dive testing)
- `targets/jaffle_shop/models/staging/schema.yml`: Complexity Score **4.5**. (Recommended for refactoring or deep-dive testing)
- `targets/jaffle_shop/models/orders.sql`: Complexity Score **1.0**. (Recommended for refactoring or deep-dive testing)
- `targets/jaffle_shop/models/customers.sql`: Complexity Score **1.0**. (Recommended for refactoring or deep-dive testing)
