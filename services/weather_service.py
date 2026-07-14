import requests

from sqlalchemy.orm import Session

from models.farm import Farm

from config.settings import OPEN_METEO_BASE_URL


def get_current_weather(db: Session, farm_id: int):

    # Get Farm Details
    farm = db.query(Farm).filter(
        Farm.id == farm_id
    ).first()

    if farm is None:
        return {
            "message": "Farm Not Found"
        }

    latitude = farm.latitude
    longitude = farm.longitude

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
    }

    response = requests.get(
        OPEN_METEO_BASE_URL,
        params=params
    )

    weather = response.json()

    current = weather["current"]

    return {
        "farm_name": farm.farm_name,
        "district": farm.district,
        "state": farm.state,

        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"]
    }