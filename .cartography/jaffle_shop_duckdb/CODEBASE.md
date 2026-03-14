# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-14 23:02

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

- `targets/jaffle_shop_duckdb/dbt_project.yml`
- `targets/jaffle_shop_duckdb/profiles.yml`
- `targets/jaffle_shop_duckdb/models/orders.sql`
- `targets/jaffle_shop_duckdb/models/customers.sql`
- `targets/jaffle_shop_duckdb/models/schema.yml`
- `targets/jaffle_shop_duckdb/models/staging/stg_payments.sql`
- `targets/jaffle_shop_duckdb/models/staging/stg_customers.sql`
- `targets/jaffle_shop_duckdb/models/staging/schema.yml`
- `targets/jaffle_shop_duckdb/models/staging/stg_orders.sql`

## 5. Recent Change Velocity (90-Day Map)
> [!TIP]
> High velocity files often indicate areas of high complexity or ongoing refactoring.

- `targets/jaffle_shop_duckdb/dbt_project.yml`: **1** changes in last 30 days
- `targets/jaffle_shop_duckdb/models/schema.yml`: **1** changes in last 30 days
- `targets/jaffle_shop_duckdb/models/staging/schema.yml`: **1** changes in last 30 days

## 6. Module Purpose Index
### `targets/jaffle_shop_duckdb/dbt_project.yml`
**Purpose:** This dbt project configuration defines the structure and behavior of a data transformation pipeline for the 'jaffle_shop' analytics system. It specifies paths for organizing models, seeds, tests, and macros, and sets materialization strategies—such as building final models as tables and staging models as views—to systematically convert raw data into persistent analytics tables. The configuration ensures version compatibility, cleanup of build artifacts, and consistent execution for reliable business intelligence outputs.
**Complexity:** 10.5 | **Domain:** N/A

### `targets/jaffle_shop_duckdb/profiles.yml`
**Purpose:** This configuration defines the development environment for the jaffle_shop data pipeline, routing all data transformations and queries to a local DuckDB database file named 'jaffle_shop.duckdb' with 24 threads for parallel processing. It isolates development work from production by using a file-based storage system, enabling safe and efficient iteration on data models. The setup optimizes local testing and debugging by specifying database type, path, and thread count directly in the pipeline configuration.
**Complexity:** 4.5 | **Domain:** N/A

### `targets/jaffle_shop_duckdb/models/orders.sql`
**Purpose:** This code aggregates payment data by order and payment method to create a unified dataset that breaks down the total amount paid for each order into specific payment channels (credit card, coupon, bank transfer, gift card). It joins this aggregated payment information with order details from staging tables, enabling financial analysis such as revenue tracking, payment method distribution, and order reconciliation for business reporting.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/jaffle_shop_duckdb/models/customers.sql`
**Purpose:** This code aggregates raw customer, order, and payment data to compute essential customer-centric metrics such as first order date, most recent order date, total number of orders, and customer lifetime value. By joining these aggregates with customer details, it creates a unified customer profile table that supports business analytics, such as customer segmentation, behavior analysis, and lifetime value calculation.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/jaffle_shop_duckdb/models/schema.yml`
**Purpose:** This schema configures analytical data models that aggregate customer order metrics (e.g., number_of_orders, total_order_amount) and detail order payment breakdowns (e.g., credit_card_amount, coupon_amount). It enables business intelligence on customer lifetime value, order fulfillment trends, and payment method distribution by structuring transactional data into ready-for-analysis tables.
**Complexity:** 7.0 | **Domain:** N/A

### `targets/jaffle_shop_duckdb/models/staging/stg_payments.sql`
**Purpose:** This code standardizes raw payment data for business analytics by renaming the 'id' column to 'payment_id' for clarity and converting the 'amount' from cents to dollars to ensure monetary values are in a consistent unit. This transformation enables accurate financial reporting and analysis downstream.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/jaffle_shop_duckdb/models/staging/stg_customers.sql`
**Purpose:** This code standardizes raw customer data by renaming the 'id' column to 'customer_id' and selecting only first and last names, creating a clean and consistent customer attribute dataset. It acts as a foundational transformation in the data pipeline, ensuring downstream analytics and reporting use unified, relevant customer information while discarding unnecessary or raw fields.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/jaffle_shop_duckdb/models/staging/schema.yml`
**Purpose:** This configuration defines data quality tests for staging models of customers, orders, and payments to enforce integrity at the data ingestion layer. It specifies that identifiers like customer_id, order_id, and payment_id must be unique and non-null, and that order status and payment method fields are restricted to predefined acceptable values, preventing invalid data from entering downstream analytics or reporting systems.
**Complexity:** 5.0 | **Domain:** N/A

### `targets/jaffle_shop_duckdb/models/staging/stg_orders.sql`
**Purpose:** This code transforms raw order data by renaming columns to more descriptive business terms, specifically mapping 'id' to 'order_id' and 'user_id' to 'customer_id'. It serves as a staging step in a data pipeline to standardize column names for downstream analytics or reporting, ensuring consistency and clarity in the data model. The use of dbt's ref function indicates it integrates with a modular data transformation workflow, pulling from a seed or model named 'raw_orders'.
**Complexity:** 1.0 | **Domain:** N/A


## 7. System Statistics
Total Modules: 9
Total Dependencies: 0
