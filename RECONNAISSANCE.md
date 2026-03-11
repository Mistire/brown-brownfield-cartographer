# RECONNAISSANCE: jaffle_shop

## Five FDE Day-One Answers

### 1. What is the primary data ingestion path?
The data is ingested via CSV seed files located in the `seeds/` directory:
- `raw_customers.csv`
- `raw_orders.csv`
- `raw_payments.csv`

These are loaded into the database and then referenced by the staging models using `{{ ref() }}`.

### 2. What are the 3-5 most critical output datasets/endpoints?
The primary output datasets are:
- `customers`: Aggregates customer-level metrics like first order date, most recent order date, number of orders, and customer lifetime value (LTV).
- `orders`: Aggregates order-level metrics, including a pivot of payment methods and total amount.

### 3. What is the blast radius if the most critical module fails?
The staging models are the most critical "hubs". If `stg_orders.sql` fails:
- `orders.sql` will fail (direct dependency).
- `customers.sql` will fail (dependency on `stg_orders` for order counts and LTV calculation).
This effectively breaks all downstream reporting.

### 4. Where is the business logic concentrated vs. distributed?
- **Concentrated:** Metrics and business logic are in the final models:
    - `models/customers.sql`: LTV calculation and joining order/payment history.
    - `models/orders.sql`: Payment method pivoting logic.
- **Distributed:** Staging models (`models/staging/`) handle light transformation like renaming columns (`id` to `customer_id`) and simple type casting (e.g., cent-to-dollar conversion in `stg_payments.sql`).

### 5. What has changed most frequently in the last 90 days?
Based on the full git log (since recent activity is low):
- `models/customers.sql` (12 changes)
- `models/orders.sql` (8 changes)
- `dbt_project.yml` (5 changes)

## Difficulty Analysis

- **What was hardest to figure out manually?**
  Tracing the `amount` conversion from cents to dollars. It happens in `stg_payments.sql`, and if you only look at the final `customers` or `orders` model, it's not immediately obvious where that transformation occurred without searching for the column name across files.
- **Where did you get lost?**
  Following the join logic in `customers.sql` which pulls from three different staging models and handles multiple levels of aggregation (per order and then per customer). Mapping the grain of each CTE manually is tedious.
