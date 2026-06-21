from google import genai
from dotenv import load_dotenv
import os
import time
from datetime import datetime
import random

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = API_KEY)

print("=" * 50)
print("Gemini Chatbot")
print("=" * 50)

def get_current_time(query = None):
    return datetime.now().strftime("%H:%M:%S, %p")

def calculator(expression):
    try:
        return eval(expression)
    except Exception as ex:
        return "Invalid expression"
    

def motivation_quotes(query = None):
    quotes = [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
    ]
    return random.choice(quotes)

def generate_roadmap(topic):
    prompt = f"""
    Generate a roadmap for learning {topic}.
    The roadmap should include:
    1. Key concepts to learn
    2. Recommended resources (books, courses, articles)
    3. Suggested projects to practice
    4. Estimated time to master each concept

    Return the roadmap in a structured format.
    """
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )
    return response.text


TOOLS = {
    "TIME_TOOL": get_current_time,
    "CALCULATOR_TOOL": calculator,
    "QUOTE_TOOL": motivation_quotes,
    "ROADMAP_TOOL": generate_roadmap
}

def select_tool(query):
    prompt = f"""
    You are a tool selector.
    Available tools:
    1. TIME_TOOL
    2. CALCULATOR_TOOL
    3. QUOTE_TOOL
    4. ROADMAP_TOOL

    Return only tool name.
    User query: {query}
    """

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    return response.text.strip()

def execute_tool(tool_name, query):
    tool = TOOLS.get(tool_name)
    if not tool:
        return "Tool not found."
    
    return tool(query)


while True:
    query = input("\nYou : ")
    if(query.lower() in ["exit", "quit", "bye"]):
        print("Goodbye!")
        break

    tool = select_tool(query)
    print(f"\n[Selected Tool]: {tool}")

    result = execute_tool(tool, query)
    print(f"\nAssistant: {result}")


