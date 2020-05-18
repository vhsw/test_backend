# Flask Weather API

## Setup

Get api key at [openweathermap.org](https://openweathermap.org/api)

```console
poetry install

echo "OPENWEATHERMAP_API_KEY=<key>
FLASK_APP=server.py" > .env

flask run
```

## Usage

```console
usage: weather.py [-h] [--forcast days] city

Get current weather data for given location

positional arguments:
  city            city name

optional arguments:
  -h, --help      show this help message and exit
  --forcast days  show forecast for 1..7 days
```

## CLI Examples

Current weather data:

```console
➜ weather.py Hafnarfjörður
2020-05-18:  +7.0°C Shower rain
```

Daily forecast for 3 days

```console
➜ weather.py Amsterdam --forcast 3
2020-05-18: +14.0°C Broken clouds
2020-05-19: +16.1°C Broken clouds
2020-05-20: +21.5°C Few clouds
```

## Server Examples

```console
➜ http localhost:5000/city/Södertälje
HTTP/1.0 200 OK
Content-Length: 97
Content-Type: text/html; charset=utf-8
Date: Mon, 18 May 2020 20:43:02 GMT
Server: Werkzeug/1.0.1 Python/3.8.3

{
    "date": "Mon, 18 May 2020 00:00:00 GMT",
    "description": "scattered clouds",
    "temperature": 6.58
}
```

```console
➜ http "localhost:5000/city/Apeldoorn/forcast?days=5"
HTTP/1.0 200 OK
Content-Length: 478
Content-Type: text/html; charset=utf-8
Date: Mon, 18 May 2020 20:44:59 GMT
Server: Werkzeug/1.0.1 Python/3.8.3

[
    {
        "date": "Mon, 18 May 2020 00:00:00 GMT",
        "description": "overcast clouds",
        "temperature": 13.7
    },
    {
        "date": "Tue, 19 May 2020 00:00:00 GMT",
        "description": "overcast clouds",
        "temperature": 18.6
    },
    {
        "date": "Wed, 20 May 2020 00:00:00 GMT",
        "description": "few clouds",
        "temperature": 20.75
    },
    {
        "date": "Thu, 21 May 2020 00:00:00 GMT",
        "description": "light rain",
        "temperature": 22.96
    },
    {
        "date": "Fri, 22 May 2020 00:00:00 GMT",
        "description": "light rain",
        "temperature": 24.95
    }
]
```
