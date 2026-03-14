# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-14 23:30

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

- `targets/jaffle_shop/dbt_project.yml`
- `targets/jaffle_shop/models/orders.sql`
- `targets/jaffle_shop/models/customers.sql`
- `targets/jaffle_shop/models/schema.yml`
- `targets/jaffle_shop/models/staging/stg_payments.sql`
- `targets/jaffle_shop/models/staging/stg_customers.sql`
- `targets/jaffle_shop/models/staging/schema.yml`
- `targets/jaffle_shop/models/staging/stg_orders.sql`

## 5. Recent Change Velocity (90-Day Map)
> [!TIP]
> High velocity files often indicate areas of high complexity or ongoing refactoring.


## 6. Module Purpose Index
### `targets/jaffle_shop/dbt_project.yml`
**Purpose:** This dbt project configuration establishes the 'jaffle_shop' data transformation pipeline by organizing code into models, seeds, tests, and macros, and defining materialization strategies—core models as persistent tables and staging models as lightweight views—to systematically convert raw data into analytics-ready structures. It manages build artifacts through target path cleaning and enforces dbt version compatibility, ensuring reliable and maintainable data processing for business reporting and analysis.
**Complexity:** 9.0 | **Domain:** N/A

### `targets/jaffle_shop/models/orders.sql`
**Purpose:** This code aggregates payment transactions by order to create a comprehensive order summary that includes total revenue and breakdowns by specific payment methods (e.g., credit_card, coupon). It enables business analytics by providing clear insights into revenue sources per order, supporting financial reporting, reconciliation, and analysis of payment method usage. The dynamic handling of payment methods ensures the output adapts to changes in payment options without code modifications.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/jaffle_shop/models/customers.sql`
**Purpose:** This code aggregates order and payment data per customer to compute key business metrics such as first order date, most recent order date, order count, and customer lifetime value (total payments). It integrates these aggregates with customer demographic details to create a unified customer profile, enabling analysis of customer behavior, value segmentation, and retention strategies for business intelligence and reporting.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/jaffle_shop/models/schema.yml`
**Purpose:** This code defines a data model schema that structures raw transactional data into business-ready tables for analytics. It creates a customers table aggregating order history (e.g., first order date, total spend) and an orders table detailing individual transactions with payment method splits, linked via foreign keys to support analysis of customer lifetime value, sales trends, and payment distribution.
**Complexity:** 6.5 | **Domain:** N/A

### `targets/jaffle_shop/models/staging/stg_payments.sql`
**Purpose:** This code transforms raw payment data by renaming the 'id' column to 'payment_id' and converting the 'amount' from cents to dollars, standardizing the data for downstream analytics and reporting. It acts as a staging model in a data pipeline, preparing seed data from 'raw_payments' for consistent business intelligence use.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/jaffle_shop/models/staging/stg_customers.sql`
**Purpose:** This code transforms raw customer data by renaming the 'id' column to 'customer_id' and selecting only first_name and last_name fields. It standardizes the customer identifier and reduces the dataset to core attributes, ensuring consistency and efficiency for downstream analytics and reporting. This acts as a cleaning step in the data pipeline to improve data quality and prepare it for further processing.
**Complexity:** 1.0 | **Domain:** N/A

### `targets/jaffle_shop/models/staging/schema.yml`
**Purpose:** This configuration defines staging data models for key business entities—customers, orders, and payments—and enforces data quality tests like uniqueness, non-null constraints, and accepted value lists on critical columns. It ensures that foundational data entering the pipeline is clean and reliable, supporting accurate analytics, reporting, and operational decisions by preventing invalid or inconsistent data from propagating downstream.
**Complexity:** 4.5 | **Domain:** N/A

### `targets/jaffle_shop/models/staging/stg_orders.sql`
**Purpose:** This code standardizes raw order data by renaming columns to business-friendly terms (e.g., `id` to `order_id`, `user_id` to `customer_id`) and selecting only key attributes like order date and status. It prepares a consistent, analytics-ready dataset for downstream reporting or business intelligence systems, ensuring uniform naming and focused data scope.
**Complexity:** 1.0 | **Domain:** N/A


## 7. System Statistics
Total Modules: 8
Total Dependencies: 0
