# main.py
from flask import Flask, render_template
from weather import get_weather

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather/<location>")
def weather(location):
    weather_data = get_weather(location)
    return render_template("weather.html", weather_data=weather_data)


@app.route("/traffic")
def traffic():
    return render_template("traffic.html")


@app.route("/cameras")
def cameras():
    return render_template("cameras.html")
