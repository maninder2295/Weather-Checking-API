import requests
from twilio.rest import Client


# LAT = 32.677124
# LONG = 74.848442
API_KEY = "c95d80c8d38b54b4ff1ce6c8050f1f4c"

# Twilio details
account_sid = "AC9bfdae395c16df5b9cad0a7b969909b4"
auth_token = "dfed8535083e5a7bbc3bb3b53d0d1f53"



parameters = {
    "lat" : -27.46794,
    "lon" : 153.02809,
    "exclude" : "current,minutely,daily",
    "appid" : API_KEY,
    "units" : "metric",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for twelve_hours in range(0, 12):
    id_hourly = data["hourly"][twelve_hours]["weather"][0]["id"]
    if id_hourly < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to be rain bring your ☂",
        from_="+16149454125",
        to="+917889361366"
    )

print(message.status)