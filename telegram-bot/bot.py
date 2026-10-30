"""Telegram-бот с нейросетью: отвечает на любое сообщение и помнит контекст диалога.

pip install aiogram openai
export API_MARKET_KEY=sk-ваш-ключ
export BOT_TOKEN=токен-от-BotFather
python bot.py
"""
import asyncio
import os
from collections import defaultdict, deque

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from openai import AsyncOpenAI

ai = AsyncOpenAI(base_url="https://api-market1.shop/v1", api_key=os.environ["API_MARKET_KEY"])
bot = Bot(os.environ["BOT_TOKEN"])
dp = Dispatcher()

SYSTEM = "Ты дружелюбный помощник. Отвечай по-русски, кратко и по делу."
history = defaultdict(lambda: deque(maxlen=12))  # последние 12 сообщений на каждого пользователя


@dp.message(CommandStart())
async def start(message: types.Message):
    history.pop(message.chat.id, None)
    await message.answer("Привет! Напишите вопрос — я отвечу.")


@dp.message()
async def answer(message: types.Message):
    if not message.text:
        return
    h = history[message.chat.id]
    h.append({"role": "user", "content": message.text})
    reply = await ai.chat.completions.create(
        model="gpt-6-luna",
        messages=[{"role": "system", "content": SYSTEM}, *h],
    )
    text = reply.choices[0].message.content
    h.append({"role": "assistant", "content": text})
    await message.answer(text)


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
