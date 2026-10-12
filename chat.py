import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

config = types.GenerateContentConfig(
    system_instruction="You are a concise, helpful tutor. Keep answers under two sentences."
)

messages_history = []

def send_chat_message(user_input: str) -> str:
    messages_history.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)]
        )
    )
    
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=messages_history,
        config=config,
    )
    
    messages_history.append(
        types.Content(
            role="model",
            parts=[types.Part.from_text(text=response.text)]
        )
    )
    
    return response.text

turn_1_reply = send_chat_message("I don't like to bully people!")
print(f"User:I don't like to bully people! \nAI: {turn_1_reply}\n")

turn_2_reply = send_chat_message("What did I say?")
print(f"User: What did I just say I didn't liked?\nAI: {turn_2_reply}\n")