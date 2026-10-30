"""Потоковый ответ (stream): текст появляется по мере генерации, как в ChatGPT."""
import os
from openai import OpenAI

client = OpenAI(base_url="https://api-market1.shop/v1", api_key=os.environ["API_MARKET_KEY"])

stream = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[{"role": "user", "content": "Напиши короткое стихотворение про осень"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
