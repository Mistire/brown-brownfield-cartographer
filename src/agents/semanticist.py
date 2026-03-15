from typing import List, Dict, Any, Optional
import os
import json
from dotenv import load_dotenv

load_dotenv()
from tenacity import retry, stop_after_attempt
from langchain_openai import ChatOpenAI
from models.graph import ModuleNode

class ContextWindowBudget:
    """Tracks token usage and cost for LLM operations with model tiering."""
    PRICING = {
        "openai/gpt-4o": (5.0, 15.0),
        "openai/gpt-4o-mini": (0.15, 0.6),
        "qwen/qwen-2.5-72b-instruct:free": (0.0, 0.0),
    }

    def __init__(self, max_tokens: int = 100_000):
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
             
             p_rate, c_rate = self.PRICING.get(model_name, (0.01, 0.03))
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
            "estimated_cost_usd": float(f"{self.total_cost:.6f}")
        }

class Semanticist:
    """
    Uses LLMs (via OpenRouter) to generate purpose statements, cluster domains, and detect drift.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.high_model = os.getenv("LLM_HIGH_MODEL", "openai/gpt-4o")
        self.low_model = os.getenv("LLM_LOW_MODEL", "openai/gpt-4o-mini")
        self.budget = ContextWindowBudget()
        self.current_model = self.low_model
        
        if self.api_key:
            self._init_llm(self.low_model)
        else:
            self.llm = None
            print("Warning: OPENROUTER_API_KEY not set. Semanticist will be disabled.")

    def _init_llm(self, model: str):
        self.llm = ChatOpenAI(
            model=model,
            openai_api_key=self.api_key,
            openai_api_base=os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1"),
            temperature=0.1
        )
        self.current_model = model

    @property
    def enabled(self) -> bool:
        return self.llm is not None

    async def generate_purpose(self, code: str, size: int = 0) -> tuple[str, float]:
        if not self.llm or self.budget.is_exhausted:
            return "Analysis Limitation (Budget/Disabled)", 0.0
            
        # Tiering: Use high model for files > 50KB or complex files
        target_model = self.high_model if size > 50000 else self.low_model
        if self.current_model != target_model:
            self._init_llm(target_model)

        @retry(stop=stop_after_attempt(3))
        async def _invoke():
            prompt = f"""
            You are a Master Software Architect performing context extraction for a brownfield project.
            Analyze the following code and provide a 2-3 sentence 'Purpose Statement'.
            
            RULES:
            1. Focus on WHAT the code does for the business/system, not HOW it is implemented.
            2. Ground your answer in implementation evidence.
            3. IGNORE the docstrings.
            
            Return JSON: {{"purpose": str, "confidence": 0.0-1.0}}
            
            Code:
            {code[:12000] if target_model == self.high_model else code[:6000]} 
            """
            response = await self.llm.ainvoke(prompt)
            self.budget.record(self.current_model, response)
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
            
        prompt = f"""
        You are a Master Software Architect detecting documentation drift.
        Compare the following CODE DOCSTRING with the ACTUAL IMPLEMENTATION PURPOSE.
        
        Docstring: {docstring}
        Actual Purpose (from code analysis): {purpose}
        
        Is there a significant discrepancy or 'drift' where the docstring describes behavior that is no longer present or is fundamentally different?
        
        Return JSON: {{"drift_detected": bool, "mismatch_reason": str, "score": 0.0-1.0, "confidence": 0.0-1.0}}
        """
        try:
            response = await self.llm.ainvoke(prompt)
            self.budget.record(self.current_model, response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            data = json.loads(text)
            data["inference_type"] = "LLM Inference"
            return data
        except:
            return {"drift_detected": False, "score": 0.0, "confidence": 0.0, "inference_type": "LLM Inference"}

    async def answer_day_one_questions(self, context: Dict[str, Any]) -> Dict[str, str]:
        if not self.llm:
            return {f"q{i+1}": "Analysis pending: LLM disabled." for i in range(5)}
            
        prompt = f"""
        You are a Senior FDE synthesizing an Onboarding Brief for a new engineer.
        Answer the 'Five FDE Day-One Questions' based on the following architectural evidence:
        
        {json.dumps(context, indent=2)}
        
        QUESTIONS:
        1. What is the primary data ingestion path? (Identify specific files/sources)
        2. What are the 3-5 most critical output datasets/endpoints? (Identify sinks)
        3. What is the blast radius if the most critical module fails? (Based on PageRank and edges)
        4. Where is the business logic concentrated vs. distributed? (Semantic clusters)
        5. What has changed most frequently in the last 90 days? (Git velocity hotspots)
        
        Rules:
        - Be technical and precise.
        - Cite specific file paths from the provided context.
        - If unsure, state 'Analysis inconclusive'.
        
        Return only a JSON object with keys q1-q5.
        """
        try:
            response = await self.llm.ainvoke(prompt)
            self.budget.record(self.current_model, response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            data = json.loads(text)
            # Standardize Day-One results with inference markers
            return {k: f"{v} (Inference: LLM)" for k, v in data.items()}
        except Exception as e:
            return {f"q{i+1}": f"Error: {str(e)}" for i in range(5)}

    async def cluster_into_domains(self, nodes: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """Uses LLM to categorize modules into domains (ingestion, core, etc)."""
        if not self.llm:
            return {"unclassified": [str(m.get("path", "")) for m in nodes]}
            
        paths = [str(m.get("path", "")) for m in nodes if m.get("path")]
        
        prompt = f"""
        Categorize these file paths into high-level business domains (e.g., 'ingestion', 'transformation', 'infra', 'logic').
        Paths: {paths}
        
        Return ONLY a JSON object: {{"domain_name": ["path1", "path2"]}}
        """
        try:
            response = await self.llm.ainvoke(prompt)
            self.budget.record(self.current_model, response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            data = json.loads(text)
            # Ensure all values are list of strings
            return {k: [str(v) for v in vs] for k, vs in data.items()}
        except:
            return {"unclassified": paths}

    async def get_embeddings(self, text: str) -> List[float]:
        """Generates embeddings for a given text using the LLM's embedding model if available."""
        # For OpenRouter, we might need a specific embedding model or use a generic one.
        # However, since we are using langchain-openai, we can leverage their embedding interface
        # if the provider supports it. For now, we'll use a mocked/simpler approach or 
        # a dedicated embedding model if configured.
        
        # NOTE: OpenRouter doesn't always support /embeddings in the same way.
        # A more robust FDE approach is to use a local or standard embedding model.
        # For this challenge, we'll try to use the OpenAI compatible embeddings if provided.
        
        if not self.api_key:
            return []

        from langchain_openai import OpenAIEmbeddings
        try:
            embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small", # Default choice
                openai_api_key=self.api_key,
                openai_api_base=os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
            )
            return await embeddings.aembed_query(text)
        except Exception as e:
            print(f"Embedding failed: {e}")
            # Fallback: return a zero vector of standard size (1536) for consistency
            import numpy as np
            return np.zeros(1536).tolist()
