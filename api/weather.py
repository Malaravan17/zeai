from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.database import get_db

from services import weather_service

router = APIRouter()


@router.get("/weather/current/{farm_id}")
def get_current_weather(
        farm_id: int,
        db: Session = Depends(get_db)
):
    return weather_service.get_current_weather(
        db,
        farm_id
    )

@router.get("/weather/forecast/{farm_id}")
def get_weather_forecast(
        farm_id: int,
        db: Session = Depends(get_db)
):
    return weather_service.get_weather_forecast(
        db,
        farm_id
    )