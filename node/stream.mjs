// Потоковый ответ в Node.js.
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api-market1.shop/v1",
  apiKey: process.env.API_MARKET_KEY,
});

const stream = await client.chat.completions.create({
  model: "gpt-6-luna",
  messages: [{ role: "user", content: "Расскажи короткую сказку про робота" }],
  stream: true,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
console.log();
