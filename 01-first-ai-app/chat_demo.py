from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

prompt = "Explain AI in simple terms."

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt
)

print(response.text)