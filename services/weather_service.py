import requests

from sqlalchemy.orm import Session

from models.farm import Farm

from config.settings import OPEN_METEO_BASE_URL


def get_current_weather(db: Session, farm_id: int):

    farm = db.query(Farm).filter(
        Farm.id == farm_id
    ).first()

    if farm is None:
        return {
            "message": "Farm Not Found"
        }

    f_latitude = farm.latitude
    f_longitude = farm.longitude

    params = {
        "latitude": f_latitude,
        "longitude": f_longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
    }

    response = requests.get(
        OPEN_METEO_BASE_URL,
        params=params
    )

    weather = response.json()

    current = weather["current"]

    advice = generate_weather_advice(current["temperature_2m"],current["relative_humidity_2m"],current["weather_code"])

    condition = get_weather_condition(current["weather_code"])

    return {
        "farm_name": farm.farm_name,
        "district": farm.district,
        "state": farm.state,

        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "condition": condition,
        "advice": advice
        }

def get_weather_forecast(
        db: Session,
        farm_id: int
):

    farm = db.query(Farm).filter(
        Farm.id == farm_id
    ).first()

    if farm is None:
        return {
            "message": "Farm Not Found"
        }

    params = {

        "latitude": farm.latitude,

        "longitude": farm.longitude,

        "daily":
        "weather_code,"
        "temperature_2m_max,"
        "temperature_2m_min,"
        "precipitation_probability_max",

        "forecast_days": 7

    }

    response = requests.get(
        OPEN_METEO_BASE_URL,
        params=params
    )

    weather = response.json()

    daily = weather["daily"]

    forecast = []

    for i in range(len(daily["time"])):

        forecast.append({

            "date": daily["time"][i],

            "condition":
            get_weather_condition(
                daily["weather_code"][i]
            ),

            "max_temperature":
            daily["temperature_2m_max"][i],

            "min_temperature":
            daily["temperature_2m_min"][i],

            "rain_probability":
            daily["precipitation_probability_max"][i]

        })

    return {

        "farm_name": farm.farm_name,

        "district": farm.district,

        "state": farm.state,

        "forecast": forecast

    }






def get_weather_condition(code: int):

    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Dense Drizzle",
        61: "Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Snow",
        80: "Rain Showers",
        95: "Thunderstorm"
    }

    return weather_codes.get(code,"Unknown")

def generate_weather_advice(
        temperature,
        humidity,
        weather_code
):

    advice = []

    if weather_code == 61:
        advice.append(
            "Rain expected. Avoid irrigation."
        )

    if humidity > 85:
        advice.append(
            "High humidity may increase fungal disease risk."
        )

    if temperature > 35:
        advice.append(
            "High temperature. Irrigate during early morning or evening."
        )

    if len(advice) == 0:
        advice.append(
            "Weather conditions look normal."
        )

    return advice