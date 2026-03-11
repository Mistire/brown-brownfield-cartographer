from typing import List, Dict, Any, Optional
import os
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

    def cluster_into_domains(self, nodes: List[ModuleNode]) -> Dict[str, List[str]]:
        # TODO: Implement embedding-based clustering
        # For now, return a placeholder
        return {"utility": [node.path for node in nodes]}
