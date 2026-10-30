"""Генерация картинки gpt-image-2 через API. Сохраняет cat.png в текущую папку."""
import base64
import os
import urllib.request
from openai import OpenAI

client = OpenAI(base_url="https://api-market1.shop/v1", api_key=os.environ["API_MARKET_KEY"])

result = client.images.generate(
    model="gpt-image-2",
    prompt="Минималистичная иллюстрация: кот в очках читает книгу, пастельные цвета",
    size="1024x1024",
)
img = result.data[0]
if img.b64_json:
    open("cat.png", "wb").write(base64.b64decode(img.b64_json))
else:
    urllib.request.urlretrieve(img.url, "cat.png")
print("Сохранено: cat.png")
