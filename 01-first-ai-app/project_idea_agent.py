from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = API_KEY)

def ask_gemini(prompt):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )
    return response.text

class ProjectIdeaAgent:
    def __init__(self, skills):
        # skills = user_input
        self.skills = skills

    # step-1 : Reasoning
    def analyze_skills(self):
        print(f"[Agent] Analyzing skills...")
        
        prompt = f""""
        User skills and interests : {self.skills}
        Analyze the user's skills and interests.

        Identify:
        1. Core technical strengths
        2. Areas of expertise
        3. Types of projects the user is capable of building

        Return the analysis in bullet points.
        """

        return ask_gemini(prompt)
    
    def find_domains(self, analysis):
        print(f"[Agent] Finding Domains for project...")
        prompt = f""""
        user_analysis = {analysis}
        Based on the user's strengths and capabilities,
        identify the most suitable domains where the user can build impactful projects.

        Consider domains such as:
        - Education
        - Healthcare
        - Finance
        - Productivity
        - Generative AI
        - Travel
        - E-commerce
        - Cybersecurity

        Return only the top 5 domains with a short reason for each.
        """


        return ask_gemini(prompt)

    # step-2 : Planning   
    def generate_ideas(self, domains):
        print(f"[Agent] Generating project ideas...")
        prompt = f"""
        project_domains = {domains}
        For each project provide:
        1. Project Name
        2. Problem it solves
        3. Brief Description
        4. Difficulty Level (Beginner/Intermediate/Advanced)
        5. Expected Tech Stack

        The projects should:
        - Be practical and portfolio-worthy
        - Be suitable for a student
        - Be achievable within 2-4 weeks
        - Demonstrate AI/ML or software development skills

        Return the response in a structured format.
        """

        return ask_gemini(prompt)
    
    def run(self):
        analysis = self.analyze_skills()
        time.sleep(1)

        domains = self.find_domains(analysis)
        time.sleep(1)

        ideas = self.generate_ideas(domains)
        print("\n" + "=" * 50)
        print(ideas)
        print("=" * 50)

print("=" * 50)
print("Welcome to the Project Idea Generator!")
print("=" * 50)
skill = input("Enter the skills you have :")
agent = ProjectIdeaAgent(skill)
agent.run()