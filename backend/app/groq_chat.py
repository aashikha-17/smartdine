import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def groq_chat(messages):
    url = "https://api.groq.com/openai/v1/chat/completions"

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 300
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    r = requests.post(url, json=payload, headers=headers)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
