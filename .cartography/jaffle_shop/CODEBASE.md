# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-13 13:33

### 1.1 System Map (Mermaid)
```mermaid
graph TD
    "models/orders.sql" --> "payment_methods"
    "models/orders.sql" --> "order_payments"
    "models/orders.sql" --> "order_id"
    "models/orders.sql" --> "payment_method"
    "models/orders.sql" --> "total_amount"
    "models/orders.sql" --> "customer_id"
    "models/orders.sql" --> "order_date"
    "models/customers.sql" --> "customer_orders"
    "models/customers.sql" --> "customer_id"
    "models/customers.sql" --> "order_date"
    "models/customers.sql" --> "first_order"
    "models/customers.sql" --> "most_recent_order"
    "models/customers.sql" --> "order_id"
    "models/customers.sql" --> "number_of_orders"
    "models/customers.sql" --> "customer_payments"
    "models/customers.sql" --> "total_amount"
    "models/customers.sql" --> "first_name"
    "models/customers.sql" --> "last_name"
    "models/customers.sql" --> "customer_lifetime_value"
    "models/staging/stg_payments.sql" --> "payment_id"
    "models/staging/stg_payments.sql" --> "order_id"
    "models/staging/stg_payments.sql" --> "payment_method"
    "models/staging/stg_customers.sql" --> "customer_id"
    "models/staging/stg_customers.sql" --> "first_name"
    "models/staging/stg_customers.sql" --> "last_name"
    "models/staging/stg_orders.sql" --> "order_id"
    "models/staging/stg_orders.sql" --> "user_id"
    "models/staging/stg_orders.sql" --> "customer_id"
    "models/staging/stg_orders.sql" --> "order_date"
```

## 2. Critical Architectural Hubs (PageRank)

## 3. Architectural Debt & Risks

### 3.2 Dead Code Candidates
> [!NOTE]
> These modules have zero in-degree (no detected imports). Verify if they are entry points or unused.

- `dbt_project.yml`
- `models/orders.sql`
- `models/customers.sql`
- `models/schema.yml`
- `models/staging/stg_payments.sql`
- `models/staging/stg_customers.sql`
- `models/staging/schema.yml`
- `models/staging/stg_orders.sql`

## 4. Module Purpose Index
### `dbt_project.yml`
**Purpose:** The code defines the configuration for a dbt project named 'jaffle_shop', specifying paths for models, seeds, tests, analysis, and macros, as well as target directories and version requirements. It also sets the materialization strategy for models and staging tables, ensuring efficient data transformation and storage.
**Complexity:** 9.0 | **Velocity:** 0 changes/30d

### `models/orders.sql`
**Purpose:** This code aggregates payment data by order, breaking down the total amount by payment method (credit card, coupon, bank transfer, gift card) and calculating the overall total for each order. It then joins this payment information with order details to provide a comprehensive view of each order's payment breakdown and total amount.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `models/customers.sql`
**Purpose:** This code aggregates customer data to provide a comprehensive view of customer behavior and value, including their first and most recent order dates, total number of orders, and lifetime value. It serves as a foundation for customer analytics and segmentation, enabling businesses to understand customer purchasing patterns and identify high-value customers.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `models/schema.yml`
**Purpose:** This code defines the structure of two database tables, 'customers' and 'orders', to store and manage customer and order information for a business system. It ensures data integrity and relationships between tables, enabling efficient tracking of customer orders, order statuses, and payment methods.
**Complexity:** 6.5 | **Velocity:** 0 changes/30d

### `models/staging/stg_payments.sql`
**Purpose:** The code transforms raw payment data by converting the amount from cents to dollars and renaming columns for clarity, preparing it for further analysis or reporting.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `models/staging/stg_customers.sql`
**Purpose:** The code transforms raw customer data by selecting specific fields and renaming them for clarity and consistency. It serves to prepare customer information for downstream use in the system, ensuring data is structured and labeled appropriately for business processes.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `models/staging/schema.yml`
**Purpose:** This code defines data quality tests for staging tables in a data warehouse, ensuring data integrity and consistency for downstream analytics and reporting.
**Complexity:** 4.5 | **Velocity:** 0 changes/30d

### `models/staging/stg_orders.sql`
**Purpose:** The code transforms raw order data by renaming columns to more meaningful names and selecting specific fields for further processing or analysis.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

## 5. System Statistics
Total Modules: 25
Total Dependencies: 29
