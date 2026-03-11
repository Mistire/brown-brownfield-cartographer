# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-11 17:28

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
**Purpose:** None
**Complexity:** 9.0 | **Velocity:** 0 changes/30d

### `models/orders.sql`
**Purpose:** None
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
**Purpose:** None
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
**Purpose:** None
**Complexity:** 6.5 | **Velocity:** 0 changes/30d

### `models/staging/stg_payments.sql`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `models/staging/stg_customers.sql`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `models/staging/schema.yml`
**Purpose:** None
**Complexity:** 4.5 | **Velocity:** 0 changes/30d

### `models/staging/stg_orders.sql`
**Purpose:** None
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

## 5. System Statistics
Total Modules: 25
Total Dependencies: 29
