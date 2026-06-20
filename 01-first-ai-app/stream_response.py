from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key not found...")


# create gemini client
client = genai.Client(api_key = API_KEY)

# store chat history
history = []

max_history = 20

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

    if(len(history) > max_history):
        history = history[-max_history:]

    conversation_context = system_prompt + "\n"
    conversation_context += "\n".join(history)


    start_time = time.time()
    full_response = ""
    # call gemini
    stream = client.models.generate_content_stream(
        model = "gemini-2.5-flash",
        contents = conversation_context
    )
    for chunk in stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text

    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nResponse time = {total_time:.2f} seconds")

    # store bot response
    history.append(f"Assistant: {full_response}")
