# ChatGPT, Claude, Gemini и DeepSeek API из России — примеры кода

Готовые примеры, как обращаться к нейросетям по API из России без VPN и зарубежной карты: Python, Node.js, PHP, cURL, Telegram-бот, LangChain, Claude Code, Cursor, n8n.

Все примеры работают через [API Market](https://api-market1.shop) — OpenAI-совместимый шлюз с оплатой в рублях (СБП, от 10 ₽, без подписки). Меняются только два параметра: адрес и ключ. Остальной код такой же, как в официальной документации OpenAI и Anthropic.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api-market1.shop/v1",   # вместо https://api.openai.com/v1
    api_key="sk-ваш-ключ",
)
reply = client.chat.completions.create(
    model="gpt-6-luna",
    messages=[{"role": "user", "content": "Привет!"}],
)
print(reply.choices[0].message.content)
```

## Быстрый старт

1. Зарегистрируйтесь на [api-market1.shop](https://api-market1.shop) и создайте ключ в разделе «Ключи API» ([пошаговая инструкция](https://api-market1.shop/gaidy/kak-poluchit-api-klyuch-chatgpt-v-rossii)).
2. Сохраните ключ в переменную окружения:
   ```bash
   export API_MARKET_KEY=sk-ваш-ключ        # macOS / Linux
   set API_MARKET_KEY=sk-ваш-ключ           # Windows (cmd)
   $env:API_MARKET_KEY="sk-ваш-ключ"        # Windows (PowerShell)
   ```
3. Запустите любой пример:
   ```bash
   pip install -r python/requirements.txt
   python python/01_chat.py
   ```

## Примеры

| Файл | Что делает |
|---|---|
| [python/01_chat.py](python/01_chat.py) | Первый запрос к GPT |
| [python/02_stream.py](python/02_stream.py) | Потоковый ответ (stream) |
| [python/03_dialog.py](python/03_dialog.py) | Консольный чат с памятью |
| [python/04_json.py](python/04_json.py) | Извлечение данных в JSON |
| [python/05_images.py](python/05_images.py) | Генерация картинок gpt-image-2 |
| [python/06_claude_anthropic_sdk.py](python/06_claude_anthropic_sdk.py) | Claude через библиотеку `anthropic` |
| [python/07_langchain.py](python/07_langchain.py) | LangChain |
| [python/08_list_models.py](python/08_list_models.py) | Список доступных моделей |
| [node/chat.mjs](node/chat.mjs), [node/stream.mjs](node/stream.mjs) | Node.js |
| [php/chat.php](php/chat.php) | PHP через cURL |
| [curl/chat.sh](curl/chat.sh) | Проверка ключа одной командой |
| [telegram-bot/bot.py](telegram-bot/bot.py) | Telegram-бот с нейросетью (aiogram) |
| [integrations/](integrations/README.md) | Claude Code, Cursor, Cline, Continue, n8n, Open WebUI |

## Модели

Название модели передаётся в поле `model`. Актуальные цены в рублях — на странице [цен](https://api-market1.shop/ceny).

| Модель | Для чего |
|---|---|
| [`gpt-6.1-sol`](https://api-market1.shop/modeli/gpt-6.1-sol) | Универсальная модель OpenAI |
| [`gpt-6-astra`](https://api-market1.shop/modeli/gpt-6-astra) | Сложные задачи и рассуждения |
| [`gpt-6-luna`](https://api-market1.shop/modeli/gpt-6-luna) | Быстрая и дешёвая, для ботов и массовых задач |
| [`claude-sonnet-5-5`](https://api-market1.shop/modeli/claude-sonnet-5-5) | Код и тексты, основной выбор для Claude Code |
| [`claude-opus-5-5`](https://api-market1.shop/modeli/claude-opus-5-5) | Самая сильная модель Anthropic |
| [`gemini-4-argon`](https://api-market1.shop/modeli/gemini-4-argon) | Длинный контекст, большие документы |
| [`gemini-3.8-flash`](https://api-market1.shop/modeli/gemini-3.8-flash) | Очень быстрые ответы |
| [`deepseek-v4.1-flash`](https://api-market1.shop/modeli/deepseek-v4.1-flash) | Код за копейки |
| [`grok-4.7`](https://api-market1.shop/modeli/grok-4.7) | Модель xAI |
| [`kimi-k3`](https://api-market1.shop/modeli/kimi-k3), [`glm-5.3`](https://api-market1.shop/modeli/glm-5.3) | Недорогие модели для агентов и кода |
| [`gpt-image-2`](https://api-market1.shop/modeli/gpt-image-2) | Генерация изображений |
| [`seedance-2.0-mini`](https://api-market1.shop/modeli/seedance-2.0-mini) | Генерация видео |

Все модели: [api-market1.shop/modeli](https://api-market1.shop/modeli). Сравнения: [какую нейросеть выбрать](https://api-market1.shop/gaidy/sravnenie-nejrosetej).

## Гайды

- [Как получить API-ключ ChatGPT в России](https://api-market1.shop/gaidy/kak-poluchit-api-klyuch-chatgpt-v-rossii)
- [Claude Code в России](https://api-market1.shop/gaidy/claude-code-v-rossii)
- [Как подключить ChatGPT к Telegram-боту на Python](https://api-market1.shop/gaidy/kak-podklyuchit-gpt-k-telegram-botu)
- [OpenAI в n8n из России](https://api-market1.shop/gaidy/n8n-openai-api-rossiya)
- [LangChain с OpenAI-совместимым API](https://api-market1.shop/gaidy/langchain-openai-rossiya)
- [OpenAI API на Node.js](https://api-market1.shop/gaidy/openai-api-nodejs-primer) · [на PHP](https://api-market1.shop/gaidy/openai-api-php-primer)
- [Генерация картинок через API на Python](https://api-market1.shop/gaidy/generaciya-kartinok-python)
- [Свой ChatGPT для команды: Open WebUI](https://api-market1.shop/gaidy/open-webui-svoj-chatgpt)
- [Что такое токены и как считать стоимость](https://api-market1.shop/gaidy/chto-takoe-tokeny)
- [Ошибки OpenAI API и как их исправить](https://api-market1.shop/gaidy/oshibki-openai-api)
- [ChatGPT Plus или оплата по API: что выгоднее](https://api-market1.shop/gaidy/chatgpt-plus-ili-api)

## Частые ошибки

| Ошибка | Причина |
|---|---|
| `401 Unauthorized` | Ключ скопирован не полностью или удалён |
| `402` / `insufficient quota` | Закончился баланс — пополните в разделе «Кошелёк» |
| `404 model not found` | Опечатка в названии модели — проверьте через `python/08_list_models.py` |
| Claude-библиотека не подключается | Для `anthropic` адрес указывается без `/v1`: `https://api-market1.shop` |

## Безопасность ключа

Не храните ключ в коде и не коммитьте его в Git — используйте переменные окружения или файл `.env` (он уже в `.gitignore`). Если ключ утёк, удалите его в личном кабинете и создайте новый.

## Поддержка

Вопросы — в Telegram: [@ap1market](https://t.me/ap1market). Сайт: [api-market1.shop](https://api-market1.shop).

Лицензия MIT: копируйте примеры в свои проекты.
