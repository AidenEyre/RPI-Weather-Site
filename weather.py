import requests
import pytz
import constants
from datetime import datetime


def get_weather(location):
    """Reach out to the openweathermap API and return wather data for
    the given zip code.

    Unix timestamps are converted to HH:MM am/pm in MST.
    """
    coords = Weather.get_coordinates(location)
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = (
        base_url
        + "lat="
        + str(coords["lat"])
        + "&lon="
        + str(coords["lon"])
        + "&appid="
        + constants.OPEN_WEATHER_MAP_API_KEY
        + "&units=imperial"
    )
    response = requests.get(complete_url)
    weather = response.json()

    if weather["cod"] != "404":
        tempData = weather["main"]
        temperature = tempData["temp"]
        feels_like = tempData["feels_like"]
        humidity = tempData["humidity"]

        weather_data = weather["weather"]
        sky = weather_data[0]["description"]

        wind_data = weather["wind"]
        wind = wind_data["speed"]

        sun_data = weather["sys"]
        sunrise = Weather.get_mtn_time(sun_data["sunrise"])
        sunset = Weather.get_mtn_time(sun_data["sunset"])
    else:
        print(" City Not Found ")

    weather_data = {
        "temperature": temperature,
        "feels_like": feels_like,
        "humidity": humidity,
        "sky": sky,
        "wind": wind,
        "sunrise": sunrise,
        "sunset": sunset,
        "location": coords["name"],
    }
    return weather_data


class Weather:
    def get_coordinates(location):
        """Reached out to the openweathermap API to return lat/long
        for the given zip code.
        """
        base_url = "http://api.openweathermap.org/geo/1.0/zip?"
        complete_url = (
            base_url
            + "zip="
            + location
            + ",US"
            + "&appid="
            + constants.OPEN_WEATHER_MAP_API_KEY
        )
        response = requests.get(complete_url)

        return response.json()

    def get_mtn_time(timestamp):
        """Convert a uniz timestamp to MST with the format HH:MM am/pm"""
        mtn_tz = pytz.timezone("America/Denver")
        datetime_obj = datetime.fromtimestamp(timestamp, mtn_tz)
        return datetime_obj.strftime("%I:%M %p")
