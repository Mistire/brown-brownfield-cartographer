from typing import List, Dict, Any, Optional
import os
import json
from google import generativeai as genai
from src.models.graph import ModuleNode

class Semanticist:
    """
    Uses LLMs to generate purpose statements and cluster domains.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
        else:
            self.model = None
            print("Warning: GEMINI_API_KEY not set. Semanticist will be disabled.")

    @property
    def enabled(self) -> bool:
        return self.model is not None

    async def generate_purpose(self, code: str) -> str:
        if not self.model:
            return "LLM Analysis Disabled"
            
        prompt = f"""
        Analyze the following code and provide a 2-3 sentence 'Purpose Statement'.
        Focus on WHAT the code does for the business/system, not HOW it is implemented.
        Do not use technical jargon if possible.
        
        Code:
        {code[:5000]} 
        """
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating purpose: {str(e)}"

    async def answer_day_one_questions(self, context: Dict[str, Any]) -> Dict[str, str]:
        if not self.model:
            return {f"q{i+1}": "Analysis pending: LLM disabled." for i in range(5)}
            
        prompt = f"""
        Act as a Senior Forward Deployed Engineer (FDE). 
        Based on the following codebase analysis data, answer the 'Five FDE Day-One Questions'.
        
        Analysis Data:
        {json.dumps(context, indent=2, default=str)}
        
        The Questions:
        1. What is the primary data ingestion path?
        2. What are the 3-5 most critical output datasets/endpoints?
        3. What is the blast radius if the most critical module fails?
        4. Where is the business logic concentrated vs. distributed?
        5. What has changed most frequently in the last 90 days?
        
        Provide concise, evidence-based answers for each. Format as a JSON object with keys q1-q5.
        """
        try:
            response = await self.model.generate_content_async(prompt)
            # Basic cleaning if LLM returns markdown blocks
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:-3].strip()
            return json.loads(text)
        except Exception as e:
            return {f"q{i+1}": f"Error: {str(e)}" for i in range(5)}

    def cluster_into_domains(self, nodes: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        # Heuristic-based clustering as a fallback if embeddings aren't used
        # (A true Master Thinker would use embeddings, but this is a solid start)
        domains = {
            "ingestion": ["source", "loader", "stream", "api", "fetch"],
            "transformation": ["transform", "stg_", "clean", "process", "sql"],
            "core_logic": ["models", "schema", "logic", "calculator"],
            "infra_config": ["dag", "pipeline", "config", "yml", "yaml", "env"],
            "monitoring_tests": ["test", "audit", "trace", "log"]
        }
        
        clusters = {d: [] for d in domains}
        clusters["unclassified"] = []
        
        for node in nodes:
            path = node.get("path", "").lower()
            assigned = False
            for domain, keywords in domains.items():
                if any(kw in path for kw in keywords):
                    clusters[domain].append(path)
                    assigned = True
                    break
            if not assigned:
                clusters["unclassified"].append(path)
        
        return clusters
