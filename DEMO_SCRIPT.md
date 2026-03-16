# DEMO SCRIPT — 6-Minute Mastery Video
## Brownfield Cartographer (UI Demo with jaffle_shop)

**Total Time: ~5:45** (15s buffer)  
**Target:** `https://github.com/dbt-labs/jaffle_shop`  
**Interface:** Dashboard UI at `http://localhost:3000`

---

## PRE-RECORDING CHECKLIST

```bash
# 1. Delete cached jaffle_shop analysis for a fresh cold start
rm -rf .cartography/jaffle_shop

# 2. Clean Docker and restart
docker-compose down --remove-orphans
docker rm -f $(docker ps -aq) 2>/dev/null
docker-compose up --build -d

# 3. Verify API is running
curl http://localhost:8000/projects   # Should return []
```

- [ ] Dashboard open in browser
- [ ] Browser zoomed to ~110% for screen readability
- [ ] `RECONNAISSANCE.md` open in a VS Code tab (for Step 4 verification)
- [ ] Fresh ChatGPT or Claude tab ready (for Step 5)
- [ ] Self-analysis of your own brownfield-cartographer already cached (for Step 6)
- [ ] Screen recorder ON, mic tested

---

## STEP 1 — Cold Start (0:00 → 1:15) — 20 pts

### 🎙️ INTRO (5s):
> "This is the Brownfield Cartographer — a multi-agent system that maps unfamiliar codebases for rapid FDE onboarding. I'll run a live cold start against the dbt jaffle_shop, a data engineering project with SQL models, YAML configs, and CSV seed files."

### 👆 ACTION:
1. In the Dashboard, paste into the analysis input:
   ```
   https://github.com/dbt-labs/jaffle_shop
   ```
2. Click **Begin Analysis**
3. The Build Console should stream agent activity

### 🎙️ NARRATE WHILE IT RUNS:
> "The system runs four agents. The **Surveyor** is building the module dependency graph using tree-sitter AST parsing — it's computing complexity scores and git change velocity for every file."
>
> "Now the **Hydrologist** is tracing data lineage — it's using sqlglot to parse SQL table references and following dbt `ref()` calls to map data flows from source CSVs to final reporting models."
>
> "The **Semanticist** is analyzing each module with LLM model tiering — it uses GPT-4o for complex logic files and 4o-mini for simpler configs — generating purpose statements and detecting documentation drift."

### 👆 WHEN COMPLETE:
1. Click the **CODEBASE.md** / Documentation tab
2. Scroll slowly — pause on the **Mermaid architecture diagram** and the **Data Sources & Sinks** section

### 🎙️ SAY:
> "Analysis complete. Here's the generated CODEBASE.md — a living architecture map. You can see the dependency diagram, the critical path hubs identified by PageRank, and the system's identified data sources — raw CSVs — and sinks — the final `customers` and `orders` models. This is what an FDE reads on Day Zero, before ever meeting the client team."

**⏱️ Target: 1:15**

---

## STEP 2 — Lineage Query (1:15 → 2:15) — 15 pts

### 🎙️ SAY:
> "As an FDE, I need to understand where the customer lifetime value comes from. Let me trace the upstream lineage."

### 👆 ACTION:
1. Switch to the **Navigator Chat** panel
2. Type:
   ```
   Trace the upstream lineage of the customers model
   ```
3. Wait for the response

### 🎙️ NARRATE THE RESPONSE:
> "The Navigator traced the full upstream chain. The `customers` model depends on three staging models — `stg_customers`, `stg_orders`, and `stg_payments` — which in turn source from the raw CSV seed files: `raw_customers.csv`, `raw_orders.csv`, and `raw_payments.csv`."
>
> "Each dependency includes a **file path**, the **inference type — Static Analysis**, and a **confidence score of 1.0**, meaning this was determined deterministically from the code, not estimated by an LLM."
>
> "For an FDE, this means if there's a data quality issue in the customer LTV number, I can trace it back to the exact source file in seconds — I don't need to grep through the codebase manually."

**⏱️ Target: 2:15**

---

## STEP 3 — Blast Radius (2:15 → 3:15) — 15 pts

### 🎙️ SAY:
> "Before proposing any refactor, an FDE needs to know the blast radius. What breaks if I change the staging orders model?"

### 👆 ACTION:
1. In the **Navigator Chat**, type:
   ```
   What is the blast radius of stg_orders?
   ```
2. Wait for the response

### 🎙️ NARRATE:
> "The blast radius of `stg_orders` is critical — if it fails, both `orders.sql` and `customers.sql` break. That's **100% of the final output models**."
>
> "The system found this through **multi-hop graph traversal** — `stg_orders` feeds `orders`, which feeds `customers` through a transitive dependency for order counts and LTV calculations. This isn't just the immediate imports — it's the full downstream cascade."
>
> "Without this analysis, an FDE might assume changing the staging model is low-risk. The Cartographer shows it's actually the **highest-risk change** in this entire codebase."

**⏱️ Target: 3:15**

---

## STEP 4 — Day-One Brief Verification (3:15 → 4:15) — 15 pts

### 🎙️ SAY:
> "Now the Onboarding Brief — the five Day-One answers every FDE needs. I'll show it and then verify two answers against the actual source code."

### 👆 ACTION:
1. Switch to the **Onboarding Brief** tab
2. Let the viewer see the five answers on screen — pause 3 seconds

### 🎙️ SAY:
> "These are codebase-specific, not generic templates. Let me verify."

### LIVE VERIFICATION #1:
> "The brief says the primary ingestion path is CSV seed files. Let me verify..."

3. **Switch to VS Code** or terminal:
   ```bash
   ls targets/jaffle_shop/seeds/
   ```
   *Shows: `raw_customers.csv`, `raw_orders.csv`, `raw_payments.csv`*

> "Confirmed — three CSV seed files, exactly as the system reported."

### LIVE VERIFICATION #2:
> "The brief says business logic is concentrated in `customers.sql` with LTV calculations. Let me check..."

4. Open the file:
   ```bash
   cat targets/jaffle_shop/models/customers.sql
   ```
   *Point to the `sum(amount)` and join logic*

> "Confirmed — lines 23 through 35 show the LTV aggregation and the multi-CTE join structure. The system's purpose statement is grounded in actual code evidence, file path and line number."

**⏱️ Target: 4:15**

---

## STEP 5 — Living Context Injection (4:15 → 5:00) — 10 pts

### 🎙️ SAY:
> "Does this generated context actually make AI assistants smarter? Let me demonstrate."

### 👆 ACTION:
1. **Open ChatGPT/Claude** — fresh session, NO context
2. Ask:
   ```
   How does jaffle_shop calculate customer lifetime value?
   ```
3. Show the vague answer (it'll say something generic about "typically" or "usually")

4. **New chat** — paste the CODEBASE.md content first, then ask the same question
5. Show the specific answer (it should name `customers.sql`, the CTEs, `stg_payments`)

### 🎙️ SAY:
> "Without context, the AI guesses generically. With CODEBASE.md injected, it correctly identifies that LTV is calculated in `customers.sql` by summing the `amount` field from `stg_payments`, which converts cents to dollars at line 9."
>
> "For an FDE, you paste one file and your AI assistant becomes a **codebase-aware pair programmer** that understands the client's actual architecture."

**⏱️ Target: 5:00**

---

## STEP 6 — Self-Audit (5:00 → 5:45) — 10 pts

### 🎙️ SAY:
> "Finally, the most honest test — running the Cartographer against my own code."

### 👆 ACTION:
1. In the Dashboard, switch to the **brown-brownfield-cartographer** project (pre-analyzed)
2. Open its **CODEBASE.md**
3. Find and highlight a real discrepancy

### 🎙️ PICK ONE OF THESE (whichever is real in your output):

**Option A — Dead Code False Positive:**
> "The system flagged `semantic_index.py` as a dead code candidate because nothing in the project statically imports it. But it's loaded dynamically by the Navigator agent at runtime via lazy imports. This shows a real limitation — static analysis can't see `importlib` or lazy loading patterns. The system is honest about this: it marks the inference type as 'Static Analysis,' which signals the FDE to verify before deleting."

**Option B — Documentation Drift:**
> "The system detected documentation drift in my `orchestrator.py` — the docstring says it runs agents sequentially, but the implementation now uses `asyncio.to_thread` for parallel execution. My docs fell behind my code. The Cartographer caught something I missed in my own project."

**Option C — Purpose Statement Mismatch:**
> "My README describes the Archivist as 'generating CODEBASE.md.' But the system's purpose statement says it 'synthesizes multi-source knowledge graph data into executive-level architectural reports.' The system's description is more accurate than what I originally wrote."

### 🎙️ CLOSE:
> "This self-audit shows both the value and the limitations. The system isn't perfect — no static tool can capture runtime behavior. But for an FDE walking into an unfamiliar codebase, the Brownfield Cartographer compresses **weeks of manual exploration into minutes of structured, cited, verifiable analysis.** Thank you."

**⏱️ Target: 5:45. STOP RECORDING.**

---

## TIMING CHEAT SHEET

| Step | Start | End | Seconds | Points |
|---|---|---|---|---|
| 1. Cold Start | 0:00 | 1:15 | 75 | 20 |
| 2. Lineage Query | 1:15 | 2:15 | 60 | 15 |
| 3. Blast Radius | 2:15 | 3:15 | 60 | 15 |
| 4. Day-One Brief | 3:15 | 4:15 | 60 | 15 |
| 5. Context Injection | 4:15 | 5:00 | 45 | 10 |
| 6. Self-Audit | 5:00 | 5:45 | 45 | 10 |
| **Total** | | | **5:45** | **85** + 15 (delivery) = **100** |

## IF THINGS GO WRONG

| Problem | Fix |
|---|---|
| Analysis takes too long | Say: "Let me show the pre-generated output" → show cached artifacts |
| Navigator chat errors | Say: "Let me query directly" → switch to terminal, run Python one-liner |
| Docker containers down | Run locally: `./.venv/bin/python -m src.cli analyze targets/jaffle_shop` |
| Can't find discrepancy for Step 6 | Use the dead code false positive — `semantic_index.py` is almost certainly flagged |
