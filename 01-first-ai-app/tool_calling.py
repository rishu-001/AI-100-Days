from google import genai
from dotenv import load_dotenv
import os
import time
from datetime import datetime
import random

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

def get_current_time():
    return datetime.now().strftime("%H:%M:%S, %p")

def calculator(expression):
    try:
        return eval(expression)
    except Exception as ex:
        return "Invalid expression"
    

def motivation_quotes():
    quotes = [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    return random.choice(quotes)


def route_tool(query):
    query = query.lower()
    if "time" in query:
        return "time"
    elif "calculate" in query:
        return "calculator"
    elif "motivate" in  query or "quote" in query:
        return "quote"
    
    return "gemini"


while True:
    user_input = input("Prompt: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break

    tool = route_tool(user_input)
    if tool =="time":
        result = get_current_time()
        print(f"Assistant: The current time is {result}")
    elif tool == "calculator":
        expression = user_input.lower().replace("calculate", "").strip()
        result = calculator(expression)
        print(f"Assistant: The result is {result}")
    elif tool == "quote":
        result = motivation_quotes()
        print(f"Assistant: Here's a motivational quote for you:\n{result}")
    else:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = user_input
        )   

        print(f"Assistant: {response.text}")