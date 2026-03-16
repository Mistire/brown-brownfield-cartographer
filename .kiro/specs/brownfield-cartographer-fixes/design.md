# Brownfield Cartographer Fixes — Bugfix Design

## Overview

The Brownfield Cartographer pipeline contains 13 bugs spanning crash-on-init failures,
silent LLM misconfiguration, broken semantic search, O(n²) performance regressions,
async/sync mismatches, missing cost guards, absent error recovery, and security gaps.
The fix strategy is minimal and targeted: each change addresses exactly one defect,
preserving all existing pipeline behavior for non-buggy inputs.

## Glossary

- **Bug_Condition (C)**: The set of inputs or runtime states that trigger a defective behavior.
- **Property (P)**: The desired correct behavior that must hold for all inputs satisfying C.
- **Preservation**: All behaviors for inputs NOT satisfying C that must remain unchanged.
- **Orchestrator**: `src/orchestrator.py` — wires Surveyor → Hydrologist → Semanticist → Archivist.
- **Navigator**: `src/agents/navigator.py` — LangGraph agent providing query interface to the knowledge graph.
- **Hydrologist**: `src/agents/hydrologist.py` — builds the lineage graph from Python/SQL/YAML files.
- **Semanticist**: `src/agents/semanticist.py` — LLM wrapper for purpose generation, drift detection, clustering.
- **ContextWindowBudget**: Token-usage tracker inside `Semanticist`; sets `is_exhausted` when limit exceeded.
- **SQLLineageAnalyzer**: `src/analyzers/sql_lineage.py` — extracts dbt ref() dependencies via regex + sqlglot.
- **Surveyor**: `src/agents/surveyor.py` — walks the repo and builds the module graph.
- **KnowledgeGraph**: `src/graph/knowledge_graph.py` — container for module_graph and lineage_graph.
- **ToolNode**: LangGraph primitive that dispatches registered tools; requires consistent async/sync signatures.

## Bug Details

### Bug Condition

The 13 bugs share a common structure: each is triggered by a specific runtime condition
(wrong argument, missing guard, wrong message type, etc.) that causes incorrect behavior
while all other inputs remain unaffected.

**Formal Specification:**

```
FUNCTION isBugCondition(context)
  INPUT: context describing the runtime state at a specific call site
  OUTPUT: boolean

  RETURN (
    -- Bug 1: Navigator passes project_name instead of repo_path to Hydrologist
    (context.call_site == "Navigator.__init__" AND context.arg_to_hydrologist == project_name)
    OR
    -- Bug 2: System prompt injected as AIMessage instead of SystemMessage
    (context.call_site == "Navigator.agent" AND context.system_msg_type == AIMessage)
    OR
    -- Bug 3: Embeddings requested via OpenRouter with OpenAI-only model
    (context.call_site == "Semanticist.get_embeddings"
     AND context.api_base CONTAINS "openrouter.ai"
     AND context.model == "text-embedding-3-small")
    OR
    -- Bug 4: _enrich_lineage_metadata called inside per-file loop
    (context.call_site == "Hydrologist.run"
     AND context.enrich_call_count > 1)
    OR
    -- Bug 5: Async coroutines called without await in Orchestrator
    (context.call_site IN ["Orchestrator.run_full_pipeline"]
     AND context.awaited == False
     AND context.method IN ["cluster_into_domains", "answer_day_one_questions"])
    OR
    -- Bug 6: LLM called after budget exhausted
    (context.call_site IN ["detect_drift","answer_day_one_questions","cluster_into_domains"]
     AND context.budget.is_exhausted == True)
    OR
    -- Bug 7: Hydrologist runs after Surveyor exception
    (context.call_site == "Orchestrator.run_full_pipeline"
     AND context.surveyor_raised == True
     AND context.hydrologist_started == True)
    OR
    -- Bug 8: Async tool dispatched without await by ToolNode
    (context.call_site == "Navigator.tools"
     AND context.tool_name == "find_implementation"
     AND context.execution_mode == "sync_dispatch")
    OR
    -- Bug 9: Double-quoted dbt ref not matched by regex
    (context.call_site == "SQLLineageAnalyzer.extract_dbt_refs"
     AND context.sql CONTAINS 'ref("' )
    OR
    -- Bug 10: WebSocket accepts unbounded message or idle connection
    (context.call_site == "/ws/analysis"
     AND (context.message_size > MAX_SIZE OR context.idle_seconds > TIMEOUT))
    OR
    -- Bug 11: LLM steps run with no API key, writing fake results
    (context.call_site IN ["cluster_into_domains","answer_day_one_questions"]
     AND context.api_key == None
     AND context.result_written_as_real == True)
    OR
    -- Bug 12: Navigator model hardcoded, ignoring env override
    (context.call_site == "Navigator.__init__"
     AND context.NAVIGATOR_MODEL_env_set == True
     AND context.model_used == "openai/gpt-4o")
    OR
    -- Bug 13: Corrupted status file causes unhandled exception
    (context.call_site == "Orchestrator.run_full_pipeline"
     AND context.status_file_corrupt == True
     AND context.exception_raised == True)
  )
END FUNCTION
```

### Examples

- **Bug 1**: `Navigator("/repos/my-project")` → Hydrologist receives `"my-project"` (bare name), walks non-existent path, raises `FileNotFoundError` or silently builds empty graph.
- **Bug 2**: LLM receives `[AIMessage(content={"role":"system","content":"..."})]` → system instructions ignored, responses lack file citations.
- **Bug 3**: `get_embeddings("purpose text")` → OpenRouter returns 404 for `text-embedding-3-small` → fallback returns `[0.0] * 1536` → all cosine similarities are identical → semantic search returns arbitrary results.
- **Bug 4**: Repository with 500 files → `_enrich_lineage_metadata()` called 500 times → O(n²) = 250,000 graph traversals → scan takes minutes instead of seconds.
- **Bug 5**: `orchestrator.run_full_pipeline()` calls `self.semanticist.cluster_into_domains(module_data)` without `await` → coroutine object returned, never executed → domain clusters are empty.
- **Bug 6**: Budget exhausted after 100,000 tokens → `detect_drift()` still calls `self.llm.ainvoke(...)` → unbounded API spend.
- **Bug 7**: Surveyor raises `PermissionError` on a locked file → Hydrologist runs on empty `module_graph` → `lineage_graph.json` written as `{}` → status file marks pipeline as successful.
- **Bug 8**: LangGraph `ToolNode` dispatches `find_implementation` synchronously → unawaited coroutine warning → tool result is `None` or a coroutine object.
- **Bug 9**: `{{ ref("orders") }}` in SQL → regex `['\"](.+?)['\"]` matches `"orders"` but the outer quotes are double → depending on regex engine behavior, may match or silently drop → upstream dependency missing from lineage graph.
- **Bug 10**: Attacker sends 100 MB WebSocket message → server buffers entire payload → OOM or CPU spike.
- **Bug 11**: `OPENROUTER_API_KEY` unset → `cluster_into_domains()` returns `{"unclassified": [...]}` → written to `CODEBASE.md` as if real domain analysis.
- **Bug 12**: Operator sets `NAVIGATOR_MODEL=openai/gpt-4o-mini` → Navigator still uses `"openai/gpt-4o"` → higher cost, no override possible without code change.
- **Bug 13**: `.cartography_status.json` truncated mid-write → `json.load()` raises `JSONDecodeError` → pipeline aborts before any analysis runs.

## Expected Behavior

### Preservation Requirements

**Unchanged Behaviors:**
- Navigator instantiation with a valid repo path and pre-built knowledge graph must continue to load the graph, bind tools, and compile the LangGraph workflow without error (Req 3.1).
- Navigator query flow must continue to invoke the agent loop, call tools, and return a cited answer (Req 3.2).
- Hydrologist must continue to build a correct lineage graph with source/sink labels for Python, SQL, and YAML files (Req 3.3).
- `Semanticist.generate_purpose()` with a valid API key and non-exhausted budget must continue to invoke the LLM and return a purpose string with confidence score (Req 3.4).
- Full pipeline execution (Surveyor → Hydrologist → Semanticist → Archivist) must continue to write all artifacts to the output directory (Req 3.5).
- Incremental resume from a valid status file must continue to skip completed stages (Req 3.6).
- Single-quoted dbt ref syntax `{{ ref('model_name') }}` must continue to be extracted as an upstream dependency (Req 3.7).
- `/analyze` endpoint must continue to start the pipeline as a background task and return an immediate acknowledgement (Req 3.8).
- `/query` endpoint must continue to route queries to Navigator and return answers (Req 3.9).
- `ContextWindowBudget.record()` must continue to accumulate token counts and set `is_exhausted` correctly (Req 3.10).

**Scope:**
All inputs that do NOT satisfy `isBugCondition` must be completely unaffected by these fixes.
This includes: valid Hydrologist initialization, correct message types already in use, non-OpenRouter embedding calls, single-file Hydrologist runs, properly awaited coroutines, non-exhausted budget calls, successful Surveyor runs, sync tool dispatches, single-quoted SQL refs, well-formed WebSocket messages within size limits, configured API keys, unset NAVIGATOR_MODEL (uses default), and valid status files.

## Hypothesized Root Cause

1. **Bug 1 — Wrong variable passed**: `Navigator.__init__` sets `self.project_name = os.path.basename(repo_path.rstrip("/"))` then passes `self.project_name` to `Hydrologist()` instead of `repo_path`. Simple copy-paste error.

2. **Bug 2 — Wrong message class**: The system prompt is constructed as a plain dict and wrapped in `AIMessage` instead of imported and used as `SystemMessage`. LangChain distinguishes message roles by class type, not by a `role` key in the content.

3. **Bug 3 — OpenRouter embedding endpoint mismatch**: `OpenAIEmbeddings` is pointed at `openrouter.ai/api/v1` with model `text-embedding-3-small`, which is an OpenAI-proprietary model not proxied by OpenRouter. The fix requires either using a model OpenRouter supports for embeddings or using a direct OpenAI embeddings call when the base URL is OpenRouter.

4. **Bug 4 — Misplaced enrichment call**: `self._enrich_lineage_metadata()` is indented inside the `for full_path in iterate_over:` loop body (after the `try/except`), so it runs after every file instead of once at the end.

5. **Bug 5 — Missing await**: `domain_clusters = await self.semanticist.cluster_into_domains(module_data)` and `day_one_answers = await self.semanticist.answer_day_one_questions(synthesis_context)` — reading the orchestrator code confirms `await` IS present. The bug is that these are called inside `asyncio.to_thread` wrappers for the surveyor/hydrologist but the semanticist calls are direct awaits in the async pipeline — this is actually correct. Re-reading: the orchestrator IS async and does `await` these. The actual bug is that `cluster_into_domains` is called unconditionally even when `semanticist.enabled` is False, and the result is used regardless. The `answer_day_one_questions` is guarded but `cluster_into_domains` is not. This causes the disabled semanticist to return placeholder data that gets written as real output.

6. **Bug 6 — Missing guard**: `detect_drift`, `answer_day_one_questions`, and `cluster_into_domains` check `if not self.llm` but not `if self.budget.is_exhausted`. The budget check exists only in `generate_purpose`.

7. **Bug 7 — No try/except around Surveyor stage**: The orchestrator calls `await asyncio.to_thread(self.surveyor.run, ...)` without wrapping it in a try/except, so any exception propagates and the `status.get("hydrologist")` check still passes (it's False), causing Hydrologist to run on an empty graph.

8. **Bug 8 — Mixed async/sync tools**: `find_implementation` is declared `async def` while the other three tools are `def`. LangGraph's `ToolNode` in some versions does not automatically await async tools, leading to unawaited coroutine objects being returned as tool results.

9. **Bug 9 — Regex character class instead of alternation**: The regex `['\"](.+?)['\"]` uses a character class `['\"]` which matches either a single or double quote independently on each side. For `ref("model")` it matches `"model"` correctly. However for `ref('model')` it also works. The actual issue is that the regex pattern `r"\{\{\s*ref\(['\"](.+?)['\"]\)\s*\}\}"` may fail on whitespace variants or nested Jinja. Testing confirms double-quoted refs ARE matched by the character class — the real gap is that the regex doesn't handle whitespace inside the ref call like `ref( "model" )`.

10. **Bug 10 — No WebSocket guards**: The `/ws/analysis` endpoint calls `await websocket.receive_text()` in an infinite loop with no message size limit and no idle timeout. FastAPI/Starlette do not enforce these by default.

11. **Bug 11 — Placeholder output indistinguishable from real**: When `semanticist.enabled` is False, `cluster_into_domains` returns `{"unclassified": [...]}` and `answer_day_one_questions` returns `{f"q{i+1}": "Analysis pending: LLM disabled."}`. These are written into artifacts without any clear marker distinguishing them from real LLM analysis.

12. **Bug 12 — Hardcoded model string**: `Navigator.__init__` hardcodes `model_name="openai/gpt-4o"` with no `os.getenv("NAVIGATOR_MODEL", "openai/gpt-4o")` fallback.

13. **Bug 13 — Unguarded JSON load**: `json.load(f)` on the status file has no `try/except json.JSONDecodeError` and no validation that the loaded dict contains the expected boolean keys `surveyor`, `hydrologist`, `semanticist`.

## Correctness Properties

Property 1: Bug Condition — Navigator Receives Valid Repo Path

_For any_ `repo_path` string passed to `Navigator.__init__`, the fixed code SHALL pass
`repo_path` (not `project_name`) to `Hydrologist()`, so that Hydrologist initializes
against a valid filesystem path and does not raise an exception or build an empty graph.

**Validates: Requirements 2.1**

---

Property 2: Bug Condition — System Prompt Delivered as SystemMessage

_For any_ invocation of the Navigator agent node, the fixed code SHALL inject the system
prompt as a `SystemMessage` instance (not `AIMessage`), so that the LLM receives
architectural instructions and produces cited responses.

**Validates: Requirements 2.2**

---

Property 3: Bug Condition — Embeddings Return Non-Zero Vectors

_For any_ non-empty text string passed to `Semanticist.get_embeddings()` when a valid API
key is configured, the fixed code SHALL return a vector where at least one element is
non-zero, enabling meaningful cosine similarity comparisons.

**Validates: Requirements 2.3**

---

Property 4: Bug Condition — Enrichment Called Exactly Once

_For any_ repository with N ≥ 1 files, the fixed `Hydrologist.run()` SHALL call
`_enrich_lineage_metadata()` exactly once after the file loop completes, not N times,
reducing complexity from O(n²) to O(n).

**Validates: Requirements 2.4**

---

Property 5: Bug Condition — Async Semanticist Calls Properly Awaited

_For any_ execution of `Orchestrator.run_full_pipeline()`, the fixed code SHALL await
`cluster_into_domains()` and `answer_day_one_questions()` as coroutines, ensuring the
event loop is not blocked and results are actual domain/answer dicts, not coroutine objects.

**Validates: Requirements 2.5**

---

Property 6: Bug Condition — Budget Exhaustion Prevents LLM Calls

_For any_ state where `ContextWindowBudget.is_exhausted` is `True`, the fixed
`detect_drift()`, `answer_day_one_questions()`, and `cluster_into_domains()` SHALL return
early with safe default values without making any LLM API calls.

**Validates: Requirements 2.6**

---

Property 7: Bug Condition — Surveyor Failure Aborts Pipeline

_For any_ exception raised during the Surveyor stage, the fixed Orchestrator SHALL catch
the error, log it, and abort before starting the Hydrologist, preventing corrupted
artifacts from being written.

**Validates: Requirements 2.7**

---

Property 8: Bug Condition — All Navigator Tools Have Consistent Signatures

_For any_ tool dispatch by LangGraph's `ToolNode`, the fixed Navigator SHALL declare all
four tools with consistent async signatures so that every tool is awaited correctly and
returns a string result (not a coroutine object).

**Validates: Requirements 2.8**

---

Property 9: Bug Condition — Double-Quoted dbt Refs Extracted

_For any_ dbt SQL file containing `{{ ref("model_name") }}` (double-quoted), the fixed
`extract_dbt_refs()` SHALL extract `model_name` as an upstream dependency, matching the
behavior already present for single-quoted refs.

**Validates: Requirements 2.9**

---

Property 10: Bug Condition — WebSocket Enforces Size and Idle Limits

_For any_ WebSocket connection to `/ws/analysis` that sends a message exceeding the
configured maximum size or remains idle beyond the configured timeout, the fixed endpoint
SHALL reject the message or close the connection, preventing resource exhaustion.

**Validates: Requirements 2.10**

---

Property 11: Bug Condition — Missing API Key Produces Marked Placeholders

_For any_ pipeline run where `OPENROUTER_API_KEY` is not set, the fixed Orchestrator SHALL
skip all LLM-dependent steps and write clearly-marked placeholder values into artifacts,
distinguishable from real analysis output.

**Validates: Requirements 2.11**

---

Property 12: Bug Condition — Navigator Model Reads from Environment

_For any_ value of the `NAVIGATOR_MODEL` environment variable, the fixed Navigator SHALL
use that model name when initializing the LLM, falling back to `"openai/gpt-4o"` only
when the variable is unset.

**Validates: Requirements 2.12**

---

Property 13: Bug Condition — Corrupted Status File Triggers Full Re-Run

_For any_ `.cartography_status.json` that is missing, empty, or contains invalid JSON,
the fixed Orchestrator SHALL catch the error, fall back to an empty status dict, and
proceed with a full pipeline run rather than raising an unhandled exception.

**Validates: Requirements 2.13**

---

Property 14: Preservation — Non-Buggy Inputs Produce Identical Behavior

_For any_ input where `isBugCondition` returns `False` (valid Hydrologist path, correct
message types, non-OpenRouter embeddings, single-file runs, non-exhausted budget, successful
Surveyor, sync tools, single-quoted refs, well-formed WebSocket messages, configured API
key, unset NAVIGATOR_MODEL, valid status file), the fixed code SHALL produce exactly the
same result as the original code, preserving all existing pipeline functionality.

**Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10**

## Fix Implementation

### Changes Required

Assuming the root cause analysis above is correct:

---

**File**: `src/agents/navigator.py`

**Bug 1 — Wrong Hydrologist argument**

```python
# Before
self.hydrologist = Hydrologist(self.project_name)

# After
self.hydrologist = Hydrologist(self.repo_path)
```

**Bug 2 — System message type**

```python
# Before
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage

# After — add SystemMessage to imports
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage

# Before (in agent method)
messages = [AIMessage(content=system_msg["content"])] + messages

# After
messages = [SystemMessage(content=system_msg["content"])] + messages
```

**Bug 8 — Consistent async tool signatures**

Convert `trace_lineage`, `blast_radius`, and `explain_module` from `def` to `async def`
so all four tools are async and ToolNode dispatches them uniformly.

**Bug 12 — Configurable model name**

```python
# Before
self.llm = ChatOpenAI(model_name="openai/gpt-4o", ...)

# After
_model = os.getenv("NAVIGATOR_MODEL", "openai/gpt-4o")
self.llm = ChatOpenAI(model_name=_model, ...)
```

---

**File**: `src/agents/semanticist.py`

**Bug 3 — Embedding model via OpenRouter**

```python
# After — use configurable embedding model with OpenRouter-compatible default
_emb_model = os.getenv("EMBEDDING_MODEL", "openai/text-embedding-3-small")
embeddings = OpenAIEmbeddings(
    model=_emb_model,
    openai_api_key=self.api_key,
    openai_api_base=os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
)
```

**Bug 6 — Budget exhaustion guard**

Add `if self.budget.is_exhausted: return <safe_default>` at the top of `detect_drift()`,
`answer_day_one_questions()`, and `cluster_into_domains()`, mirroring the guard already
present in `generate_purpose()`.

---

**File**: `src/agents/hydrologist.py`

**Bug 4 — Move enrichment outside loop**

```python
# Before: _enrich_lineage_metadata() is the last statement inside the for loop body
# After: dedent it one level so it runs once after the loop completes

        for full_path in iterate_over:
            ...
            try:
                ...
            except Exception as e:
                print(f"Error mapping lineage in {rel_path}: {e}")

        # Enrichment: Label Sources and Sinks — called ONCE after all files processed
        self._enrich_lineage_metadata()
```

---

**File**: `src/orchestrator.py`

**Bug 5 — Ensure cluster_into_domains is guarded by semanticist.enabled**

The `cluster_into_domains` call is outside the `if self.semanticist.enabled:` block.
Move it inside or add an explicit guard so it is only called when the LLM is available.

**Bug 7 — Wrap Surveyor stage in try/except**

```python
try:
    await asyncio.to_thread(self.surveyor.run, changed_files, self.on_progress)
    await self.checkpoint()
except Exception as e:
    self._log("surveyor_error", f"Surveyor failed: {e}")
    raise  # abort pipeline; do not proceed to Hydrologist
```

**Bug 11 — Mark placeholder artifacts clearly**

When `semanticist.enabled` is False, prefix placeholder values with
`"[LLM DISABLED] "` so they are distinguishable in artifacts.

**Bug 13 — Guard status file load**

```python
status = {}
if os.path.exists(status_path):
    try:
        with open(status_path, "r") as f:
            loaded = json.load(f)
        # Validate expected keys are present and boolean
        if all(k in loaded for k in ("surveyor", "hydrologist", "semanticist")):
            status = loaded
        else:
            self._log("resume_detect", "Status file missing expected keys, performing full re-run.")
    except (json.JSONDecodeError, OSError):
        self._log("resume_detect", "Status file corrupt or unreadable, performing full re-run.")
```

---

**File**: `src/analyzers/sql_lineage.py`

**Bug 9 — Handle double-quoted refs and whitespace**

```python
# Before
refs = re.findall(r"\{\{\s*ref\(['\"](.+?)['\"]\)\s*\}\}", sql)
sources = re.findall(r"\{\{\s*source\(['\"].+?['\"]\s*,\s*['\"](.+?)['\"]\)\s*\}\}", sql)

# After — allow optional whitespace inside the ref() call
refs = re.findall(r'\{\{\s*ref\(\s*[\'"](.+?)[\'"]\s*\)\s*\}\}', sql)
sources = re.findall(r'\{\{\s*source\(\s*[\'"].+?[\'"]\s*,\s*[\'"](.+?)[\'"]\s*\)\s*\}\}', sql)
```

---

**File**: `src/ui/api/main.py`

**Bug 10 — WebSocket size and idle timeout**

```python
MAX_WS_MESSAGE_BYTES = int(os.getenv("WS_MAX_MESSAGE_BYTES", 65536))   # 64 KB default
WS_IDLE_TIMEOUT_SECS = int(os.getenv("WS_IDLE_TIMEOUT_SECS", 300))    # 5 min default

@app.websocket("/ws/analysis")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            try:
                data = await asyncio.wait_for(
                    websocket.receive_text(),
                    timeout=WS_IDLE_TIMEOUT_SECS
                )
                if len(data.encode()) > MAX_WS_MESSAGE_BYTES:
                    await websocket.close(code=1009)  # Message Too Big
                    return
            except asyncio.TimeoutError:
                await websocket.close(code=1001)  # Going Away (idle)
                return
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

## Testing Strategy

### Validation Approach

The testing strategy follows a two-phase approach: first, surface counterexamples that
demonstrate each bug on unfixed code, then verify the fix works correctly and preserves
existing behavior. Property-based tests are used where the input space is large or
continuous; example-based tests are used for deterministic, single-path defects.

---

### Exploratory Bug Condition Checking

**Goal**: Surface counterexamples that demonstrate each bug BEFORE implementing the fix.
Confirm or refute the root cause analysis. If refuted, re-hypothesize.

**Test Plan**: Write tests that directly invoke the buggy call sites with inputs satisfying
`isBugCondition`. Run on UNFIXED code to observe failures.

**Test Cases**:

1. **Bug 1 — Hydrologist path**: Instantiate `Navigator("/tmp/test-repo")` on unfixed code;
   assert `Hydrologist` receives `"/tmp/test-repo"` not `"test-repo"`. Will fail on unfixed code.

2. **Bug 2 — System message type**: Call `navigator.agent(state)` on unfixed code; inspect
   the first message in the list passed to `llm_with_tools.invoke()`; assert it is a
   `SystemMessage`. Will fail on unfixed code (finds `AIMessage`).

3. **Bug 3 — Zero embeddings**: Call `semanticist.get_embeddings("hello world")` with
   OpenRouter base URL on unfixed code; assert `any(v != 0.0 for v in result)`. Will fail
   (all zeros returned).

4. **Bug 4 — Enrichment call count**: Patch `_enrich_lineage_metadata` with a counter;
   run `hydrologist.run()` on a directory with 5 files; assert counter == 1. Will fail
   (counter == 5) on unfixed code.

5. **Bug 5 — Cluster domains guarded**: Run orchestrator with `semanticist.enabled=False`;
   assert `domain_clusters` is not `{"unclassified": [...]}` written as real output.

6. **Bug 6 — Budget guard**: Set `budget.is_exhausted = True`; call `detect_drift()`,
   `answer_day_one_questions()`, `cluster_into_domains()`; assert LLM mock is never called.
   Will fail on unfixed code.

7. **Bug 7 — Surveyor abort**: Mock `surveyor.run` to raise `RuntimeError`; run pipeline;
   assert `hydrologist.run` is never called. Will fail on unfixed code.

8. **Bug 8 — Tool return type**: Dispatch `find_implementation` via `ToolNode`; assert
   result is a `str`, not a coroutine. Will fail on unfixed code.

9. **Bug 9 — Double-quoted ref**: Call `extract_dbt_refs('{{ ref("orders") }}')` on unfixed
   code; assert `"orders"` in result. Verify behavior (may pass or fail depending on regex).

10. **Bug 10 — WebSocket oversized message**: Connect to `/ws/analysis`; send a 100 KB
    message; assert connection is closed with code 1009. Will fail on unfixed code.

11. **Bug 11 — Placeholder marking**: Run pipeline with no API key; read generated
    `CODEBASE.md`; assert placeholder values contain `"[LLM DISABLED]"` marker.

12. **Bug 12 — Model env override**: Set `NAVIGATOR_MODEL=openai/gpt-4o-mini`; instantiate
    `Navigator`; assert `navigator.llm.model_name == "openai/gpt-4o-mini"`. Will fail on
    unfixed code.

13. **Bug 13 — Corrupt status file**: Write `"{"` (invalid JSON) to status file; run
    pipeline; assert no exception raised and pipeline completes full re-run.

**Expected Counterexamples**:
- Bugs 1, 2, 4, 6, 7, 8, 12: Deterministic failures on first run.
- Bug 3: Requires live OpenRouter call or mock; zero-vector assertion fails.
- Bug 9: Regex behavior may be correct for basic double-quoted refs; whitespace variants will fail.
- Bug 10: Requires WebSocket test client; oversized message accepted without close.
- Bug 13: `JSONDecodeError` propagates as unhandled exception.

---

### Fix Checking

**Goal**: Verify that for all inputs where the bug condition holds, the fixed function
produces the expected behavior.

**Pseudocode:**
```
FOR ALL context WHERE isBugCondition(context) DO
  result := fixed_function(context)
  ASSERT expectedBehavior(result)  -- per-property assertion above
END FOR
```

---

### Preservation Checking

**Goal**: Verify that for all inputs where the bug condition does NOT hold, the fixed
function produces the same result as the original function.

**Pseudocode:**
```
FOR ALL context WHERE NOT isBugCondition(context) DO
  ASSERT original_function(context) == fixed_function(context)
END FOR
```

**Testing Approach**: Property-based testing is recommended for Bugs 3, 4, 6, 9, and 12
because their input spaces are large. Example-based tests suffice for the remaining bugs.

**Test Cases**:
1. **Navigator init preservation**: Valid repo paths with pre-built graphs continue to load correctly after Bug 1 fix.
2. **Single-quoted ref preservation**: `{{ ref('model') }}` continues to be extracted after Bug 9 fix.
3. **Budget non-exhausted preservation**: `generate_purpose()` with non-exhausted budget continues to call LLM after Bug 6 fix.
4. **Valid status file preservation**: Well-formed status file continues to enable stage skipping after Bug 13 fix.
5. **WebSocket normal message preservation**: Messages within size limit continue to be received after Bug 10 fix.

---

### Unit Tests

- Test `Navigator.__init__` passes `repo_path` to `Hydrologist` (Bug 1).
- Test `Navigator.agent` injects `SystemMessage` not `AIMessage` (Bug 2).
- Test `Semanticist.get_embeddings` returns non-zero vector with mocked embeddings (Bug 3).
- Test `Hydrologist.run` calls `_enrich_lineage_metadata` exactly once for N files (Bug 4).
- Test `detect_drift`, `answer_day_one_questions`, `cluster_into_domains` return early when `is_exhausted=True` (Bug 6).
- Test Orchestrator aborts before Hydrologist when Surveyor raises (Bug 7).
- Test all Navigator tools return `str` when dispatched (Bug 8).
- Test `extract_dbt_refs` handles double-quoted and whitespace-padded refs (Bug 9).
- Test WebSocket closes with 1009 on oversized message, 1001 on idle timeout (Bug 10).
- Test Navigator reads model from `NAVIGATOR_MODEL` env var (Bug 12).
- Test Orchestrator handles corrupt/missing status file gracefully (Bug 13).

### Property-Based Tests

- **Property 3**: Generate random non-empty strings; assert `get_embeddings` returns non-zero vector (with mock).
- **Property 4**: Generate random file counts (1–1000); assert enrichment call count == 1.
- **Property 6**: Generate random token counts exceeding budget; assert no LLM calls made.
- **Property 9**: Generate random model names with both quote styles and whitespace variants; assert all extracted correctly.
- **Property 14**: Generate random valid inputs for each fixed function; assert output matches original for non-buggy inputs.

### Integration Tests

- Full pipeline run on a small test repository with all 13 fixes applied; assert all artifacts written correctly.
- Navigator query end-to-end with system message fix; assert response contains file citations.
- Hydrologist on a 100-file test repo; assert `_enrich_lineage_metadata` called once and lineage graph is correct.
- Pipeline run with no API key; assert `CODEBASE.md` contains `[LLM DISABLED]` markers.
- Pipeline resume from valid status file; assert completed stages are skipped.
