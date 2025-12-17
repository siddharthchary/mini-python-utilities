# weather_fetcher.py

import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print("City not found!")
            return

        print("\n--- WEATHER DETAILS ---")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])

    except requests.exceptions.RequestException:
        print("Network error occurred")

city_name = input("Enter city name: ")
get_weather(city_name)
