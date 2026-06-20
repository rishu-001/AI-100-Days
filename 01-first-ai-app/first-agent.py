from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = API_KEY)

class RoadMapAgent:
    def __init__(self, goal):
        # Goal = user_input
        self.goal = goal
    
    # step-1 : Reasoning
    def reason(self):
        print(f"[Agent] Understanding the goal...")
        prompt = f"""
        User Goal = {self.goal}
        Identify all the required skills.
        Return only the skills.
        """

        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )

        return response.text
    
    # step-2 : Planning
    def plan(self, skills):
        print(f"[Agent] Creating the plan...")
        prompt = f"""
        Goal = {self.goal}
        Skills = {skills}
        Arrange the skills in the best order to achieve the goal.
        """

        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )

        return response.text
    
    # step-3 : Execute
    def execute(self, plan):
        print(f"[Agent] Executing the plan...")
        prompt = f"""
        Goal = {self.goal}
        Learning_plan = {plan}
        Create a detailed 90-day roadmap to achieve the goal.
        """

        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )

        return response.text

    # step-4 : Run the agent
    def run(self):
        skills = self.reason()
        time.sleep(1)

        plan = self.plan(skills)
        time.sleep(1)


        roadmap = self.execute(plan)
        print("\n" + "=" * 50)
        print(f"Final Roadmap")
        print("=" * 50)
        print(roadmap)



print("*" * 50)
print("Welcome to the RoadMap Agent")
print("*" * 50)
goal = input("Enter your goal : ")
agent = RoadMapAgent(goal)
agent.run()


