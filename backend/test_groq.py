from dotenv import load_dotenv
load_dotenv()

import os
from app.services.groq_chat import groq_chat

print("API KEY:", os.getenv("GROQ_API_KEY"))

messages = [{"role": "user", "content": "Hello"}]
print(groq_chat(messages))
