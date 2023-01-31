# main.py
from flask import Flask, render_template, send_from_directory
from fetch_data import update_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather")
def weather():
    return render_template("weather.html")


@app.route("/fetch_weather_data")
def weather_data():
    return send_from_directory('/tmp/weather_site_bin', 'weather_data.json')
