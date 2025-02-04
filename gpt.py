import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="davinci",
    prompt="This is a test",
    temperature=0,
    max_tokens=5,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)

print(response)

response = openai.ChatCompletion.create(
    engine="davinci",
    message = [
        # {"speaker": "Human", "text": "Hello, who are you?"},
        # {"speaker": "AI", "text": "I am an AI created by OpenAI. How can I help you today?"},
        # {"speaker": "Human", "text": "I'd like to cancel my subscription."},
        # {"speaker": "AI", "text": "I'm sorry to hear that. Can you tell me why you want to cancel?"}
        {"speaker": "Human", "text": "Hello, what is python?"},

    ],
    temperature=0,

    max_tokens=5,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)

print(response["choices"][0]["message"]["content"])
