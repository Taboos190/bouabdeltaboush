<?php
// proxy.php

header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");

$data = json_decode(file_get_contents("php://input"), true);

$apiKey = $data["apiKey"];
$prompt = $data["prompt"];

$payload = [
    "model" => "gpt-3.5-turbo",
    "messages" => [
        ["role" => "user", "content" => $prompt]
    ]
];

$ch = curl_init("https://api.openai.com/v1/chat/completions");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "Authorization: Bearer $apiKey"
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
