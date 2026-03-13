from typing import List, Dict, Any, Optional
import os
import json
from langchain_openai import ChatOpenAI
from src.models.graph import ModuleNode

class Semanticist:
    """
    Uses LLMs (via OpenRouter) to generate purpose statements and cluster domains.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if self.api_key:
            self.llm = ChatOpenAI(
                model="liquid/lfm-7b-creative", # Default free model
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
            
        prompt = f"""
        Analyze the following code and provide a 2-3 sentence 'Purpose Statement'.
        Focus on WHAT the code does for the business/system, not HOW it is implemented.
        Code:
        {code[:4000]} 
        """
        try:
            response = await self.llm.ainvoke(prompt)
            return response.content.strip()
        except Exception as e:
            return f"Error generating purpose: {str(e)}"

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
            text = response.content.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
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
