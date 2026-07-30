from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import state_service, district_service
from services import market_service
from database.database import get_db
from config.settings import AGMARKNET_API_KEY

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

@router.post("/market/sync/markets/{farm_id}")
def sync_markets(
    farm_id: int,
    db: Session = Depends(get_db)
):
    return market_service.sync_markets_for_farm(db, farm_id)


@router.post("/market/sync/states")
def sync_states(db: Session = Depends(get_db)):
    geographies = state_service.fetch_all_geographies()
    return state_service.sync_states(db, geographies)


@router.post("/market/sync/districts")
def sync_districts(db: Session = Depends(get_db)):
    geographies = district_service.fetch_all_geographies()
    return district_service.sync_districts(db, geographies)




