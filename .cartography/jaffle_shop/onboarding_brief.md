# FDE Day-One Onboarding Brief

> [!NOTE]
> This document is generated to accelerate the first 72 hours of embedding.

## 1. The Five Day-One Answers
### Q1: What is the primary data ingestion path?
Data is ingested from `stg_orders`, `stg_payments`, and `stg_customers`. These appear to be staging tables, suggesting an ELT process.

### Q2: What are the 3-5 most critical output datasets/endpoints?
The critical outputs are `inferred_sink`, `customers`, and `orders`. `customers` and `orders` are likely core business tables, and `inferred_sink` suggests a downstream application or reporting layer.

### Q3: What is the blast radius if the most critical module fails?
The blast radius is moderate. Errors in the staging models (`stg_orders`, `stg_payments`, `stg_customers`) will impact the `customers` and `orders` tables, and potentially the `inferred_sink`. The impact is contained within this data pipeline, but core business data is affected.

### Q4: Where is the business logic concentrated vs. distributed?
Logic is distributed across dbt project configuration (`dbt_project.yml`, `models/schema.yml`, `models/staging/schema.yml`) and SQL models for staging (`models/staging/stg_orders.sql`, `models/staging/stg_payments.sql`, `models/staging/stg_customers.sql`) and core tables (`models/orders.sql`, `models/customers.sql`).

### Q5: What has changed most frequently in the last 90 days?
Change hotspots are likely to be the staging models (`stg_orders`, `stg_payments`, `stg_customers`) as they are the first point of transformation. Changes to the schema or logic in these models will ripple through the pipeline. Also, `dbt_project.yml` and the schema files (`schema.yml`) are hotspots for configuration changes.

## 2. High-Velocity Hotspots
- `dbt_project.yml` (0 changes/30d)
- `models/orders.sql` (0 changes/30d)
- `models/customers.sql` (0 changes/30d)
- `models/schema.yml` (0 changes/30d)
- `models/staging/stg_payments.sql` (0 changes/30d)

## 3. Top Complexity Risks
- `dbt_project.yml` (Complexity: 9.0)
- `models/schema.yml` (Complexity: 6.5)
- `models/staging/schema.yml` (Complexity: 4.5)
- `models/orders.sql` (Complexity: 1.0)
- `models/customers.sql` (Complexity: 1.0)
