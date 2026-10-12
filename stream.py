import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

prompt = "Explain how streaming works in large language models in three short paragraphs."

response = client.models.generate_content_stream(
    model="gemini-3.5-flash-lite",
    contents=prompt,
)

for chunk in response:
    print(chunk.text, end="", flush=True)

print()