import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""                        # ENTER YOUR TWILIO API KEY
account_sid = ""                    # ENTER YOUR TWILIO ACCOUNT SID
auth_token = ""                     # ENTER YOUR TWILIO AUTH TOKEN

TWILIO_NUMBER = "+1123456789"       # ENTER YOUR TWILIO GENERATED NUMBER
MOBILE_NUMBER = "+1123456789"       # ENTER YOUR MOBILE NUMBER



parameters = {
    "lat":19.0144,                  # ENTER YOUR LATITUDE
    "lon":72.8479,                  # ENTER YOUR LONGITUDE
    "appid":API_KEY,
    "exclude":"current,minutely,daily"
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

weather_codes=[]
will_rain = False
time=""

for i in range(0, 13):
    code = data["hourly"][i]["weather"][0]["id"]
    if code < 700:
        will_rain = True
        time += f"{i + 1}, "

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"It's going to rain today at hours : {time} Bring an Umbrella! ☂️",
        from_=TWILIO_NUMBER,
        to=MOBILE_NUMBER
    )

    print(message.status)