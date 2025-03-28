from datetime import datetime
import os
import requests

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
NUTRITION_ENDPOINT = os.getenv("NUTRITION_ENDPOINT")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")  

GENDER = "male"
WEIGHT = 67
HEIGHT = 180
AGE = 21

user_input = input("Tell me which exercise you did today: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NUTRITION_ENDPOINT, headers=headers, json=parameters)
result = response.json()
print(result)

sheet_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result.get("exercises", []):
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=sheet_headers)
    print(sheet_response.text)
