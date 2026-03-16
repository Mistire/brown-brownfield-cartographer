# Implementation Plan

- [x] 1. Write bug condition exploration tests (BEFORE implementing any fix)
  - **Property 1: Bug Condition** - All 13 Bugs Confirmed on Unfixed Code
  - **CRITICAL**: These tests MUST FAIL on unfixed code — failure confirms each bug exists
  - **DO NOT attempt to fix the tests or the code when they fail**
  - **NOTE**: These tests encode the expected behavior — they will validate the fixes when they pass after implementation
  - **GOAL**: Surface counterexamples that demonstrate each bug exists
  - **Scoped PBT Approach**: For deterministic bugs, scope each property to the concrete failing case to ensure reproducibility
  - Create `tests/test_bug_conditions.py`
  - Bug 1: Instantiate `Navigator("/tmp/test-repo")`; capture the path passed to `Hydrologist()`; assert it equals `"/tmp/test-repo"` not `"test-repo"` (from Bug Condition: `context.arg_to_hydrologist == project_name`)
  - Bug 2: Call `navigator.agent(state)` on unfixed code; inspect first message passed to `llm_with_tools.invoke()`; assert it is a `SystemMessage` instance (from Bug Condition: `context.system_msg_type == AIMessage`)
  - Bug 3: Mock `OpenAIEmbeddings.aembed_query` to raise an exception (simulating OpenRouter 404); call `semanticist.get_embeddings("hello world")`; assert `any(v != 0.0 for v in result)` — will fail because fallback returns all zeros
  - Bug 4: Patch `_enrich_lineage_metadata` with a call counter; run `hydrologist.run()` on a temp dir with 5 dummy `.py` files; assert counter == 1 — will fail (counter == 5) on unfixed code
  - Bug 5: Run orchestrator with `semanticist.enabled=False`; assert `domain_clusters` is not written as real output (i.e., not `{"unclassified": [...]}` without a `[LLM DISABLED]` marker)
  - Bug 6: Set `budget.is_exhausted = True`; call `detect_drift()`, `answer_day_one_questions()`, `cluster_into_domains()` with a mock LLM; assert mock LLM is never called — will fail on unfixed code
  - Bug 7: Mock `surveyor.run` to raise `RuntimeError("disk error")`; run pipeline; assert `hydrologist.run` is never called — will fail on unfixed code
  - Bug 8: Dispatch `find_implementation` via `ToolNode`; assert result is a `str`, not a coroutine object — will fail on unfixed code
  - Bug 9: Call `extract_dbt_refs('{{ ref("orders") }}')` (double-quoted); assert `"orders"` in result; also test `{{ ref( "orders" ) }}` with whitespace — verify behavior
  - Bug 10: Connect to `/ws/analysis` via test client; send a message of 100 KB; assert connection is closed with code 1009 — will fail on unfixed code
  - Bug 11: Run pipeline with no API key; read generated `CODEBASE.md`; assert placeholder values contain `"[LLM DISABLED]"` marker — will fail on unfixed code
  - Bug 12: Set env `NAVIGATOR_MODEL=openai/gpt-4o-mini`; instantiate `Navigator`; assert `navigator.llm.model_name == "openai/gpt-4o-mini"` — will fail on unfixed code
  - Bug 13: Write `"{"` (invalid JSON) to `.cartography_status.json`; run pipeline; assert no exception raised and pipeline proceeds with full re-run — will fail on unfixed code
  - Run all tests on UNFIXED code
  - **EXPECTED OUTCOME**: Tests FAIL (this is correct — it proves the bugs exist)
  - Document counterexamples found to understand root cause for each bug
  - Mark task complete when tests are written, run, and failures are documented
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13_

- [x] 2. Write preservation property tests (BEFORE implementing any fix)
  - **Property 2: Preservation** - Non-Buggy Inputs Produce Identical Behavior
  - **IMPORTANT**: Follow observation-first methodology — run UNFIXED code with non-buggy inputs, observe outputs, then write tests
  - Create `tests/test_preservation.py`
  - Observe: `Navigator("/tmp/valid-repo")` with a pre-built knowledge graph loads correctly on unfixed code — write property test asserting this holds for any valid repo path
  - Observe: `extract_dbt_refs("{{ ref('model_name') }}")` (single-quoted) returns `{"model_name"}` on unfixed code — write property test asserting single-quoted refs are always extracted (for all valid model name strings)
  - Observe: `generate_purpose(code, size)` with non-exhausted budget calls LLM and returns `(str, float)` on unfixed code — write property test asserting this holds for any non-empty code string
  - Observe: Orchestrator resumes from a valid well-formed `.cartography_status.json` and skips completed stages on unfixed code — write test asserting this holds
  - Observe: WebSocket messages within 64 KB are received normally on unfixed code — write property test asserting messages of size 1–65536 bytes are accepted
  - Observe: `ContextWindowBudget.record()` accumulates tokens and sets `is_exhausted` correctly on unfixed code — write property test for any token count
  - Observe: `/analyze` endpoint returns immediate acknowledgement for any valid repo path on unfixed code — write test asserting this
  - Observe: `/query` endpoint routes to Navigator and returns an answer for any valid project/query on unfixed code — write test asserting this
  - Property-based tests use `hypothesis` to generate inputs across the input domain for stronger guarantees
  - Run all preservation tests on UNFIXED code
  - **EXPECTED OUTCOME**: Tests PASS (this confirms baseline behavior to preserve)
  - Mark task complete when tests are written, run, and passing on unfixed code
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10_

- [x] 3. Fix Bug 1 — Navigator passes wrong argument to Hydrologist

  - [x] 3.1 Implement the fix in `src/agents/navigator.py`
    - Change `self.hydrologist = Hydrologist(self.project_name)` to `self.hydrologist = Hydrologist(self.repo_path)`
    - _Bug_Condition: `context.call_site == "Navigator.__init__" AND context.arg_to_hydrologist == project_name`_
    - _Expected_Behavior: Hydrologist receives `repo_path` (a valid filesystem path), initializes without error_
    - _Preservation: Navigator instantiation with valid repo path and pre-built graph continues to load graph, bind tools, compile workflow (Req 3.1)_
    - _Requirements: 2.1, 3.1_

  - [x] 3.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Navigator Receives Valid Repo Path
    - **IMPORTANT**: Re-run the SAME test from task 1 (Bug 1 case) — do NOT write a new test
    - Run `tests/test_bug_conditions.py::test_bug1_hydrologist_path`
    - **EXPECTED OUTCOME**: Test PASSES (confirms bug is fixed)
    - _Requirements: 2.1_

  - [x] 3.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Navigator Init with Valid Repo Path
    - **IMPORTANT**: Re-run the SAME tests from task 2 — do NOT write new tests
    - Run preservation tests covering Navigator initialization
    - **EXPECTED OUTCOME**: Tests PASS (confirms no regressions)

- [x] 4. Fix Bug 2 — Navigator system message injected as wrong type

  - [x] 4.1 Implement the fix in `src/agents/navigator.py`
    - Add `SystemMessage` to the import: `from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage`
    - Change `messages = [AIMessage(content=system_msg["content"])] + messages` to `messages = [SystemMessage(content=system_msg["content"])] + messages`
    - _Bug_Condition: `context.call_site == "Navigator.agent" AND context.system_msg_type == AIMessage`_
    - _Expected_Behavior: LLM receives system prompt as `SystemMessage`, produces cited high-quality responses_
    - _Preservation: Navigator query flow continues to invoke agent loop, call tools, return cited answer (Req 3.2)_
    - _Requirements: 2.2, 3.2_

  - [x] 4.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - System Prompt Delivered as SystemMessage
    - Re-run `tests/test_bug_conditions.py::test_bug2_system_message_type`
    - **EXPECTED OUTCOME**: Test PASSES

  - [x] 4.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Navigator Query Flow
    - Re-run preservation tests covering Navigator query behavior
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 5. Fix Bug 3 — Embeddings return zero vectors via OpenRouter

  - [x] 5.1 Implement the fix in `src/agents/semanticist.py`
    - In `get_embeddings()`, replace hardcoded `"text-embedding-3-small"` with `os.getenv("EMBEDDING_MODEL", "openai/text-embedding-3-small")`
    - Use the configurable model so operators can point to an OpenRouter-supported embedding model
    - _Bug_Condition: `context.call_site == "Semanticist.get_embeddings" AND context.api_base CONTAINS "openrouter.ai" AND context.model == "text-embedding-3-small"`_
    - _Expected_Behavior: Returns a vector where at least one element is non-zero, enabling meaningful cosine similarity_
    - _Preservation: `generate_purpose()` with valid API key and non-exhausted budget continues to invoke LLM and return purpose string (Req 3.4)_
    - _Requirements: 2.3, 3.4_

  - [x] 5.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Embeddings Return Non-Zero Vectors
    - Re-run `tests/test_bug_conditions.py::test_bug3_embeddings_nonzero`
    - **EXPECTED OUTCOME**: Test PASSES

  - [x] 5.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Semanticist generate_purpose Behavior
    - Re-run preservation tests covering Semanticist LLM calls
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 6. Fix Bug 4 — Hydrologist O(n²) metadata enrichment

  - [x] 6.1 Implement the fix in `src/agents/hydrologist.py`
    - Move `self._enrich_lineage_metadata()` call from inside the `for full_path in iterate_over:` loop to after the loop completes (dedent one level)
    - Remove the call from inside the `try` block; place it once after the loop body
    - _Bug_Condition: `context.call_site == "Hydrologist.run" AND context.enrich_call_count > 1`_
    - _Expected_Behavior: `_enrich_lineage_metadata()` called exactly once after all files processed, O(n) complexity_
    - _Preservation: Hydrologist continues to build correct lineage graph with source/sink labels for Python, SQL, YAML files (Req 3.3)_
    - _Requirements: 2.4, 3.3_

  - [x] 6.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Enrichment Called Exactly Once
    - Re-run `tests/test_bug_conditions.py::test_bug4_enrichment_call_count`
    - **EXPECTED OUTCOME**: Test PASSES (counter == 1 for any N files)

  - [x] 6.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Hydrologist Lineage Graph Correctness
    - Re-run preservation tests covering Hydrologist lineage output
    - **EXPECTED OUTCOME**: Tests PASS

- [ ] 7. Fix Bug 5 — cluster_into_domains called without semanticist.enabled guard

  - [x] 7.1 Implement the fix in `src/orchestrator.py`
    - Move the `domain_clusters = await self.semanticist.cluster_into_domains(module_data)` call inside the `if self.semanticist.enabled:` block, or add an explicit guard
    - When `semanticist.enabled` is False, set `domain_clusters = {}` directly without calling the method
    - _Bug_Condition: `context.call_site IN ["Orchestrator.run_full_pipeline"] AND context.awaited == False AND context.method IN ["cluster_into_domains", "answer_day_one_questions"]`_
    - _Expected_Behavior: `cluster_into_domains()` and `answer_day_one_questions()` only called when LLM is available; results are actual dicts not coroutine objects_
    - _Preservation: Full pipeline execution continues to write all artifacts to output directory (Req 3.5)_
    - _Requirements: 2.5, 3.5_

  - [x] 7.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Async Semanticist Calls Properly Guarded
    - Re-run `tests/test_bug_conditions.py::test_bug5_cluster_domains_guarded`
    - **EXPECTED OUTCOME**: Test PASSES

  - [x] 7.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Full Pipeline Artifact Output
    - Re-run preservation tests covering full pipeline execution
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 8. Fix Bug 6 — Token budget exhaustion flag never checked

  - [x] 8.1 Implement the fix in `src/agents/semanticist.py`
    - Add `if self.budget.is_exhausted: return <safe_default>` at the top of `detect_drift()` (return `{"drift_detected": False, "score": 0.0, "confidence": 0.0}`)
    - Add `if self.budget.is_exhausted: return {f"q{i+1}": "Budget exhausted." for i in range(5)}` at the top of `answer_day_one_questions()`
    - Add `if self.budget.is_exhausted: return {"unclassified": [str(m.get("path", "")) for m in nodes]}` at the top of `cluster_into_domains()`
    - Mirror the guard already present in `generate_purpose()`
    - _Bug_Condition: `context.call_site IN ["detect_drift","answer_day_one_questions","cluster_into_domains"] AND context.budget.is_exhausted == True`_
    - _Expected_Behavior: Returns early with safe default value without making any LLM API calls_
    - _Preservation: `ContextWindowBudget.record()` continues to accumulate tokens and set `is_exhausted` correctly (Req 3.10); `generate_purpose()` with non-exhausted budget continues to call LLM (Req 3.4)_
    - _Requirements: 2.6, 3.4, 3.10_

  - [x] 8.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Budget Exhaustion Prevents LLM Calls
    - Re-run `tests/test_bug_conditions.py::test_bug6_budget_exhaustion_guard`
    - **EXPECTED OUTCOME**: Test PASSES (mock LLM never called when budget exhausted)

  - [x] 8.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Non-Exhausted Budget Calls LLM Normally
    - Re-run preservation tests covering budget non-exhausted path
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 9. Fix Bug 7 — No error recovery when Surveyor fails

  - [x] 9.1 Implement the fix in `src/orchestrator.py`
    - Wrap `await asyncio.to_thread(self.surveyor.run, changed_files, self.on_progress)` and `await self.checkpoint()` in a `try/except Exception as e:` block
    - In the except block: call `self._log("surveyor_error", f"Surveyor failed: {e}")` then `raise` to abort the pipeline
    - This prevents Hydrologist from running on an empty module graph
    - _Bug_Condition: `context.call_site == "Orchestrator.run_full_pipeline" AND context.surveyor_raised == True AND context.hydrologist_started == True`_
    - _Expected_Behavior: Surveyor exception is caught, logged, and pipeline aborts before Hydrologist runs_
    - _Preservation: Full pipeline execution on a repository that has not been analyzed before continues to execute Surveyor → Hydrologist → Semanticist → Archivist in sequence (Req 3.5)_
    - _Requirements: 2.7, 3.5_

  - [x] 9.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Surveyor Failure Aborts Pipeline
    - Re-run `tests/test_bug_conditions.py::test_bug7_surveyor_abort`
    - **EXPECTED OUTCOME**: Test PASSES (hydrologist.run never called after surveyor raises)

  - [x] 9.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Full Pipeline on Successful Surveyor
    - Re-run preservation tests covering successful full pipeline execution
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 10. Fix Bug 8 — Navigator tools have inconsistent async/sync signatures

  - [x] 10.1 Implement the fix in `src/agents/navigator.py`
    - Convert `trace_lineage`, `blast_radius`, and `explain_module` from `def` to `async def` so all four tools are async
    - This ensures LangGraph's `ToolNode` dispatches and awaits all tools uniformly
    - _Bug_Condition: `context.call_site == "Navigator.tools" AND context.tool_name == "find_implementation" AND context.execution_mode == "sync_dispatch"`_
    - _Expected_Behavior: All four tools declared async; every tool dispatched and awaited correctly; results are strings not coroutine objects_
    - _Preservation: Navigator query flow continues to invoke agent loop, call tools, return cited answer (Req 3.2)_
    - _Requirements: 2.8, 3.2_

  - [x] 10.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - All Navigator Tools Have Consistent Signatures
    - Re-run `tests/test_bug_conditions.py::test_bug8_tool_return_type`
    - **EXPECTED OUTCOME**: Test PASSES (all tools return str, not coroutine)

  - [x] 10.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Navigator Tool Dispatch
    - Re-run preservation tests covering Navigator tool execution
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 11. Fix Bug 9 — SQL lineage regex only handles single-quoted dbt refs

  - [x] 11.1 Implement the fix in `src/analyzers/sql_lineage.py`
    - Update `extract_dbt_refs()` regex to allow optional whitespace inside the `ref()` call:
      - `refs = re.findall(r'\{\{\s*ref\(\s*[\'"](.+?)[\'"]\s*\)\s*\}\}', sql)`
      - `sources = re.findall(r'\{\{\s*source\(\s*[\'"].+?[\'"]\s*,\s*[\'"](.+?)[\'"]\s*\)\s*\}\}', sql)`
    - This handles both single-quoted, double-quoted, and whitespace-padded variants
    - _Bug_Condition: `context.call_site == "SQLLineageAnalyzer.extract_dbt_refs" AND context.sql CONTAINS 'ref("'`_
    - _Expected_Behavior: `model_name` extracted from `{{ ref("model_name") }}` as upstream dependency_
    - _Preservation: Single-quoted `{{ ref('model_name') }}` continues to be extracted as upstream dependency (Req 3.7)_
    - _Requirements: 2.9, 3.7_

  - [x] 11.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Double-Quoted dbt Refs Extracted
    - Re-run `tests/test_bug_conditions.py::test_bug9_double_quoted_ref`
    - **EXPECTED OUTCOME**: Test PASSES (double-quoted and whitespace-padded refs extracted)

  - [x] 11.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Single-Quoted dbt Ref Extraction
    - Re-run preservation tests covering single-quoted ref extraction
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 12. Fix Bug 10 — WebSocket endpoint has no timeout or max message size

  - [x] 12.1 Implement the fix in `src/ui/api/main.py`
    - Add module-level constants: `MAX_WS_MESSAGE_BYTES = int(os.getenv("WS_MAX_MESSAGE_BYTES", 65536))` and `WS_IDLE_TIMEOUT_SECS = int(os.getenv("WS_IDLE_TIMEOUT_SECS", 300))`
    - Rewrite the `websocket_endpoint` receive loop to use `asyncio.wait_for(..., timeout=WS_IDLE_TIMEOUT_SECS)`
    - After receiving data, check `if len(data.encode()) > MAX_WS_MESSAGE_BYTES: await websocket.close(code=1009); return`
    - Catch `asyncio.TimeoutError` and close with `code=1001`
    - _Bug_Condition: `context.call_site == "/ws/analysis" AND (context.message_size > MAX_SIZE OR context.idle_seconds > TIMEOUT)`_
    - _Expected_Behavior: Oversized messages rejected with close code 1009; idle connections closed with code 1001_
    - _Preservation: `/analyze` endpoint continues to start pipeline as background task and return immediate acknowledgement (Req 3.8); `/query` endpoint continues to route queries (Req 3.9)_
    - _Requirements: 2.10, 3.8, 3.9_

  - [x] 12.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - WebSocket Enforces Size and Idle Limits
    - Re-run `tests/test_bug_conditions.py::test_bug10_websocket_oversized_message`
    - **EXPECTED OUTCOME**: Test PASSES (connection closed with 1009 on oversized message)

  - [x] 12.3 Verify preservation tests still pass
    - **Property 2: Preservation** - WebSocket Normal Message Handling
    - Re-run preservation tests covering WebSocket messages within size limit
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 13. Fix Bug 11 — No validation that OPENROUTER_API_KEY is set before Semanticist runs

  - [x] 13.1 Implement the fix in `src/orchestrator.py`
    - When `semanticist.enabled` is False, prefix all placeholder values with `"[LLM DISABLED] "` before writing to artifacts
    - Ensure `domain_clusters` and `day_one_answers` are clearly marked when LLM is disabled
    - _Bug_Condition: `context.call_site IN ["cluster_into_domains","answer_day_one_questions"] AND context.api_key == None AND context.result_written_as_real == True`_
    - _Expected_Behavior: Placeholder values contain `"[LLM DISABLED]"` marker, distinguishable from real analysis output_
    - _Preservation: Full pipeline execution continues to write all artifacts to output directory (Req 3.5)_
    - _Requirements: 2.11, 3.5_

  - [x] 13.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Missing API Key Produces Marked Placeholders
    - Re-run `tests/test_bug_conditions.py::test_bug11_placeholder_marking`
    - **EXPECTED OUTCOME**: Test PASSES (`CODEBASE.md` contains `[LLM DISABLED]` markers)

  - [x] 13.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Full Pipeline with API Key Configured
    - Re-run preservation tests covering full pipeline with API key set
    - **EXPECTED OUTCOME**: Tests PASS

- [ ] 14. Fix Bug 12 — LLM model name is hardcoded with no config override

  - [x] 14.1 Implement the fix in `src/agents/navigator.py`
    - Replace `model_name="openai/gpt-4o"` with `model_name=os.getenv("NAVIGATOR_MODEL", "openai/gpt-4o")`
    - Apply to both the `if self.api_key:` branch and the `else:` branch (fallback `ChatOpenAI`)
    - _Bug_Condition: `context.call_site == "Navigator.__init__" AND context.NAVIGATOR_MODEL_env_set == True AND context.model_used == "openai/gpt-4o"`_
    - _Expected_Behavior: Navigator uses `NAVIGATOR_MODEL` env var value when set, falls back to `"openai/gpt-4o"` when unset_
    - _Preservation: Navigator instantiation with valid repo path continues to work when `NAVIGATOR_MODEL` is unset (Req 3.1)_
    - _Requirements: 2.12, 3.1_

  - [x] 14.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Navigator Model Reads from Environment
    - Re-run `tests/test_bug_conditions.py::test_bug12_model_env_override`
    - **EXPECTED OUTCOME**: Test PASSES (`navigator.llm.model_name == "openai/gpt-4o-mini"` when env set)

  - [x] 14.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Navigator Default Model When Env Unset
    - Re-run preservation tests covering Navigator instantiation without `NAVIGATOR_MODEL` set
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 15. Fix Bug 13 — Checkpoint status file has no corruption validation

  - [x] 15.1 Implement the fix in `src/orchestrator.py`
    - Replace the unguarded `json.load(f)` block with a try/except that catches `json.JSONDecodeError` and `OSError`
    - After loading, validate that all expected keys (`"surveyor"`, `"hydrologist"`, `"semanticist"`) are present and boolean
    - Fall back to `status = {}` (triggering full re-run) if file is missing, empty, malformed, or missing expected keys
    - Log the fallback reason via `self._log("resume_detect", "...")`
    - _Bug_Condition: `context.call_site == "Orchestrator.run_full_pipeline" AND context.status_file_corrupt == True AND context.exception_raised == True`_
    - _Expected_Behavior: Corrupt/missing status file caught gracefully; pipeline falls back to full re-run without raising_
    - _Preservation: Orchestrator with valid status file continues to skip completed stages and resume from first incomplete stage (Req 3.6)_
    - _Requirements: 2.13, 3.6_

  - [x] 15.2 Verify bug condition exploration test now passes
    - **Property 1: Expected Behavior** - Corrupted Status File Triggers Full Re-Run
    - Re-run `tests/test_bug_conditions.py::test_bug13_corrupt_status_file`
    - **EXPECTED OUTCOME**: Test PASSES (no exception raised; pipeline proceeds with full re-run)

  - [x] 15.3 Verify preservation tests still pass
    - **Property 2: Preservation** - Valid Status File Enables Stage Skipping
    - Re-run preservation tests covering incremental resume from valid status file
    - **EXPECTED OUTCOME**: Tests PASS

- [x] 16. Fix UI — API metadata endpoint ignores filename parameter

  - [x] 16.1 Fix `src/ui/api/main.py` — update `/metadata/{project}` to accept and serve any artifact file
    - Add `filename: str = "CODEBASE.md"` query parameter to `get_metadata()`
    - Resolve the file path as `os.path.join(CARTOGRAPHY_DIR, project, filename)` instead of hardcoding `CODEBASE.md`
    - Return 404 with a clear message if the requested file does not exist
    - This unblocks the `ArtifactViewer` component which already passes `?filename=onboarding_brief.md` but currently always receives `CODEBASE.md`

  - [x] 16.2 Fix `src/ui/dashboard/src/App.tsx` — surface `[LLM DISABLED]` markers in the UI
    - In `ArtifactViewer`, after content is loaded, check if it contains `[LLM DISABLED]`
    - If found, render a visible warning banner above the artifact: "⚠ LLM analysis was disabled during this run. Some sections show placeholder data."
    - Style the banner with an amber/yellow background to make it visually distinct

  - [x] 16.3 Fix `src/ui/dashboard/src/App.tsx` — add WebSocket reconnection logic
    - The current WebSocket setup in `useEffect` connects once and never retries on disconnect
    - Add exponential backoff reconnection: on `ws.onclose`, schedule a reconnect attempt after 2s, 4s, 8s (max 3 retries)
    - Show a "Reconnecting…" status in the Build Console when reconnection is in progress
    - Reset retry counter on successful `pipeline_complete` event

  - [x] 16.4 Fix `src/ui/dashboard/src/App.tsx` — guard Navigator chat against missing project
    - The `handleSendMessage` function checks `!project` but the chat UI is still openable and shows the input when no project is selected
    - When `chatOpen` is true and `project` is null, show a message: "Select a project first to use Navigator."
    - Disable the Send button and input when no project is selected

  - [x] 16.5 Fix `src/ui/dashboard/src/App.tsx` — fix `onKeyPress` deprecation
    - `onKeyPress` is deprecated in React 17+ and removed in React 19
    - Replace `onKeyPress={e => e.key === 'Enter' && handleSendMessage()}` with `onKeyDown={e => e.key === 'Enter' && !e.shiftKey && handleSendMessage()}`

- [x] 17. Checkpoint — Ensure all tests pass
  - Run the full test suite: `pytest tests/ -v`
  - Ensure all 13 bug condition exploration tests now PASS (bugs are fixed)
  - Ensure all preservation tests still PASS (no regressions introduced)
  - Ensure integration tests pass: full pipeline on small test repo, Navigator query end-to-end, Hydrologist on 100-file repo, pipeline with no API key, pipeline resume from valid status file
  - Ask the user if any questions arise
