"""Консольный чат с памятью: модель помнит последние 20 сообщений. Пустая строка — выход."""
import os
from openai import OpenAI

client = OpenAI(base_url="https://api-market1.shop/v1", api_key=os.environ["API_MARKET_KEY"])
history = [{"role": "system", "content": "Ты консультант магазина цветов."}]

while True:
    text = input("Вы: ").strip()
    if not text:
        break
    history.append({"role": "user", "content": text})
    reply = client.chat.completions.create(model="gpt-6-luna", messages=history[-20:])
    answer = reply.choices[0].message.content
    history.append({"role": "assistant", "content": answer})
    print("Бот:", answer)
