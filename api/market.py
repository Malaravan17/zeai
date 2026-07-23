from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import market_service
from database.database import get_db

router = APIRouter()


# Sync commodities from AGMARKNET to DB
@router.post("/market/sync/commodities")
def sync_commodities(
    db: Session = Depends(get_db)
):

    commodities = market_service.fetch_all_commodities()

    return market_service.sync_commodities(
        db,
        commodities
    )


# Read commodities from DB
@router.get("/market/commodities")
def get_all_commodities(
    db: Session = Depends(get_db)
):

    return market_service.get_all_commodities(db)


# Get market prices for a farm
@router.get("/market/{farm_id}")
def get_market_prices(
    farm_id: int,
    db: Session = Depends(get_db)
):

    return market_service.get_market_prices(
        db,
        farm_id
    )