#!/bin/sh
# Проверка ключа одной командой.
# API_MARKET_KEY=sk-ваш-ключ sh chat.sh

curl https://api-market1.shop/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_MARKET_KEY" \
  -d '{"model": "gpt-6-luna", "messages": [{"role": "user", "content": "Hello! Answer in Russian."}]}'
