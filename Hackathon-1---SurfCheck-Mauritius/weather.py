import requests
import json

def load_api_key():
    with open("config.json") as f:
        config = json.load(f)
        return config["api_key"]

def get_weather_by_coords(lat, lon):
    api_key = load_api_key()
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(data.get("message", "API error"))

    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    temp = data["main"]["temp"]

    return {
        "location": f"{lat},{lon}",
        "weather": weather,
        "wind_speed": wind_speed,
        "temp": temp
    }
