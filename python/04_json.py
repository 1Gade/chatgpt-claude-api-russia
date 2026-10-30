"""Извлечение данных из текста в JSON (response_format=json_object)."""
import json
import os
from openai import OpenAI

client = OpenAI(base_url="https://api-market1.shop/v1", api_key=os.environ["API_MARKET_KEY"])

reply = client.chat.completions.create(
    model="gpt-6-luna",
    response_format={"type": "json_object"},
    messages=[{
        "role": "user",
        "content": "Извлеки имя, телефон и город в JSON (ключи name, phone, city): "
                   "Здравствуйте, я Анна из Казани, мой номер 8 900 123-45-67",
    }],
)
print(json.loads(reply.choices[0].message.content))
