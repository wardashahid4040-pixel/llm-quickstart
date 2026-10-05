import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain what an LLM token is in one simple sentence.",
)

print("\n--- Gemini Response ---")
print(response.text)