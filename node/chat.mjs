// Запрос к GPT из Node.js через OpenAI-совместимый API.
// npm install openai
// API_MARKET_KEY=sk-ваш-ключ node chat.mjs
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api-market1.shop/v1",
  apiKey: process.env.API_MARKET_KEY,
});

const reply = await client.chat.completions.create({
  model: "gpt-6-luna",
  messages: [{ role: "user", content: "Привет! Что ты умеешь?" }],
});
console.log(reply.choices[0].message.content);
