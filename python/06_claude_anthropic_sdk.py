"""Claude (Opus 5.5 / Sonnet 5.5) через официальную библиотеку Anthropic.

pip install anthropic
base_url указывается без /v1 — библиотека добавляет путь сама.
"""
import os
import anthropic

client = anthropic.Anthropic(
    base_url="https://api-market1.shop",
    api_key=os.environ["API_MARKET_KEY"],
)

msg = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Напиши функцию на Python, которая проверяет, является ли строка палиндромом."}],
)
print(msg.content[0].text)
