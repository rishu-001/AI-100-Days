from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key not found...")


# create gemini client
client = genai.Client(api_key = API_KEY)

# store chat history
history = []

system_prompt = """
You are a friendly AI assistant.
Rules:
1. Be helful
2. Be Professional
3. Keep  answers clean and concise
4. Remember previous conversation context 
"""

print("*" * 50)
print("Gemini chatbot")
print("*" * 50)


while True:
    user_input = input("Prompt: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break

    # store user message
    history.append(f"User: {user_input}")
    conversation_context = system_prompt + "\n"
    conversation_context += "\n".join(history)

    # call gemini
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = conversation_context
    )
    

    bot_response = response.text
    print(f"\nGemini: {bot_response}")

    # store bot response
    history.append(f"Assistant: {bot_response}")
