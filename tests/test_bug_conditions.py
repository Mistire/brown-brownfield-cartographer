"""
Bug condition exploration tests.
These tests MUST FAIL on unfixed code — failure confirms each bug exists.
DO NOT fix the tests or the code when they fail.
"""
import sys
import os
import asyncio
import json
import tempfile
import pytest
from unittest.mock import MagicMock, patch, AsyncMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


# ---------------------------------------------------------------------------
# Bug 1: Navigator passes project_name instead of repo_path to Hydrologist
# ---------------------------------------------------------------------------
def test_bug1_hydrologist_path():
    """Navigator must pass repo_path (not project_name) to Hydrologist."""
    captured = {}

    def fake_hydrologist_init(self, repo_path, graph=None):
        captured["repo_path"] = repo_path
        self.repo_path = repo_path
        self.python_analyzer = MagicMock()
        self.sql_analyzer = MagicMock()
        self.config_parser = MagicMock()
        import networkx as nx
        self.lineage_graph = nx.DiGraph()

    with patch("agents.hydrologist.Hydrologist.__init__", fake_hydrologist_init), \
         patch("graph.knowledge_graph.KnowledgeGraph.load", return_value=MagicMock(
             module_graph=MagicMock(nodes=MagicMock(return_value=[])),
             lineage_graph=MagicMock()
         )), \
         patch("agents.archivist.Archivist.__init__", lambda self, *a, **kw: None), \
         patch("agents.semanticist.Semanticist.__init__", lambda self, *a, **kw: setattr(self, "llm", None) or setattr(self, "budget", MagicMock()) or setattr(self, "api_key", None)), \
         patch("agents.semantic_index.SemanticIndex.__init__", lambda self, *a, **kw: None), \
         patch("langchain_openai.ChatOpenAI.__init__", lambda self, **kw: None), \
         patch("langgraph.graph.StateGraph.compile", return_value=MagicMock()):
        from agents.navigator import Navigator
        Navigator("/tmp/test-repo")

    assert captured.get("repo_path") == "/tmp/test-repo", (
        f"Bug 1: Hydrologist received '{captured.get('repo_path')}' instead of '/tmp/test-repo'"
    )


# ---------------------------------------------------------------------------
# Bug 2: System prompt injected as AIMessage instead of SystemMessage
# ---------------------------------------------------------------------------
def test_bug2_system_message_type():
    """Navigator.agent must inject system prompt as SystemMessage, not AIMessage."""
    from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

    captured_messages = {}

    def fake_invoke(messages):
        captured_messages["first"] = messages[0]
        return AIMessage(content="ok")

    llm_mock = MagicMock()
    llm_mock.invoke = fake_invoke
    llm_mock.bind_tools = MagicMock(return_value=llm_mock)

    with patch("graph.knowledge_graph.KnowledgeGraph.load", return_value=MagicMock(
             module_graph=MagicMock(nodes=MagicMock(return_value=[])),
             lineage_graph=MagicMock()
         )), \
         patch("agents.archivist.Archivist.__init__", lambda self, *a, **kw: None), \
         patch("agents.archivist.Archivist.log_trace", lambda self, *a, **kw: None), \
         patch("agents.semanticist.Semanticist.__init__", lambda self, *a, **kw: setattr(self, "llm", None) or setattr(self, "budget", MagicMock()) or setattr(self, "api_key", None)), \
         patch("agents.semantic_index.SemanticIndex.__init__", lambda self, *a, **kw: None), \
         patch("agents.hydrologist.Hydrologist.__init__", lambda self, *a, **kw: None), \
         patch("langchain_openai.ChatOpenAI.__init__", lambda self, **kw: None), \
         patch("langgraph.graph.StateGraph.compile", return_value=MagicMock()):
        from agents.navigator import Navigator
        nav = Navigator("/tmp/test-repo")
        nav.llm_with_tools = llm_mock

        state = {"messages": [HumanMessage(content="hi")], "context": {}}
        nav.agent(state)

    first_msg = captured_messages.get("first")
    assert isinstance(first_msg, SystemMessage), (
        f"Bug 2: First message is {type(first_msg).__name__}, expected SystemMessage"
    )


# ---------------------------------------------------------------------------
# Bug 3: Embeddings fallback returns zero vector
# ---------------------------------------------------------------------------
@pytest.mark.asyncio
async def test_bug3_embeddings_nonzero():
    """get_embeddings must return a non-zero vector; fallback zeros is the bug."""
    from agents.semanticist import Semanticist

    sem = Semanticist.__new__(Semanticist)
    sem.api_key = "fake-key"
    sem.budget = MagicMock()

    with patch("langchain_openai.OpenAIEmbeddings.aembed_query",
               new_callable=AsyncMock, side_effect=Exception("OpenRouter 404")):
        result = await sem.get_embeddings("hello world")

    assert any(v != 0.0 for v in result), (
        "Bug 3: get_embeddings returned all-zero vector (fallback bug)"
    )


# ---------------------------------------------------------------------------
# Bug 4: _enrich_lineage_metadata called inside per-file loop (O(n²))
# ---------------------------------------------------------------------------
def test_bug4_enrichment_call_count():
    """_enrich_lineage_metadata must be called exactly once after the loop, not per file."""
    import networkx as nx
    from agents.hydrologist import Hydrologist

    with tempfile.TemporaryDirectory() as tmpdir:
        # Create 5 dummy .py files
        for i in range(5):
            path = os.path.join(tmpdir, f"module_{i}.py")
            with open(path, "w") as f:
                f.write(f"x = {i}\n")

        hydro = Hydrologist(tmpdir)
        call_count = {"n": 0}
        original_enrich = hydro._enrich_lineage_metadata

        def counting_enrich():
            call_count["n"] += 1
            original_enrich()

        hydro._enrich_lineage_metadata = counting_enrich
        hydro.run()

    assert call_count["n"] == 1, (
        f"Bug 4: _enrich_lineage_metadata called {call_count['n']} times, expected 1"
    )


# ---------------------------------------------------------------------------
# Bug 5: cluster_into_domains called without semanticist.enabled guard
# ---------------------------------------------------------------------------
@pytest.mark.asyncio
async def test_bug5_cluster_domains_guarded():
    """When semanticist.enabled=False, day_one_answers must contain [LLM DISABLED] marker."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with patch("agents.surveyor.Surveyor.run", return_value=None), \
             patch("agents.hydrologist.Hydrologist.run", return_value=None), \
             patch("agents.archivist.Archivist.generate_codebase_md", return_value=None), \
             patch("agents.archivist.Archivist.generate_interactive_graph", return_value=None), \
             patch("agents.archivist.Archivist.log_trace", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.serialize", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.enrich_metadata", return_value=None):
            from orchestrator import Orchestrator
            orch = Orchestrator(tmpdir)
            orch.semanticist.llm = None
            assert not orch.semanticist.enabled

            captured = {}
            def fake_onboarding(module_data, day_one_answers):
                captured["day_one_answers"] = day_one_answers

            orch.archivist.generate_onboarding_brief = fake_onboarding
            orch.archivist.generate_codebase_md = lambda kg: None
            orch.archivist.generate_interactive_graph = lambda g: None

            await orch.run_full_pipeline()

        day_one = captured.get("day_one_answers", {})
        day_one_str = json.dumps(day_one)
        assert "[LLM DISABLED]" in day_one_str, (
            f"Bug 5: day_one_answers does not contain '[LLM DISABLED]' marker: {day_one_str}"
        )


# ---------------------------------------------------------------------------
# Bug 6: Budget exhaustion flag not checked before LLM calls
# ---------------------------------------------------------------------------
@pytest.mark.asyncio
async def test_bug6_budget_exhaustion_guard():
    """detect_drift, answer_day_one_questions, cluster_into_domains must not call LLM when budget exhausted."""
    from agents.semanticist import Semanticist

    sem = Semanticist.__new__(Semanticist)
    sem.api_key = "fake-key"
    sem.current_model = "openai/gpt-4o-mini"
    from agents.semanticist import ContextWindowBudget
    sem.budget = ContextWindowBudget()
    sem.budget.is_exhausted = True

    llm_mock = AsyncMock()
    llm_mock.ainvoke = AsyncMock(return_value=MagicMock(content='{"drift_detected": false}'))
    sem.llm = llm_mock

    await sem.detect_drift("old docstring", "new purpose")
    await sem.answer_day_one_questions({"top_hubs": []})
    await sem.cluster_into_domains([{"path": "foo.py"}])

    llm_mock.ainvoke.assert_not_called(), (
        "Bug 6: LLM was called despite budget being exhausted"
    )


# ---------------------------------------------------------------------------
# Bug 7: Hydrologist runs after Surveyor exception
# ---------------------------------------------------------------------------
@pytest.mark.asyncio
async def test_bug7_surveyor_abort():
    """When surveyor.run raises, hydrologist.run must NOT be called."""
    with tempfile.TemporaryDirectory() as tmpdir:
        hydro_called = {"called": False}

        def fake_surveyor_run(*args, **kwargs):
            raise RuntimeError("disk error")

        def fake_hydro_run(*args, **kwargs):
            hydro_called["called"] = True

        with patch("agents.surveyor.Surveyor.run", side_effect=fake_surveyor_run), \
             patch("agents.hydrologist.Hydrologist.run", side_effect=fake_hydro_run), \
             patch("agents.archivist.Archivist.log_trace", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.serialize", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.enrich_metadata", return_value=None):
            from orchestrator import Orchestrator
            orch = Orchestrator(tmpdir)

            with pytest.raises(Exception):
                await orch.run_full_pipeline()

    assert not hydro_called["called"], (
        "Bug 7: hydrologist.run was called after surveyor raised an exception"
    )


# ---------------------------------------------------------------------------
# Bug 8: find_implementation tool returns coroutine instead of str
# ---------------------------------------------------------------------------
def test_bug8_tool_return_type():
    """find_implementation tool must return a str, not a coroutine object."""
    import inspect

    with patch("graph.knowledge_graph.KnowledgeGraph.load", return_value=MagicMock(
             module_graph=MagicMock(nodes=MagicMock(return_value=[])),
             lineage_graph=MagicMock()
         )), \
         patch("agents.archivist.Archivist.__init__", lambda self, *a, **kw: None), \
         patch("agents.semanticist.Semanticist.__init__", lambda self, *a, **kw: setattr(self, "llm", None) or setattr(self, "budget", MagicMock()) or setattr(self, "api_key", None)), \
         patch("agents.semantic_index.SemanticIndex.__init__", lambda self, *a, **kw: None), \
         patch("agents.hydrologist.Hydrologist.__init__", lambda self, *a, **kw: None), \
         patch("langchain_openai.ChatOpenAI.__init__", lambda self, **kw: None), \
         patch("langgraph.graph.StateGraph.compile", return_value=MagicMock()):
        from agents.navigator import Navigator
        nav = Navigator("/tmp/test-repo")

    # Get the find_implementation tool
    find_impl = nav.tools.get("find_implementation")
    assert find_impl is not None, "find_implementation tool not found"

    # Call it directly via asyncio.run
    result = asyncio.run(find_impl.ainvoke({"concept": "test"}))

    assert isinstance(result, str), (
        f"Bug 8: find_implementation returned {type(result).__name__}, expected str"
    )


# ---------------------------------------------------------------------------
# Bug 9: Double-quoted dbt ref not matched by regex
# ---------------------------------------------------------------------------
def test_bug9_double_quoted_ref():
    """extract_dbt_refs must handle double-quoted refs like {{ ref("orders") }}."""
    from analyzers.sql_lineage import SQLLineageAnalyzer

    analyzer = SQLLineageAnalyzer()

    # Basic double-quoted ref
    result = analyzer.extract_dbt_refs('{{ ref("orders") }}')
    assert "orders" in result, (
        f"Bug 9: 'orders' not found in result for double-quoted ref: {result}"
    )

    # Whitespace-padded double-quoted ref
    result2 = analyzer.extract_dbt_refs('{{ ref( "orders" ) }}')
    assert "orders" in result2, (
        f"Bug 9: 'orders' not found in result for whitespace-padded ref: {result2}"
    )


# ---------------------------------------------------------------------------
# Bug 10: WebSocket accepts oversized messages without closing
# ---------------------------------------------------------------------------
def test_bug10_websocket_oversized_message():
    """WebSocket must close with code 1009 when message exceeds max size."""
    from fastapi.testclient import TestClient
    from src.ui.api.main import app

    client = TestClient(app)
    oversized_payload = "x" * (100 * 1024)  # 100 KB

    closed_with_error = False
    try:
        with client.websocket_connect("/ws/analysis") as ws:
            ws.send_text(oversized_payload)
            # On unfixed code the server never closes — we just verify the send
            # doesn't raise. The assertion below will fail (no close code).
            import time; time.sleep(0.1)
            close_code = getattr(ws, "close_code", None)
        # If we get here without a 1009 close, the bug exists
        assert close_code == 1009, (
            f"Bug 10: WebSocket close code is {close_code}, expected 1009 (Message Too Big)"
        )
    except Exception:
        # Any exception other than the expected 1009 close means the bug exists
        closed_with_error = True
        assert False, "Bug 10: WebSocket did not close with code 1009 on oversized message"


# ---------------------------------------------------------------------------
# Bug 11: Placeholder output not marked with [LLM DISABLED]
# ---------------------------------------------------------------------------
@pytest.mark.asyncio
async def test_bug11_placeholder_marking():
    """When API key is absent, artifacts must contain [LLM DISABLED] markers."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with patch("agents.surveyor.Surveyor.run", return_value=None), \
             patch("agents.hydrologist.Hydrologist.run", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.serialize", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.enrich_metadata", return_value=None), \
             patch("agents.archivist.Archivist.generate_interactive_graph", return_value=None), \
             patch("agents.archivist.Archivist.log_trace", return_value=None), \
             patch.dict(os.environ, {}, clear=False):
            # Remove API key from env
            os.environ.pop("OPENROUTER_API_KEY", None)

            from orchestrator import Orchestrator
            orch = Orchestrator(tmpdir)
            assert not orch.semanticist.enabled, "Semanticist should be disabled without API key"

            captured = {}
            def fake_onboarding(module_data, day_one_answers):
                captured["day_one_answers"] = day_one_answers
            def fake_codebase(kg):
                captured["kg"] = kg

            orch.archivist.generate_onboarding_brief = fake_onboarding
            orch.archivist.generate_codebase_md = fake_codebase
            orch.archivist.generate_interactive_graph = lambda g: None

            await orch.run_full_pipeline()

        # Check that domain_clusters or day_one_answers contain [LLM DISABLED]
        day_one = captured.get("day_one_answers", {})
        day_one_str = json.dumps(day_one)
        assert "[LLM DISABLED]" in day_one_str, (
            f"Bug 11: day_one_answers does not contain '[LLM DISABLED]': {day_one_str}"
        )


# ---------------------------------------------------------------------------
# Bug 12: Navigator model hardcoded, ignoring NAVIGATOR_MODEL env var
# ---------------------------------------------------------------------------
def test_bug12_model_env_override():
    """Navigator must use NAVIGATOR_MODEL env var when set."""
    with patch.dict(os.environ, {"NAVIGATOR_MODEL": "openai/gpt-4o-mini", "OPENROUTER_API_KEY": "fake-key"}), \
         patch("graph.knowledge_graph.KnowledgeGraph.load", return_value=MagicMock(
             module_graph=MagicMock(nodes=MagicMock(return_value=[])),
             lineage_graph=MagicMock()
         )), \
         patch("agents.archivist.Archivist.__init__", lambda self, *a, **kw: None), \
         patch("agents.semanticist.Semanticist.__init__", lambda self, *a, **kw: setattr(self, "llm", None) or setattr(self, "budget", MagicMock()) or setattr(self, "api_key", None)), \
         patch("agents.semantic_index.SemanticIndex.__init__", lambda self, *a, **kw: None), \
         patch("agents.hydrologist.Hydrologist.__init__", lambda self, *a, **kw: None), \
         patch("langgraph.graph.StateGraph.compile", return_value=MagicMock()):
        from agents.navigator import Navigator
        nav = Navigator("/tmp/test-repo")

    model_name = getattr(nav.llm, "model_name", None) or getattr(nav.llm, "model", None)
    assert model_name == "openai/gpt-4o-mini", (
        f"Bug 12: Navigator used model '{model_name}', expected 'openai/gpt-4o-mini'"
    )


# ---------------------------------------------------------------------------
# Bug 13: Corrupt status file causes unhandled JSONDecodeError
# ---------------------------------------------------------------------------
@pytest.mark.asyncio
async def test_bug13_corrupt_status_file():
    """Corrupt .cartography_status.json must not raise; pipeline must proceed."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create the output dir and write corrupt JSON
        output_dir = os.path.join(tmpdir, os.path.basename(tmpdir))
        os.makedirs(output_dir, exist_ok=True)
        status_path = os.path.join(output_dir, ".cartography_status.json")
        with open(status_path, "w") as f:
            f.write("{")  # invalid JSON

        with patch("agents.surveyor.Surveyor.run", return_value=None), \
             patch("agents.hydrologist.Hydrologist.run", return_value=None), \
             patch("agents.archivist.Archivist.generate_codebase_md", return_value=None), \
             patch("agents.archivist.Archivist.generate_interactive_graph", return_value=None), \
             patch("agents.archivist.Archivist.generate_onboarding_brief", return_value=None), \
             patch("agents.archivist.Archivist.log_trace", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.serialize", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.enrich_metadata", return_value=None):
            from orchestrator import Orchestrator
            orch = Orchestrator(tmpdir)
            # Point archivist output_dir to our temp dir so it reads the corrupt file
            orch.archivist.output_dir = output_dir

            # Must not raise JSONDecodeError
            try:
                await orch.run_full_pipeline()
            except json.JSONDecodeError as e:
                pytest.fail(f"Bug 13: JSONDecodeError raised on corrupt status file: {e}")
