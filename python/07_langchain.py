"""LangChain с OpenAI-совместимым API.

pip install langchain-openai
"""
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api-market1.shop/v1",
    api_key=os.environ["API_MARKET_KEY"],
    model="gpt-6-luna",
    temperature=0.3,
)
print(llm.invoke("Объясни, что такое RAG, в двух предложениях").content)
