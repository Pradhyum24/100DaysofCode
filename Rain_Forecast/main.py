import requests
from twilio.rest import  Client

api_key = " "
OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"

account_sid = ' '
auth_token = ' '

client = Client(account_sid,auth_token)

parameters = {
    "lat":-3.119028,
    "lon":-60.021732,
    "appid":api_key,
    "cnt":4
}

response = requests.get(OWM_Endpoint,params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain =  False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client.messages \
        .create(body="Its going to rain today.Remember to carry an umbrella",
                from_="+ ",
                to="+ "
                )

    print("Bring an umbrella")
