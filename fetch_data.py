import time
import json
import os
from weather import get_weather


def update_data():
        while True:
            weather_data = get_weather("84010")
            Fetch.write_weather_to_file(weather_data)
            time.sleep(300) # sleep for 5 minutes


class Fetch:
    def write_weather_to_file(weather_data):
        if not os.path.exists('/tmp/weather_site_bin'):
            os.makedirs('/tmp/weather_site_bin')

        with open("/tmp/weather_site_bin/weather_data.json", "w") as f:
            json.dump(weather_data, f)
