import datetime as dt
import requests
from dotenv import load_dotenv
import os

GENDER = "female"  # User's Data
WEIGHT_KG = 42
HEIGHT_CM = 165
AGE = 14


def configure():
    load_dotenv()


def add_workout_row(exercise, duration, calories):
    # Get current date and time
    now = dt.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")

    # Prepare workout data to pass to Google Sheets
    workout_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),  # Capitalize the first letter of each word
            "duration (min)": duration,
            "calories": calories,
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    # Send POST request to add workout data to Google Sheets
    response = requests.post(url=os.getenv('SHEET_ENDPOINT'), json=workout_data, headers=headers)
    # print(response.text)


def fetch_and_process_exercises(query):
    # Header for authentication with the exercise endpoint
    headers = {
        "x-app-id": os.getenv('EXERCISE_API_ID'),
        "x-app-key": os.getenv('EXERCISE_API_KEY'),
        'Content-Type': 'application/json'
    }
    # Prepare request body with user query
    body = {
        "query": query,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    # Send POST request to fetch exercise data
    response = requests.post(url=os.getenv('EXERCISE_ENDPOINT'), headers=headers, json=body)
    exercises = response.json()["exercises"]
    print(exercises)
    # Add each exercise as a row in the Google Sheets
    for exercise in exercises:
        add_workout_row(exercise["name"], exercise["duration_min"], exercise["nf_calories"])


def main():
    # Prompt user for input
    query = input("What exercises did you do today, and for how long? ")
    # Process user input and add workout data to Google Sheets
    fetch_and_process_exercises(query)
    print("Workout data added successfully!")


if __name__ == "__main__":
    configure()
    main()
