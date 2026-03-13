import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

async def verify_context_injection():
    project_name = "jaffle_shop"
    codebase_md_path = f".cartography/{project_name}/CODEBASE.md"
    
    if not os.path.exists(codebase_md_path):
        print(f"Error: {codebase_md_path} not found. Run analysis first.")
        return

    with open(codebase_md_path, "r") as f:
        context = f.read()

    print("--- Priming AI Agent with CODEBASE.md ---")
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY not set.")
        return

    llm = ChatOpenAI(
        model=os.getenv("LLM_MODEL", "qwen/qwen-2.5-72b-instruct:free"),
        openai_api_key=api_key,
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0
    )

    # The architecture-specific question
    query = "Based on the CODEBASE.md, which modules are part of a circular dependency and what risk does this pose?"
    
    messages = [
        SystemMessage(content=f"You are a senior architect. Use the following codebase context to answer questions:\n\n{context}"),
        HumanMessage(content=query)
    ]

    print(f"Query: {query}")
    print("Agent is thinking...")
    
    response = await llm.ainvoke(messages)
    
    print("\n--- AI Agent Response ---")
    print(response.content)
    print("\nVerification Complete.")

if __name__ == "__main__":
    asyncio.run(verify_context_injection())
