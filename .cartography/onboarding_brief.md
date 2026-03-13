# FDE Day-One Onboarding Brief

> [!NOTE]
> This document is generated to accelerate the first 72 hours of embedding.

## 1. The Five Day-One Answers
### Q1: What is the primary data ingestion path?
The ingestion path involves SQL files, specifically `targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql`.

### Q2: What are the 3-5 most critical output datasets/endpoints?
Critical outputs include files like `big`, `yaml`, and `struve_convergence.png`.

### Q3: What is the blast radius if the most critical module fails?
Blast radius spans across infrastructure files (e.g., Docker configurations, package lock files), ingestion files (SQL fixtures), transformation files (dbt models and schemas), and logic files (test snapshots).

### Q4: Where is the business logic concentrated vs. distributed?
Logic distribution is primarily in test snapshots under `targets/better-auth/packages/cli/test/__snapshots__/`, with additional logic in transformation files like dbt models and schemas.

### Q5: What has changed most frequently in the last 90 days?
Change hotspots are likely in infrastructure files (e.g., Docker and package configurations), transformation files (dbt models and schemas), and logic files (test snapshots), as these are frequently modified during development and testing.

## 2. High-Velocity Hotspots
- `targets/better-auth/pnpm-workspace.yaml` (0 changes/30d)
- `targets/better-auth/pnpm-lock.yaml` (0 changes/30d)
- `targets/better-auth/docker-compose.yml` (0 changes/30d)
- `targets/better-auth/e2e/smoke/test/fixtures/cloudflare/drizzle/0000_lively_paladin.sql` (0 changes/30d)
- `targets/better-auth/demo/nextjs/pnpm-workspace.yaml` (0 changes/30d)

## 3. Top Complexity Risks
- `targets/better-auth/pnpm-lock.yaml` (Complexity: 3405.5)
- `targets/better-auth/demo/expo/pnpm-lock.yaml` (Complexity: 906.0)
- `targets/better-auth/demo/nextjs/pnpm-lock.yaml` (Complexity: 550.0)
- `targets/better-auth/demo/electron/pnpm-lock.yaml` (Complexity: 528.5)
- `targets/better-auth/demo/oidc-client/pnpm-lock.yaml` (Complexity: 267.0)
