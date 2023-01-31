import time
import json
import os
from weather import get_weather


def update_data():
    """This function is intended to continuously run every five minutes
    and run fetch functions for all gathered API data in the web app.
    """
    while True:
        weather_data = get_weather("84010")
        Fetch.write_weather_to_file(weather_data)
        time.sleep(300)  # sleep for 5 minutes


class Fetch:
    def write_weather_to_file(weather_data):
        """This function writes a string dictionary into a file named
        /tmp/weather_site_bin/weather_data.json.
        """
        if not os.path.exists("/tmp/weather_site_bin"):
            os.makedirs("/tmp/weather_site_bin")

        with open("/tmp/weather_site_bin/weather_data.json", "w") as f:
            json.dump(weather_data, f)
