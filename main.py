import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

YOUR_APP_ID = "app_9fd62dd3a6a049e1b19e0599"
YOUR_NUTRITION_API_KEY = "nix_live_NvaBipro3pO3gR2nbllVeqnjAf1OxCwA"
# Basic Auth Username and Password
SHEETY_USERNAME = "dstegge1"
SHEETY_PASSWORD = "dfdfdf42323drf32"

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
