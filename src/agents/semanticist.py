from typing import List, Dict, Any, Optional, Tuple
import os
import json
from dotenv import load_dotenv

load_dotenv()
from tenacity import retry, stop_after_attempt
from langchain_openai import ChatOpenAI
from models.graph import ModuleNode

# ---------------------------------------------------------------------------
# Multi-model registry — ordered from smallest to largest context window.
# Each entry: (model_id, context_tokens, supports_tools)
# The router picks the cheapest (smallest context) model whose window fits
# the estimated prompt token count, then falls back to larger ones.
# All models here are free via OpenRouter as of 2025.
# ---------------------------------------------------------------------------
MODEL_REGISTRY: List[Tuple[str, int, bool]] = [
    # model_id                                          ctx_tokens  tools
    ("mistralai/mistral-small-3.1-24b-instruct:free",   32_768,     True),
    ("meta-llama/llama-3.1-8b-instruct:free",           131_072,    True),
    ("mistralai/mistral-7b-instruct:free",              32_768,     False),
    ("meta-llama/llama-3.3-70b-instruct:free",          131_072,    True),
    ("qwen/qwen-2.5-72b-instruct:free",                 131_072,    True),
    ("deepseek/deepseek-r1-distill-llama-70b:free",     131_072,    False),
    ("google/gemma-3-27b-it:free",                      131_072,    False),
    ("microsoft/phi-4-reasoning-plus:free",             131_072,    False),
    ("qwen/qwen3-235b-a22b:free",                       131_072,    True),
]

# Safety margin: keep 20 % of context for the completion
_SAFETY_FACTOR = 0.80


def _estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token (GPT-style)."""
    return max(1, len(text) // 4)


def select_model(estimated_prompt_tokens: int, require_tools: bool = False) -> str:
    """
    Return the model_id of the smallest-context free model whose window
    comfortably fits `estimated_prompt_tokens`.  Falls back to the largest
    model if nothing fits.
    """
    candidates = [
        (mid, ctx) for mid, ctx, tools in MODEL_REGISTRY
        if (not require_tools or tools) and int(ctx * _SAFETY_FACTOR) >= estimated_prompt_tokens
    ]
    if candidates:
        # Pick the one with the smallest sufficient context window
        return min(candidates, key=lambda x: x[1])[0]
    # Nothing fits — use the largest available model as last resort
    pool = [(mid, ctx) for mid, ctx, tools in MODEL_REGISTRY if not require_tools or tools]
    return max(pool, key=lambda x: x[1])[0]



class ContextWindowBudget:
    """Tracks token usage and cost for LLM operations."""
    PRICING = {m: (0.0, 0.0) for m, _, _ in MODEL_REGISTRY}
    PRICING.update({
        "openai/gpt-4o": (5.0, 15.0),
        "openai/gpt-4o-mini": (0.15, 0.6),
    })

    def __init__(self, max_tokens: int = 500_000):
        self.max_tokens = max_tokens
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost = 0.0
        self.is_exhausted = False

    def record(self, model_name: str, response: Any):
        if hasattr(response, 'usage_metadata'):
            p_tokens = response.usage_metadata.get('prompt_tokens', 0)
            c_tokens = response.usage_metadata.get('completion_tokens', 0)
            self.total_prompt_tokens += p_tokens
            self.total_completion_tokens += c_tokens

            p_rate, c_rate = self.PRICING.get(model_name, (0.0, 0.0))
            self.total_cost += (p_tokens / 1_000_000) * p_rate
            self.total_cost += (c_tokens / 1_000_000) * c_rate

            if (self.total_prompt_tokens + self.total_completion_tokens) > self.max_tokens:
                self.is_exhausted = True

    def get_summary(self) -> Dict[str, Any]:
        return {
            "prompt_tokens": self.total_prompt_tokens,
            "completion_tokens": self.total_completion_tokens,
            "total_tokens": self.total_prompt_tokens + self.total_completion_tokens,
            "limit": self.max_tokens,
            "is_exhausted": self.is_exhausted,
            "estimated_cost_usd": float(f"{self.total_cost:.6f}"),
        }


class Semanticist:
    """
    Uses LLMs (via OpenRouter) to generate purpose statements, cluster domains,
    and detect drift.  Model selection is automatic: each call estimates its
    prompt token count and routes to the smallest free model whose context
    window fits, falling back to larger models as needed.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.budget = ContextWindowBudget()
        self._llm_cache: Dict[str, ChatOpenAI] = {}

        if not self.api_key:
            self.llm = None
            print("Warning: OPENROUTER_API_KEY not set. Semanticist will be disabled.")
        else:
            # Pre-warm with the default low-cost model
            default = os.getenv("LLM_LOW_MODEL", "mistralai/mistral-small-3.1-24b-instruct:free")
            self.llm = self._get_llm(default)
            self.current_model = default

    def _get_llm(self, model: str) -> ChatOpenAI:
        """Return a cached ChatOpenAI instance for the given model."""
        if model not in self._llm_cache:
            self._llm_cache[model] = ChatOpenAI(
                model=model,
                openai_api_key=self.api_key,
                openai_api_base=os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1"),
                temperature=0.1,
            )
        return self._llm_cache[model]

    def _llm_for(self, prompt: str, require_tools: bool = False) -> Tuple[ChatOpenAI, str]:
        """Pick the right model for this prompt and return (llm, model_id)."""
        tokens = _estimate_tokens(prompt)
        model_id = select_model(tokens, require_tools=require_tools)
        return self._get_llm(model_id), model_id

    @property
    def enabled(self) -> bool:
        return self.llm is not None


    async def generate_purpose(self, code: str, size: int = 0) -> tuple[str, float]:
        if not self.llm or self.budget.is_exhausted:
            return "Analysis Limitation (Budget/Disabled)", 0.0

        # Truncate code to a safe length before building the prompt
        max_code_chars = 48_000  # ~12k tokens — leaves room for instructions
        truncated = code[:max_code_chars]

        prompt = (
            "You are a Master Software Architect performing context extraction for a brownfield project.\n"
            "Analyze the following code and provide a 2-3 sentence 'Purpose Statement'.\n\n"
            "RULES:\n"
            "1. Focus on WHAT the code does for the business/system, not HOW it is implemented.\n"
            "2. Ground your answer in implementation evidence.\n"
            "3. IGNORE the docstrings.\n\n"
            f'Return JSON: {{"purpose": str, "confidence": 0.0-1.0}}\n\nCode:\n{truncated}'
        )

        llm, model_id = self._llm_for(prompt)

        @retry(stop=stop_after_attempt(3))
        async def _invoke():
            response = await llm.ainvoke(prompt)
            self.budget.record(model_id, response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            return json.loads(text)

        try:
            res = await _invoke()
            return res.get("purpose", "LLM Analysis Failed"), res.get("confidence", 0.5)
        except Exception as e:
            return f"Error: {str(e)}", 0.0

    async def detect_drift(self, docstring: Optional[str], purpose: str) -> Dict[str, Any]:
        """Compares actual docstring with LLM-generated purpose to detect drift."""
        if not self.llm or not docstring:
            return {"drift_detected": False, "score": 0.0, "confidence": 0.0}
        if self.budget.is_exhausted:
            return {"drift_detected": False, "score": 0.0, "confidence": 0.0, "inference_type": "Budget Exhausted"}

        prompt = (
            "You are a Master Software Architect detecting documentation drift.\n"
            "Compare the following CODE DOCSTRING with the ACTUAL IMPLEMENTATION PURPOSE.\n\n"
            f"Docstring: {docstring}\n"
            f"Actual Purpose (from code analysis): {purpose}\n\n"
            "Is there a significant discrepancy or 'drift' where the docstring describes behavior "
            "that is no longer present or is fundamentally different?\n\n"
            'Return JSON: {"drift_detected": bool, "mismatch_reason": str, "score": 0.0-1.0, "confidence": 0.0-1.0}'
        )
        llm, model_id = self._llm_for(prompt)
        try:
            response = await llm.ainvoke(prompt)
            self.budget.record(model_id, response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            data = json.loads(text)
            data["inference_type"] = "LLM Inference"
            return data
        except Exception as e:
            return {"drift_detected": False, "score": 0.0, "confidence": 0.0,
                    "inference_type": "LLM Inference", "error": str(e)}

    async def answer_day_one_questions(self, context: Dict[str, Any]) -> Dict[str, str]:
        if not self.llm:
            return {f"q{i+1}": "Analysis pending: LLM disabled." for i in range(5)}
        if self.budget.is_exhausted:
            return {f"q{i+1}": "Budget exhausted." for i in range(5)}

        context_str = json.dumps(context, indent=2)
        prompt = (
            "You are a Senior FDE synthesizing an Onboarding Brief for a new engineer.\n"
            "Answer the 'Five FDE Day-One Questions' based on the following architectural evidence:\n\n"
            f"{context_str}\n\n"
            "QUESTIONS:\n"
            "1. What is the primary data ingestion path? (Identify specific files/sources)\n"
            "2. What are the 3-5 most critical output datasets/endpoints? (Identify sinks)\n"
            "3. What is the blast radius if the most critical module fails? (Based on PageRank and edges)\n"
            "4. Where is the business logic concentrated vs. distributed? (Semantic clusters)\n"
            "5. What has changed most frequently in the last 90 days? (Git velocity hotspots)\n\n"
            "Rules:\n- Be technical and precise.\n- Cite specific file paths.\n"
            "- If unsure, state 'Analysis inconclusive'.\n\n"
            "Return only a JSON object with keys q1-q5."
        )
        llm, model_id = self._llm_for(prompt)
        try:
            response = await llm.ainvoke(prompt)
            self.budget.record(model_id, response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            data = json.loads(text)
            return {k: f"{v} (Inference: LLM, Model: {model_id})" for k, v in data.items()}
        except Exception as e:
            return {f"q{i+1}": f"Error: {str(e)}" for i in range(5)}

    async def cluster_into_domains(self, nodes: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """Uses LLM to categorize modules into domains (ingestion, core, etc)."""
        if not self.llm:
            return {"unclassified": [str(m.get("path", "")) for m in nodes]}
        if self.budget.is_exhausted:
            return {"unclassified": [str(m.get("path", "")) for m in nodes]}

        paths = [str(m.get("path", "")) for m in nodes if m.get("path")]
        prompt = (
            "Categorize these file paths into high-level business domains "
            "(e.g., 'ingestion', 'transformation', 'infra', 'logic').\n"
            f"Paths: {paths}\n\n"
            'Return ONLY a JSON object: {"domain_name": ["path1", "path2"]}'
        )
        llm, model_id = self._llm_for(prompt)
        try:
            response = await llm.ainvoke(prompt)
            self.budget.record(model_id, response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            data = json.loads(text)
            return {k: [str(v) for v in vs] for k, vs in data.items()}
        except Exception:
            return {"unclassified": paths}

    async def get_embeddings(self, text: str) -> List[float]:
        """Generates embeddings. Falls back to a deterministic hash-based vector."""
        if not self.api_key:
            return []

        _emb_model = os.getenv("EMBEDDING_MODEL", "").strip()

        # If no embedding model is configured, skip the API call entirely and
        # use the hash-based fallback — OpenRouter doesn't proxy /embeddings
        # for most models, so attempting it just produces noisy 400 errors.
        if _emb_model:
            from langchain_openai import OpenAIEmbeddings
            try:
                embeddings = OpenAIEmbeddings(
                    model=_emb_model,
                    openai_api_key=self.api_key,
                    openai_api_base=os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1"),
                )
                return await embeddings.aembed_query(text)
            except Exception as e:
                print(f"Embedding API failed ({_emb_model}): {e} — using hash fallback")

        # Deterministic hash-based non-zero vector (consistent across runs)
        import hashlib
        import numpy as np
        h = int(hashlib.md5(text.encode()).hexdigest(), 16)
        rng = np.random.default_rng(h % (2**32))
        return rng.standard_normal(1536).tolist()
