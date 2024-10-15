import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "string"
auth_token = "string"

parameters = {
    "lat": 69.5632,
    "lon": -82.406540,
    "appid": "string",
    "cnt": 4,
}
will_rain = False
response = requests.get(OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()
for index in range(0,4):
    if int(weather_data["list"][index]["weather"][0]["id"]) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It will rain today! Bring an umbrella!",from_="twilio_number",to="verified_number")
print(message.status)


