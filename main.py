import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

YOUR_APP_ID = os.environ.get("YOUR_APP_ID")
YOUR_NUTRITION_API_KEY = os.environ.get("YOUR_NUTRITION_API_KEY")
# Basic Auth Username and Password
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")

# ------------------------------------------------------------------------------------------------------
# Get calorie count for input exercise
headers = {
    "x-app-id": YOUR_APP_ID,
    "x-app-key": YOUR_NUTRITION_API_KEY
}

base_url = "https://app.100daysofpython.dev"

post_url = f"{base_url}/v1/nutrition/natural/exercise"
post_body = {
    "query": input("What exercise did you do today?\n")
}

response = requests.post(url=post_url, json=post_body, headers=headers)
exercise_data = response.json()['exercises'][0]
calories_burned = exercise_data['nf_calories']
exercise_name = exercise_data['name']
duration = exercise_data['duration_min']

# ------------------------------------------------------------------------------------------------------
# Add row to workout sheet
today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
print(today_date)
today_time = today.strftime("%H:%M:%S")
print(today_time)
workout_sheet_url = "https://api.sheety.co/4187912d679c992e84911d466be33df2/allWorkouts/workouts"
workout_sheet_inputs = {
    "workout": {
        "date": today_date,
        "time": today_time,
        "exercise": exercise_name.title(),
        "duration": duration,
        "calories": calories_burned
    }
}
workout_sheet_headers = {
    "Authorization": "dfdff23424"
}
basic_auth = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)
sheet_response = requests.post(url=workout_sheet_url, json=workout_sheet_inputs, headers=workout_sheet_headers, auth=basic_auth)
print(sheet_response.text)
