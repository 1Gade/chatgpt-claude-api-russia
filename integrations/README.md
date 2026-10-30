# Подключение готовых программ

Везде, где программа просит «OpenAI API key» и позволяет поменять адрес (Base URL), подходит ключ API Market:

| Параметр | Значение |
|---|---|
| Base URL (OpenAI-формат) | `https://api-market1.shop/v1` |
| Base URL (Anthropic-формат, Claude Code) | `https://api-market1.shop` |
| API Key | ваш ключ `sk-…` из [личного кабинета](https://api-market1.shop) |

## Claude Code

Нужен Node.js 18+.

```bash
npm install -g @anthropic-ai/claude-code

# macOS / Linux
export ANTHROPIC_BASE_URL=https://api-market1.shop
export ANTHROPIC_AUTH_TOKEN=sk-ваш-ключ
export ANTHROPIC_MODEL=claude-sonnet-5-5
claude
```

```powershell
# Windows (PowerShell)
$env:ANTHROPIC_BASE_URL="https://api-market1.shop"
$env:ANTHROPIC_AUTH_TOKEN="sk-ваш-ключ"
$env:ANTHROPIC_MODEL="claude-sonnet-5-5"
claude
```

`claude-sonnet-5-5` — основной выбор, `claude-opus-5-5` — для сложных задач. Подробнее: [Claude Code в России](https://api-market1.shop/gaidy/claude-code-v-rossii).

## Cursor

Settings → Models → OpenAI API Key: вставьте ключ, включите **Override OpenAI Base URL** и укажите `https://api-market1.shop/v1`. Добавьте модель, например `deepseek-v4.1-flash`, и нажмите Verify. Подробнее: [API-ключ для Cursor и VS Code](https://api-market1.shop/api-dlya-cursor).

## Cline (VS Code)

API Provider — **OpenAI Compatible**, Base URL — `https://api-market1.shop/v1`, API Key — ваш ключ, Model ID — например `gpt-6.1-sol`.

## Continue (VS Code)

```yaml
models:
  - name: GPT-6.1 Sol
    provider: openai
    model: gpt-6.1-sol
    apiBase: https://api-market1.shop/v1
    apiKey: sk-ваш-ключ
```

## n8n

Credentials → Add credential → **OpenAI**: API Key — ваш ключ, Base URL — `https://api-market1.shop/v1`. В узле OpenAI Chat Model переключите модель в режим **By ID** и впишите, например, `gpt-6-luna`. Подробнее: [OpenAI в n8n из России](https://api-market1.shop/gaidy/n8n-openai-api-rossiya).

Если сервис (Make, Albato и др.) не позволяет задать Base URL — используйте HTTP-запрос: `POST https://api-market1.shop/v1/chat/completions`, заголовок `Authorization: Bearer sk-…`, тело — как в документации OpenAI.

## Open WebUI — свой ChatGPT на сервере

```bash
docker run -d -p 3000:8080 \
  -e OPENAI_API_BASE_URL=https://api-market1.shop/v1 \
  -e OPENAI_API_KEY=sk-ваш-ключ \
  -v open-webui:/app/backend/data \
  --name open-webui ghcr.io/open-webui/open-webui:main
```

Откройте http://localhost:3000 — все модели появятся в списке. Подробнее: [Open WebUI + API](https://api-market1.shop/gaidy/open-webui-svoj-chatgpt).
