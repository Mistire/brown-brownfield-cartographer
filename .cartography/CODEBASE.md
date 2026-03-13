# CODEBASE.md: System Architecture Map

## 1. Architecture Overview
Generated on: 2026-03-14 00:26

### 1.1 System Map (Mermaid)
```mermaid
graph TD
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`account_id`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`provider_id`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`user_id`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`access_token`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`refresh_token`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`id_token`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`access_token_expires_at`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`refresh_token_expires_at`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`created_at`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`updated_at`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`public_key`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`private_key`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`expires_at`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`ip_address`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`user_agent`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`session_token_unique`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`sso_provider`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`oidc_config`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`saml_config`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`organization_id`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`sso_provider_provider_id_unique`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`email_verified`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`user_email_unique`"
    "targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql" --> "`verification_identifier_idx`"
    "targets/better-auth/packages/cli/test/__snapshots__/migrations.sql" --> ""verification_identifier_idx""
    "targets/jaffle_shop/models/orders.sql" --> "payment_methods"
    "targets/jaffle_shop/models/orders.sql" --> "order_payments"
    "targets/jaffle_shop/models/orders.sql" --> "order_id"
    "targets/jaffle_shop/models/orders.sql" --> "payment_method"
    "targets/jaffle_shop/models/orders.sql" --> "total_amount"
    "targets/jaffle_shop/models/orders.sql" --> "customer_id"
    "targets/jaffle_shop/models/orders.sql" --> "order_date"
    "targets/jaffle_shop/models/customers.sql" --> "customer_orders"
    "targets/jaffle_shop/models/customers.sql" --> "customer_id"
    "targets/jaffle_shop/models/customers.sql" --> "order_date"
    "targets/jaffle_shop/models/customers.sql" --> "first_order"
    "targets/jaffle_shop/models/customers.sql" --> "most_recent_order"
    "targets/jaffle_shop/models/customers.sql" --> "order_id"
    "targets/jaffle_shop/models/customers.sql" --> "number_of_orders"
    "targets/jaffle_shop/models/customers.sql" --> "customer_payments"
    "targets/jaffle_shop/models/customers.sql" --> "total_amount"
    "targets/jaffle_shop/models/customers.sql" --> "first_name"
    "targets/jaffle_shop/models/customers.sql" --> "last_name"
    "targets/jaffle_shop/models/customers.sql" --> "customer_lifetime_value"
    "targets/jaffle_shop/models/staging/stg_payments.sql" --> "payment_id"
    "targets/jaffle_shop/models/staging/stg_payments.sql" --> "order_id"
    "targets/jaffle_shop/models/staging/stg_payments.sql" --> "payment_method"
    "targets/jaffle_shop/models/staging/stg_customers.sql" --> "customer_id"
    "targets/jaffle_shop/models/staging/stg_customers.sql" --> "first_name"
    "targets/jaffle_shop/models/staging/stg_customers.sql" --> "last_name"
    "targets/jaffle_shop/models/staging/stg_orders.sql" --> "order_id"
    "targets/jaffle_shop/models/staging/stg_orders.sql" --> "user_id"
    "targets/jaffle_shop/models/staging/stg_orders.sql" --> "customer_id"
    "targets/jaffle_shop/models/staging/stg_orders.sql" --> "order_date"
```

## 2. Critical Architectural Hubs (PageRank)
- **`external_dependency`**: Centrality Score 0.0254
- **`external_dependency`**: Centrality Score 0.0231
- **`external_dependency`**: Centrality Score 0.0231

## 3. Architectural Debt & Risks

### 3.2 Dead Code Candidates
> [!NOTE]
> These modules have zero in-degree (no detected imports). Verify if they are entry points or unused.

- `targets/better-auth/pnpm-workspace.yaml`
- `targets/better-auth/pnpm-lock.yaml`
- `targets/better-auth/docker-compose.yml`
- `targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql`
- `targets/better-auth/demo/nextjs/pnpm-workspace.yaml`
- `targets/better-auth/demo/nextjs/pnpm-lock.yaml`
- `targets/better-auth/demo/stateless/pnpm-workspace.yaml`
- `targets/better-auth/demo/stateless/pnpm-lock.yaml`
- `targets/better-auth/demo/expo/pnpm-workspace.yaml`
- `targets/better-auth/demo/expo/pnpm-lock.yaml`
- `targets/better-auth/demo/oidc-client/pnpm-workspace.yaml`
- `targets/better-auth/demo/oidc-client/pnpm-lock.yaml`
- `targets/better-auth/demo/electron/pnpm-workspace.yaml`
- `targets/better-auth/demo/electron/electron-builder.yml`
- `targets/better-auth/demo/electron/pnpm-lock.yaml`
- `targets/better-auth/packages/cli/test/__snapshots__/migrations-uuid.sql`
- `targets/better-auth/packages/cli/test/__snapshots__/migrations.sql`
- `targets/jaffle_shop/dbt_project.yml`
- `targets/jaffle_shop/models/orders.sql`
- `targets/jaffle_shop/models/customers.sql`
- `targets/jaffle_shop/models/schema.yml`
- `targets/jaffle_shop/models/staging/stg_payments.sql`
- `targets/jaffle_shop/models/staging/stg_customers.sql`
- `targets/jaffle_shop/models/staging/schema.yml`
- `targets/jaffle_shop/models/staging/stg_orders.sql`

## 4. Module Purpose Index
### `targets/better-auth/pnpm-workspace.yaml`
**Purpose:** This configuration manages package dependencies and workspace settings for a software project, ensuring consistent versions and proper linking of packages across different environments.
**Complexity:** 14.5 | **Velocity:** 0 changes/30d

### `targets/better-auth/pnpm-lock.yaml`
**Purpose:** This code defines a package management configuration that specifies exact versions of dependencies and their relationships for different parts of a software project, ensuring consistent and reproducible builds across development environments.
**Complexity:** 3405.5 | **Velocity:** 0 changes/30d

### `targets/better-auth/docker-compose.yml`
**Purpose:** This code defines a Docker Compose configuration that sets up multiple database services (PostgreSQL, MySQL, MongoDB, Redis, and MSSQL) for testing different database integrations with an authentication system, each with health checks to ensure they are ready before use.
**Complexity:** 23.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql`
**Purpose:** This code defines the database schema for a user authentication and authorization system, including tables for user accounts, sessions, SSO providers, and verification processes. It establishes relationships between entities and ensures data integrity through foreign keys and unique constraints.
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

### `targets/better-auth/demo/nextjs/pnpm-workspace.yaml`
**Purpose:** The code specifies that only the 'sharp' dependency should be built, likely to optimize build processes by excluding unnecessary dependencies.
**Complexity:** 1.5 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/nextjs/pnpm-lock.yaml`
**Purpose:** This is a package lock file that manages dependencies for a React-based authentication system, ensuring consistent versions of UI components, authentication providers, and database libraries across the project.
**Complexity:** 550.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/stateless/pnpm-workspace.yaml`
**Purpose:** The code appears to be designed to process and analyze data for business insights, likely generating reports or dashboards to support decision-making.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/stateless/pnpm-lock.yaml`
**Purpose:** This code defines a package dependency configuration for a web application, specifying required libraries and their versions for proper functionality.
**Complexity:** 114.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/expo/pnpm-workspace.yaml`
**Purpose:** The code specifies that only the 'better-sqlite3' dependency should be built, likely to optimize the build process by excluding unnecessary dependencies.
**Complexity:** 1.5 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/expo/pnpm-lock.yaml`
**Purpose:** This code defines the dependency configuration for a React Native/Expo project, specifying which packages and versions are required for the application to function properly.
**Complexity:** 906.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/oidc-client/pnpm-workspace.yaml`
**Purpose:** The code appears to be designed to process and analyze data, likely for generating insights or reports that support business decision-making.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/oidc-client/pnpm-lock.yaml`
**Purpose:** This code defines the dependencies and development tools for a React-based web application, including UI components, authentication, and build tools.
**Complexity:** 267.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/electron/pnpm-workspace.yaml`
**Purpose:** The code specifies a list of dependencies that are built exclusively for a particular system, likely to ensure compatibility and streamline the build process for specific components like Electron and its installer.
**Complexity:** 1.5 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/electron/electron-builder.yml`
**Purpose:** This configuration defines the build settings for packaging an Electron application into distributable formats across multiple platforms (Windows, macOS, and Linux). It specifies which files to include/exclude, application metadata, installer options, and platform-specific settings to create professional installers and packages for end users.
**Complexity:** 17.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/demo/electron/pnpm-lock.yaml`
**Purpose:** This code defines the dependency configuration for an Electron application, specifying both production and development dependencies required to build and run the application. It establishes the project's package management structure, linking local packages and external libraries to ensure proper compilation and execution of the Electron-based software.
**Complexity:** 528.5 | **Velocity:** 0 changes/30d

### `targets/better-auth/packages/cli/test/__snapshots__/migrations-uuid.sql`
**Purpose:** This code establishes the foundational database schema for a user authentication and account management system, enabling secure user registration, session handling, and third-party account integration.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `targets/better-auth/packages/cli/test/__snapshots__/migrations.sql`
**Purpose:** This code establishes the database schema for a user authentication and session management system, including tables for users, sessions, accounts, and verification tokens. It enables secure user registration, login, and account linking with third-party providers while maintaining session state and verification processes.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/jaffle_shop/dbt_project.yml`
**Purpose:** This configuration file sets up the structure and behavior of a data transformation project, defining paths for models, seeds, tests, and other components, and specifying how data should be materialized in the database.
**Complexity:** 9.0 | **Velocity:** 0 changes/30d

### `targets/jaffle_shop/models/orders.sql`
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

### `targets/jaffle_shop/models/customers.sql`
**Purpose:** This code aggregates customer data to provide a comprehensive view of customer behavior and value, including their first and most recent order dates, total number of orders, and lifetime value. It serves as a foundation for customer analytics and business intelligence, enabling data-driven decisions to enhance customer relationships and optimize marketing strategies.
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

### `targets/jaffle_shop/models/schema.yml`
**Purpose:** This code defines the structure of a customer and order database, capturing essential information such as customer details, order history, and payment methods. It serves as a foundation for tracking customer interactions, order statuses, and financial transactions within the system.
**Complexity:** 6.5 | **Velocity:** 0 changes/30d

### `targets/jaffle_shop/models/staging/stg_payments.sql`
**Purpose:** The code transforms raw payment data by converting the amount from cents to dollars and renaming columns for clarity, preparing it for further analysis or reporting.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

### `targets/jaffle_shop/models/staging/stg_customers.sql`
**Purpose:** The code transforms raw customer data by selecting specific fields and renaming them for clarity, preparing it for further analysis or reporting.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `targets/jaffle_shop/models/staging/schema.yml`
**Purpose:** The code defines data quality tests for staging tables to ensure data integrity in a business system, such as verifying unique and non-null customer IDs, order IDs, and payment IDs, and validating accepted values for order statuses and payment methods.
**Complexity:** 4.5 | **Velocity:** 0 changes/30d

### `targets/jaffle_shop/models/staging/stg_orders.sql`
**Purpose:** The code transforms raw order data by selecting specific fields and renaming them for clarity, such as changing 'id' to 'order_id' and 'user_id' to 'customer_id'. This ensures the data is structured in a way that aligns with business reporting and analysis needs.
**Complexity:** 1.0 | **Velocity:** 0 changes/30d

### `external_dependency`
**Purpose:** No purpose generated.
**Complexity:** 0.0 | **Velocity:** 0 changes/30d

## 5. System Statistics
Total Modules: 67
Total Dependencies: 54
