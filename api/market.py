from fastapi import APIRouter

from services import market_service

router = APIRouter()


@router.get("/market/commodities")
def get_all_commodities():

    return market_service.fetch_all_commodities()