import os
from dotenv import load_dotenv
from google import genai

# 1. .env file se variables load karein
load_dotenv()

# 2. Key environment variable se access karein
api_key = os.environ.get("GEMINI_API_KEY")

# 3. Google GenAI client initialize karein
client = genai.Client(api_key=api_key)

# 4. Gemini model ko prompt bhejein
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain what an LLM token is in one simple sentence.",
)

# 5. Output print karein
print("\n--- Gemini Response ---")
print(response.text)