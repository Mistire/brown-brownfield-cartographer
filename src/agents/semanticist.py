from typing import List, Dict, Any, Optional
import os
import json
from dotenv import load_dotenv

load_dotenv()
from tenacity import retry, stop_after_attempt
from langchain_openai import ChatOpenAI
from src.models.graph import ModuleNode

class ContextWindowBudget:
    """Tracks token usage and cost for LLM operations."""
    def __init__(self):
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_cost = 0.0

    def record(self, response: Any):
        if hasattr(response, 'usage_metadata'):
             self.total_prompt_tokens += response.usage_metadata.get('prompt_tokens', 0)
             self.total_completion_tokens += response.usage_metadata.get('completion_tokens', 0)

class Semanticist:
    """
    Uses LLMs (via OpenRouter) to generate purpose statements, cluster domains, and detect drift.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.model_name = os.getenv("LLM_MODEL", "qwen/qwen-2.5-72b-instruct:free")
        self.budget = ContextWindowBudget()
        
        if self.api_key:
            self.llm = ChatOpenAI(
                model=self.model_name,
                openai_api_key=self.api_key,
                openai_api_base=os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1"),
                temperature=0.1
            )
        else:
            self.llm = None
            print("Warning: OPENROUTER_API_KEY not set. Semanticist will be disabled.")

    @property
    def enabled(self) -> bool:
        return self.llm is not None

    async def generate_purpose(self, code: str) -> str:
        if not self.llm:
            return "LLM Analysis Disabled"
            
        @retry(stop=stop_after_attempt(3))
        async def _invoke():
            prompt = f"""
            Analyze the following code and provide a 2-3 sentence 'Purpose Statement'.
            Focus on WHAT the code does for the business/system, not HOW it is implemented.
            
            Return JSON: {{"purpose": str, "confidence": 0.0-1.0}}
            
            Code:
            {code[:4000]} 
            """
            response = await self.llm.ainvoke(prompt)
            self.budget.record(response)
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
        Compare this CODE DOCSTRING with the ACTUAL IMPLEMENTATION PURPOSE.
        Docstring: {docstring}
        Actual Purpose: {purpose}
        
        Is there a significant discrepancy (drift)? 
        Return JSON: {{"drift_detected": bool, "mismatch_reason": str, "score": 0.0-1.0, "confidence": 0.0-1.0}}
        """
        try:
            response = await self.llm.ainvoke(prompt)
            self.budget.record(response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            return json.loads(text)
        except:
            return {"drift_detected": False, "score": 0.0, "confidence": 0.0}

    async def answer_day_one_questions(self, context: Dict[str, Any]) -> Dict[str, str]:
        if not self.llm:
            return {f"q{i+1}": "Analysis pending: LLM disabled." for i in range(5)}
            
        prompt = f"""
        Answer the 'Five FDE Day-One Questions' based on this data: {json.dumps(context)}.
        1. Ingestion path? 2. Critical outputs? 3. Blast radius? 4. Logic distribution? 5. Change hotspots?
        Return only a JSON object with keys q1-q5.
        """
        try:
            response = await self.llm.ainvoke(prompt)
            self.budget.record(response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            return json.loads(text)
        except Exception as e:
            return {f"q{i+1}": f"Error: {str(e)}" for i in range(5)}

    async def cluster_into_domains(self, nodes: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """Uses LLM to categorize modules into domains (ingestion, core, etc)."""
        if not self.llm:
            return {"unclassified": [m.get("path") for m in nodes]}
            
        paths = [m.get("path") for m in nodes if m.get("path")]
        
        prompt = f"""
        Categorize these file paths into high-level business domains (e.g., 'ingestion', 'transformation', 'infra', 'logic').
        Paths: {paths}
        
        Return ONLY a JSON object: {{"domain_name": ["path1", "path2"]}}
        """
        try:
            response = await self.llm.ainvoke(prompt)
            self.budget.record(response)
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            return json.loads(text)
        except:
            return {"unclassified": paths}
