"""Список моделей, доступных вашему ключу."""
import os
from openai import OpenAI

client = OpenAI(base_url="https://api-market1.shop/v1", api_key=os.environ["API_MARKET_KEY"])
for m in sorted(client.models.list(), key=lambda m: m.id):
    print(m.id)
