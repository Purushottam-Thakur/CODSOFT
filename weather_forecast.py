import requests

api_key = '27ae5f04f01c06aa23e4838dbfad7df8'

user_input = input("Enter City:")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"
)
if weather_data.json()['cod']== '404':
    print("No City Found")
else:    

    weather = weather_data.json()['weather'] [0] ['main']
    temp = round(weather_data.json()['main'] ['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°f")