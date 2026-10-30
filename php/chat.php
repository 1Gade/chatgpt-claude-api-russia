<?php
// Запрос к ChatGPT API из PHP через cURL, без библиотек.
// API_MARKET_KEY=sk-ваш-ключ php chat.php

$ch = curl_init("https://api-market1.shop/v1/chat/completions");
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
        "Authorization: Bearer " . getenv("API_MARKET_KEY"),
    ],
    CURLOPT_POSTFIELDS => json_encode([
        "model" => "gpt-6-luna",
        "messages" => [["role" => "user", "content" => "Привет! Что ты умеешь?"]],
    ]),
]);
$data = json_decode(curl_exec($ch), true);
echo $data["choices"][0]["message"]["content"] ?? json_encode($data, JSON_UNESCAPED_UNICODE), PHP_EOL;
