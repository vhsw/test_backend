#!/usr/bin/env python
"""API wrapper for openweathermap.org"""

import os
import argparse
from dataclasses import dataclass
from datetime import date
from typing import Dict, List
import requests
from dotenv import load_dotenv

load_dotenv()

try:
    default_params = {"units": "metric", "appid": os.environ["OPENWEATHERMAP_API_KEY"]}
except KeyError:
    raise KeyError("OPENWEATHERMAP_API_KEY environment variable not set")


@dataclass
class Report:
    """Weather report for single day"""

    date: date
    temperature: float
    description: str

    def __str__(self):
        return (
            f"{self.date}: {self.temperature:+5.1f}°C {self.description.capitalize()}"
        )


def get_current_weather(city: str) -> Report:
    """get realtime weather report for single city"""

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={**default_params, "q": city},
    ).json()
    if response["cod"] != 200:
        raise ValueError(response["message"])

    return Report(
        date=date.fromtimestamp(response["dt"]),
        temperature=response["main"]["temp"],
        description=response["weather"][0]["description"],
    )


def get_coords(city: str) -> Dict[str, str]:
    """return latitude and longitude for single city"""

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={**default_params, "q": city},
    ).json()
    if response["cod"] != 200:
        raise ValueError(response["message"])
    return response["coord"]


def get_forcast(city: str, days: int) -> List[Report]:
    """get weather forcast for single city"""

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall",
        params={
            **default_params,
            **get_coords(city),
            "exclude": "current,minutely,hourly",
        },
    ).json()

    return [
        Report(
            date=date.fromtimestamp(day["dt"]),
            temperature=day["temp"]["day"],
            description=day["weather"][0]["description"],
        )
        for day in response["daily"][:days]
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get current weather data for given location"
    )
    parser.add_argument("city", nargs=1, help="city name")
    parser.add_argument(
        "--forcast",
        metavar="days",
        choices=range(1, 8),
        type=int,
        help="show forecast for 1..7 days",
    )
    args = parser.parse_args()

    if args.forcast is None:
        print(get_current_weather(args.city))
    else:
        for day in get_forcast(args.city, args.forcast):
            print(day)
