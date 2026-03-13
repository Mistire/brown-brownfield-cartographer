# FDE Day-One Onboarding Brief

> [!NOTE]
> This document is generated to accelerate the first 72 hours of embedding.

## 1. The Five Day-One Answers
### Q1: What is the primary data ingestion path?
stg_orders, stg_payments, stg_customers

### Q2: What are the 3-5 most critical output datasets/endpoints?
inferred_sink, customers, orders

### Q3: What is the blast radius if the most critical module fails?
Models/orders.sql, models/customers.sql, models/staging/stg_payments.sql, models/staging/stg_customers.sql, models/staging/stg_orders.sql

### Q4: Where is the business logic concentrated vs. distributed?
dbt_project.yml, models/orders.sql, models/customers.sql, models/schema.yml, models/staging/stg_payments.sql, models/staging/stg_customers.sql, models/staging/schema.yml, models/staging/stg_orders.sql

### Q5: What has changed most frequently in the last 90 days?
models/staging/stg_payments.sql, models/staging/stg_customers.sql, models/staging/stg_orders.sql

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
