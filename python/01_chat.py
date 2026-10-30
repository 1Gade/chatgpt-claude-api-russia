"""Первый запрос к GPT через OpenAI-совместимый API из России.

pip install openai
export API_MARKET_KEY=sk-ваш-ключ      (Windows: set API_MARKET_KEY=sk-ваш-ключ)
Ключ можно получить на https://api-market1.shop
"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api-market1.shop/v1",
    api_key=os.environ["API_MARKET_KEY"],
)

reply = client.chat.completions.create(
    model="gpt-6-luna",  # или gpt-6.1-sol, claude-sonnet-5-5, gemini-3.8-flash, deepseek-v4.1-flash...
    messages=[
        {"role": "system", "content": "Ты вежливый помощник. Отвечай кратко."},
        {"role": "user", "content": "Как сварить идеальный рис?"},
    ],
)
print(reply.choices[0].message.content)
