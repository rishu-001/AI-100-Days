from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key not found...")

client = genai.Client(api_key = API_KEY)

print("=" * 50)
print("Gemini Chatbot for career roadmap - skills, certificates, salary")
print("=" * 50)

def get_skills(role: str):
    """
    Returns required skill for a role.
    Parameters: role(str) - Career selected by the user
    Return: dict: Required skills
    """

    return {
        "role" : role,
        "skills" : [
            "Python", "Machine Learning", "Deep Learning", "Data Science", "LLMs"
        ]
    }

def get_certificate(role: str):
    """
    Returns cerification info
    Parameters : role(str): Career role
    Return: dict
    """

    return {
        "role": role,
        "certifications" : [
        "AI-102", "AZ-104", "DP-300", "Google Gen AI"
        ]
    }

def get_salary(role: str):
    """
    Returns expected slaary range
    Paramaeters : role(str)
    Return: dict
    """

    return {
        "role" : role,
        "salary_range" : "10-15 LPA"
    }



#  Register Functions
tools = [
    get_skills, get_certificate, get_salary
]

query = input("Prompt : ")

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = query,
    config = types.GenerateContentConfig(
        tools = tools
    )
)

print(response.text)

