import requests
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
TWILIO_ACCOUNT_SID = 'AC5173cb3cd52ad28d247eef71b6a3b229'
TWILIO_AUTH_TOKEN = '09587f94c772208b129bead72a427ad2'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

api_key = '49290929bf2883210db08ab9aa9494cb'
# lat = 6.469044
# long = 7.549517
# my_location = [lat, long]
# emene_location = 6.477800, 7.580430

parameters = {
    'lat': 6.477800,
    'lon': 7.580430,
    'appid': api_key,
    'exclude': 'current,minutely,daily'

}
# get the response from the api call
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
# raise an error exception if there is mistake
response.raise_for_status()
# print the data
weather_data = response.json()
# weather_slice = (weather_data['hourly'][0:12])
for n in range(0, 11):
    weather_id = weather_data['hourly'][n]['weather'][0]['id']
    if weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's gonna rain today. Bring an umbrella!☂️",
            from_='+17125265712',
            to='+234 810 667 1579'
        )
        print(message.status)
        break
    else:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="It's gonna rain today. Bring an umbrella!☂️",
            from_='+17125265712',
            to='+234 810 667 1579'
        )



