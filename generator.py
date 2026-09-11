from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client()

# print("")
# print("Welcome to the Study Plan Generator!")
# print("Please fill in the prompted details in lowercase letters.")
# print("")

# subject = input("Enter one subject you need to study for: ")
# topic = input("Enter the specific topic under the subject you need to study for: ")
# days = int(input("Enter the number of days you have till the exam: "))
# while days <= 0:
    # print("Number of days must be greater than 0.")
    # days = int(input("Enter the number of days you have till the exam: "))
# hours = int(input("Enter the number of hours you have available to study each day: "))
# while hours <= 0:
    # print("Number of hours must be greater than 0.")
    # hours = int(input("Enter the number of hours you have available to study each day: "))
# difficulty = input("Enter the difficulty level (easy, medium, hard): ")
# while difficulty.lower() not in ["easy", "medium", "hard"]:
    # print("Difficulty level must be 'easy', 'medium', or 'hard'.")
    # difficulty = input("Enter the difficulty level (easy, medium, hard): ")

# print("")
# print("Generating your study plan...")
# print("")
# print("")

def generate_plan(subject, topic, days, hours, difficulty):
    user_input = f"I have a test on {topic}, which is a part of {subject}, in {days} days from today. I can study for {hours} hours every day. This is a {difficulty} subject for me. Design a study plan for me detailing what to study and what to do for how long each day. Format the plan as a day-by-day list with specific topics and time blocks."
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=user_input
    )
    return interaction.output_text