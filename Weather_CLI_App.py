import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_weather(data):
    if data["cod"] != 200:
        print("❌ City not found! Try again.\n")
        return None

    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"].capitalize()
    wind_speed = data["wind"]["speed"]

    print("\n🌍  City:", f"{city}, {country}")
    print(f"🌡️  Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️  Weather: {weather}")
    print(f"💨 Wind Speed: {wind_speed} m/s")
    print(f"🕒 Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*35)

    with open("weather_data.txt", "a", encoding="utf-8") as f:
        f.write(f"{city}, {country} | {temp}°C | {humidity}% | {weather} | {wind_speed} m/s | "
                f"{datetime.datetime.now()}\n")

def main():
    print("=== 🌤 Weather CLI App ===")
    print("Type 'exit' to quit anytime.")
    print("="*35)

    while True:
        city = input("\nEnter city name: ").strip()
        if city.lower() == "exit":
            print("👋 Exiting Weather CLI App. Stay safe!")
            break
        data = get_weather(city)
        display_weather(data)

if __name__ == "__main__":
    main()
