# Bugfix Requirements Document

## Introduction

The Brownfield Cartographer pipeline contains multiple bugs spanning crash-on-init failures,
silent LLM misconfiguration, broken semantic search, O(n²) performance regressions, async/sync
mismatches, missing cost guards, absent error recovery, and security gaps in the WebSocket API.
These issues collectively prevent reliable end-to-end pipeline execution and expose the service
to denial-of-service attacks. This document captures the defective behaviors, the correct
behaviors that must replace them, and the existing behaviors that must be preserved.

---

## Bug Analysis

### Current Behavior (Defect)

**Bug 1 — Navigator crashes on init (Hydrologist wrong argument)**

1.1 WHEN the Navigator is instantiated with a repo path THEN the system passes `self.project_name`
    (a bare directory name) to `Hydrologist()` instead of `self.repo_path`, causing Hydrologist
    to walk a non-existent path and crash on initialization.

**Bug 2 — Navigator system message silently ignored**

1.2 WHEN the Navigator agent node runs THEN the system injects the system prompt as a plain
    `AIMessage` wrapping a dict instead of a `SystemMessage`, so the LLM never receives
    architectural instructions and produces uncited, low-quality responses.

**Bug 3 — Embeddings return zero vectors via OpenRouter**

1.3 WHEN `Semanticist.get_embeddings()` is called THEN the system requests `text-embedding-3-small`
    through the OpenRouter base URL, which does not expose that OpenAI-only model, causing the
    call to fail and fall back to a zero vector of length 1536, making all semantic similarity
    scores identical and semantic search non-functional.

**Bug 4 — Hydrologist O(n²) metadata enrichment**

1.4 WHEN the Hydrologist processes a repository with N files THEN the system calls
    `_enrich_lineage_metadata()` inside the per-file loop, re-labelling every node in the
    growing graph after each file, resulting in O(n²) graph traversals that make large
    repositories impractically slow.

**Bug 5 — Orchestrator async/sync mismatch with Semanticist**

1.5 WHEN the Orchestrator calls `Semanticist.cluster_into_domains()` or
    `Semanticist.answer_day_one_questions()` outside of `asyncio.to_thread` THEN the system
    awaits coroutines that may block the event loop or, if called from a sync context, raises
    a `RuntimeError`, causing the pipeline to hang or crash.

**Bug 6 — Token budget exhaustion flag never checked before LLM calls**

1.6 WHEN `ContextWindowBudget.is_exhausted` is set to `True` THEN the system continues to
    invoke the LLM in `detect_drift()`, `answer_day_one_questions()`, and
    `cluster_into_domains()` because those methods do not check the flag, incurring unbounded
    API cost beyond the configured token limit.

**Bug 7 — No error recovery when Surveyor fails**

1.7 WHEN the Surveyor stage raises an unhandled exception THEN the system allows the
    Hydrologist to run against an empty module graph, producing a corrupted or empty
    `lineage_graph.json` artifact and a misleading `checkpoint` status file that marks
    the pipeline as successful.

**Bug 8 — Navigator tools have inconsistent async/sync signatures**

1.8 WHEN the LangGraph `ToolNode` dispatches `find_implementation` (declared `async`) alongside
    `trace_lineage`, `blast_radius`, and `explain_module` (declared sync) THEN the system
    executes the async tool without awaiting it in some execution paths, producing unawaited
    coroutine warnings and unreliable tool results.

**Bug 9 — SQL lineage regex only handles single-quoted dbt refs**

1.9 WHEN a dbt SQL file uses double-quoted ref syntax `{{ ref("model_name") }}` or nested
    Jinja expressions THEN the system's `extract_dbt_refs` regex `['\"](.+?)['\"]` fails to
    match, silently dropping those upstream dependencies from the lineage graph.

**Bug 10 — WebSocket endpoint has no timeout or max message size**

1.10 WHEN a client connects to `/ws/analysis` and sends an arbitrarily large message or holds
     the connection open indefinitely THEN the system accepts and buffers the message without
     limit and never closes idle connections, creating a denial-of-service vector.

**Bug 11 — No validation that OPENROUTER_API_KEY is set before Semanticist runs**

1.11 WHEN the Orchestrator instantiates `Semanticist` without `OPENROUTER_API_KEY` set in the
     environment THEN the system prints a warning but proceeds to call `cluster_into_domains()`
     and `answer_day_one_questions()` on the disabled instance, returning placeholder strings
     that are silently written into the final artifacts as if they were real analysis.

**Bug 12 — LLM model name is hardcoded with no config override**

1.12 WHEN the Navigator is instantiated THEN the system hardcodes `"openai/gpt-4o"` as the
     model name with no environment variable fallback, preventing operators from switching to
     a cheaper or alternative model without modifying source code.

**Bug 13 — Checkpoint status file has no corruption validation**

1.13 WHEN the Orchestrator resumes from a previous run and reads `.cartography_status.json`
     THEN the system loads the file with `json.load()` without catching `json.JSONDecodeError`
     or validating the expected keys, so a truncated or corrupted status file causes an
     unhandled exception that aborts the pipeline before any work is done.

---

### Expected Behavior (Correct)

**Bug 1 — Navigator init**

2.1 WHEN the Navigator is instantiated with a repo path THEN the system SHALL pass
    `self.repo_path` to `Hydrologist()` so that Hydrologist receives a valid filesystem path
    and initializes without error.

**Bug 2 — Navigator system message**

2.2 WHEN the Navigator agent node runs THEN the system SHALL inject the system prompt as a
    `SystemMessage` instance so that the LLM receives architectural instructions and produces
    cited, high-quality responses.

**Bug 3 — Embeddings**

2.3 WHEN `Semanticist.get_embeddings()` is called with OpenRouter as the API base THEN the
    system SHALL use a model that is available through OpenRouter (e.g. a configurable
    `EMBEDDING_MODEL` env var defaulting to a supported model such as
    `"openai/text-embedding-3-small"` via the OpenRouter embeddings endpoint, or a local
    fallback) so that embeddings contain meaningful vectors and semantic search returns
    relevant results.

**Bug 4 — Hydrologist enrichment**

2.4 WHEN the Hydrologist finishes processing all files THEN the system SHALL call
    `_enrich_lineage_metadata()` exactly once after the loop completes, reducing complexity
    from O(n²) to O(n) and making large-repository scans complete in reasonable time.

**Bug 5 — Orchestrator async/sync**

2.5 WHEN the Orchestrator calls `Semanticist.cluster_into_domains()` and
    `Semanticist.answer_day_one_questions()` THEN the system SHALL await those coroutines
    directly (since the Orchestrator pipeline is already async), ensuring the event loop is
    not blocked and no `RuntimeError` is raised.

**Bug 6 — Token budget guard**

2.6 WHEN `ContextWindowBudget.is_exhausted` is `True` THEN the system SHALL return early
    with a safe default value from `detect_drift()`, `answer_day_one_questions()`, and
    `cluster_into_domains()` without making any further LLM API calls.

**Bug 7 — Surveyor error recovery**

2.7 WHEN the Surveyor stage raises an exception THEN the system SHALL catch the error, log it
    via `_log`, broadcast the failure over the progress callback, and abort the pipeline
    before running the Hydrologist, preventing corrupted artifacts from being written.

**Bug 8 — Navigator tool signatures**

2.8 WHEN the Navigator registers tools with LangGraph THEN the system SHALL declare all four
    tools with consistent signatures (all async or all sync, matching the ToolNode execution
    model) so that every tool is dispatched and awaited correctly.

**Bug 9 — SQL lineage regex**

2.9 WHEN a dbt SQL file uses double-quoted ref syntax `{{ ref("model_name") }}` THEN the
    system SHALL extract `model_name` as an upstream dependency, and the regex SHALL handle
    both single and double quote variants so that no upstream dependency is silently dropped.

**Bug 10 — WebSocket DoS protection**

2.10 WHEN a client connects to `/ws/analysis` THEN the system SHALL enforce a maximum
     inbound message size and close connections that have been idle beyond a configurable
     timeout, preventing resource exhaustion from malicious or stale clients.

**Bug 11 — API key validation**

2.11 WHEN the Orchestrator starts the semanticist stage and `OPENROUTER_API_KEY` is not set
     THEN the system SHALL skip all LLM-dependent steps (purpose generation, drift detection,
     domain clustering, day-one answers) and write clearly-marked placeholder values into
     artifacts, rather than silently writing degraded output as if it were real analysis.

**Bug 12 — Configurable LLM model**

2.12 WHEN the Navigator is instantiated THEN the system SHALL read the model name from the
     `NAVIGATOR_MODEL` environment variable, falling back to `"openai/gpt-4o"` if unset, so
     that operators can override the model without modifying source code.

**Bug 13 — Checkpoint corruption handling**

2.13 WHEN the Orchestrator reads `.cartography_status.json` THEN the system SHALL wrap the
     read in a try/except for `json.JSONDecodeError` and validate that the expected boolean
     keys are present, falling back to an empty status dict (triggering a full re-run) if the
     file is missing, empty, or malformed.

---

### Unchanged Behavior (Regression Prevention)

3.1 WHEN the Navigator is instantiated with a valid repo path and a pre-built knowledge graph
    THEN the system SHALL CONTINUE TO load the graph, initialize all agents, bind tools to the
    LLM, and compile the LangGraph workflow without error.

3.2 WHEN a user submits a query to the Navigator THEN the system SHALL CONTINUE TO invoke the
    LangGraph agent loop, call the appropriate tools, and return a cited natural-language
    answer.

3.3 WHEN the Hydrologist processes a repository containing Python, SQL, and YAML files THEN
    the system SHALL CONTINUE TO build a lineage graph with correct source/sink labels and
    edge metadata.

3.4 WHEN `Semanticist.generate_purpose()` is called with a valid API key and a non-exhausted
    budget THEN the system SHALL CONTINUE TO invoke the LLM, record token usage, and return a
    purpose string with a confidence score.

3.5 WHEN the Orchestrator runs the full pipeline on a repository that has not been analyzed
    before THEN the system SHALL CONTINUE TO execute Surveyor → Hydrologist → Semanticist →
    Archivist in sequence and write all artifacts to the output directory.

3.6 WHEN the Orchestrator detects a previous successful run via the status file THEN the
    system SHALL CONTINUE TO skip completed stages and resume from the first incomplete stage.

3.7 WHEN `SQLLineageAnalyzer.extract_lineage()` processes a SQL file using single-quoted dbt
    ref syntax `{{ ref('model_name') }}` THEN the system SHALL CONTINUE TO extract
    `model_name` as an upstream dependency.

3.8 WHEN the FastAPI `/analyze` endpoint receives a valid repository path THEN the system
    SHALL CONTINUE TO start the analysis pipeline as a background task and return an
    immediate acknowledgement response.

3.9 WHEN the FastAPI `/query` endpoint receives a valid project name and query string THEN
    the system SHALL CONTINUE TO route the query to the Navigator and return the answer.

3.10 WHEN `ContextWindowBudget.record()` is called after an LLM response THEN the system
     SHALL CONTINUE TO accumulate token counts, compute cost, and set `is_exhausted` when
     the token limit is exceeded.
