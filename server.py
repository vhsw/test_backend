"""Flask weather API"""
from flask import Flask, redirect, request, jsonify
from weather import get_current_weather, get_forcast

app = Flask(__name__)


@app.route("/")
def default_city():
    """Redirect to default city"""
    return redirect("city/Moscow")


@app.route("/city/<city>")
def weather(city: str):
    """Get weather in the city"""
    return jsonify(get_current_weather(city))


@app.route("/city/<city>/forcast")
def forcast(city: str):
    """Get weather forcast in the city"""
    days = request.args.get("days", type=int, default=7)
    if days < 1 or days > 7:
        raise ValueError("days must be in 1..7")
    return jsonify(get_forcast(city, days))
