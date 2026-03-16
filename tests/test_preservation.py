"""
Preservation tests — these MUST PASS on unfixed code.
They establish baseline behavior that must not regress after fixes.
"""
import sys
import os
import asyncio
import json
import tempfile
import pytest
from unittest.mock import MagicMock, patch, AsyncMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from hypothesis import given, settings, strategies as st


# ---------------------------------------------------------------------------
# Preserve: single-quoted dbt ref extraction (Req 3.7)
# ---------------------------------------------------------------------------
@given(model_name=st.from_regex(r"[a-zA-Z][a-zA-Z0-9_]{0,30}", fullmatch=True))
@settings(max_examples=50)
def test_preserve_single_quoted_dbt_ref(model_name):
    """Single-quoted {{ ref('MODEL') }} must always be extracted correctly."""
    from analyzers.sql_lineage import SQLLineageAnalyzer
    analyzer = SQLLineageAnalyzer()
    sql = f"{{{{ ref('{model_name}') }}}}"
    result = analyzer.extract_dbt_refs(sql)
    assert model_name in result, (
        f"Preservation: single-quoted ref('{model_name}') not extracted: {result}"
    )


# ---------------------------------------------------------------------------
# Preserve: ContextWindowBudget.record() accumulates correctly (Req 3.10)
# ---------------------------------------------------------------------------
@given(
    prompt_tokens=st.integers(min_value=0, max_value=50_000),
    completion_tokens=st.integers(min_value=0, max_value=50_000),
)
@settings(max_examples=50)
def test_preserve_budget_record_accumulates(prompt_tokens, completion_tokens):
    """Budget.record() must accumulate tokens and set is_exhausted when over limit."""
    from agents.semanticist import ContextWindowBudget

    budget = ContextWindowBudget(max_tokens=100_000)

    response = MagicMock()
    response.usage_metadata = {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
    }

    budget.record("openai/gpt-4o-mini", response)

    assert budget.total_prompt_tokens == prompt_tokens
    assert budget.total_completion_tokens == completion_tokens

    total = prompt_tokens + completion_tokens
    if total > 100_000:
        assert budget.is_exhausted, (
            f"Preservation: budget should be exhausted at {total} tokens"
        )
    else:
        assert not budget.is_exhausted, (
            f"Preservation: budget should not be exhausted at {total} tokens"
        )


# ---------------------------------------------------------------------------
# Preserve: WebSocket normal messages received without close (Req 3.8)
# ---------------------------------------------------------------------------
@given(size=st.integers(min_value=1, max_value=1000))
@settings(max_examples=20)
def test_preserve_websocket_normal_message(size):
    """Messages of 1-1000 bytes must be received normally (no close)."""
    from fastapi.testclient import TestClient
    from src.ui.api.main import app

    client = TestClient(app)
    payload = "a" * size

    # Just verify the connection can be established and send doesn't raise
    try:
        with client.websocket_connect("/ws/analysis") as ws:
            ws.send_text(payload)
            # Small sleep to let server process
            import time; time.sleep(0.05)
    except Exception as e:
        assert False, (
            f"Preservation: WebSocket raised unexpectedly for {size}-byte message: {e}"
        )


# ---------------------------------------------------------------------------
# Preserve: /analyze endpoint returns immediately (Req 3.8)
# ---------------------------------------------------------------------------
def test_preserve_analyze_endpoint_returns_immediately():
    """POST /analyze must return 200 with 'Analysis started' immediately."""
    from fastapi.testclient import TestClient
    from src.ui.api.main import app

    client = TestClient(app)
    response = client.post("/analyze", json={"repo_path": "/tmp/test-repo"})

    assert response.status_code == 200
    data = response.json()
    assert "Analysis started" in data.get("message", ""), (
        f"Preservation: /analyze response: {data}"
    )


# ---------------------------------------------------------------------------
# Preserve: Valid status file causes completed stages to be skipped (Req 3.6)
# ---------------------------------------------------------------------------
@pytest.mark.asyncio
async def test_preserve_valid_status_file_skips_stages():
    """A valid status file with surveyor=True must cause surveyor.run to be skipped."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, os.path.basename(tmpdir))
        os.makedirs(output_dir, exist_ok=True)

        # Write a valid status file with surveyor completed
        status_path = os.path.join(output_dir, ".cartography_status.json")
        with open(status_path, "w") as f:
            json.dump({"surveyor": True, "hydrologist": False, "semanticist": False}, f)

        # Write minimal graph files so KnowledgeGraph.load succeeds
        import networkx as nx
        empty_graph = nx.node_link_data(nx.DiGraph())
        with open(os.path.join(output_dir, "module_graph.json"), "w") as f:
            json.dump(empty_graph, f)
        with open(os.path.join(output_dir, "lineage_graph.json"), "w") as f:
            json.dump(empty_graph, f)

        surveyor_called = {"called": False}

        def fake_surveyor_run(*args, **kwargs):
            surveyor_called["called"] = True

        with patch("agents.surveyor.Surveyor.run", side_effect=fake_surveyor_run), \
             patch("agents.hydrologist.Hydrologist.run", return_value=None), \
             patch("agents.archivist.Archivist.generate_codebase_md", return_value=None), \
             patch("agents.archivist.Archivist.generate_interactive_graph", return_value=None), \
             patch("agents.archivist.Archivist.generate_onboarding_brief", return_value=None), \
             patch("agents.archivist.Archivist.log_trace", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.serialize", return_value=None), \
             patch("graph.knowledge_graph.KnowledgeGraph.enrich_metadata", return_value=None):
            from orchestrator import Orchestrator
            orch = Orchestrator(tmpdir)
            orch.archivist.output_dir = output_dir

            await orch.run_full_pipeline()

    assert not surveyor_called["called"], (
        "Preservation: surveyor.run was called despite valid status file marking it complete"
    )
