import os
import requests
from dotenv import load_dotenv

load_dotenv()
# TASK 1: removed hard coded API_KEY
API_KEY = os.getenv('API-KEY')

if not API_KEY:
    raise ValueError("API key not found. Please set the API-KEY environment variable.")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        #Task 2: Handle rate limiting & errors gracefully
        if response.status_code == 429:
            print("Rate limit exceeded. Please wait a moment and try again.")
            return

        elif response.status_code != 200:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return

        data = response.json()

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        print(f" Temperature: {temp}°C")
        print(f"Condition: {weather}")

    except requests.exceptions.RequestException as e:
        print(f" Network error occurred: {e}")
    except KeyError:
        print("Unexpected response format. Please try again later.")

# Task 3:
# We do NOT log or print user-entered city names because location data is considered
# personally identifiable information (PII). Under privacy principles such as
# GDPR (General Data Protection Regulation) and data minimization, applications
# should avoid collecting or exposing unnecessary user data.

if __name__ == "__main__":
    city = input("Enter city name: ")

    get_weather(city)

