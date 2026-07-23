import requests
from models.farm import Farm
from models.crop_season import CropSeason
from models.commodity import Commodity
from models.state import State
from models.district import District
from models.market import Market
from sqlalchemy.orm import Session
from config.settings import AGMARKNET_BASE_URL
from models.commodity import Commodity


# =============================================
# Fetch Commodities From AGMARKNET
# =============================================

def fetch_all_commodities():

    response = requests.get(
        f"{AGMARKNET_BASE_URL}/agmarknet/commodities"
    )

    commodities = response.json()

    return commodities


# =============================================
# Sync Commodities To Database
# =============================================

def sync_commodities(
        db: Session,
        commodities: list
):

    for commodity in commodities:

        existing = db.query(Commodity).filter(
            Commodity.commodity_id == commodity["commodity_id"]
        ).first()

        if existing is None:

            new_commodity = Commodity(

                commodity_id=commodity["commodity_id"],

                commodity_name=commodity["commodity_name"]

            )

            db.add(new_commodity)

    db.commit()

    return {
        "message": "Commodities Synced Successfully"
    }


# =============================================
# Read Commodities From Database
# =============================================

def get_all_commodities(db: Session):

    commodities = db.query(
        Commodity
    ).all()

    return commodities






def get_market_prices(
    db: Session,
    farm_id: int
):

    # ----------------------------
    # Find Farm
    # ----------------------------
    farm = db.query(Farm).filter(
        Farm.id == farm_id
    ).first()

    if not farm:
        return {
            "message": "Farm not found"
        }

    # ----------------------------
    # Find Active Crop
    # ----------------------------
    crop = db.query(CropSeason).filter(
        CropSeason.farm_id == farm_id,
        CropSeason.status == "active"
    ).first()

    if not crop:
        return {
            "message": "No active crop found"
        }

    # ----------------------------
    # Find Commodity
    # ----------------------------
    commodity = db.query(Commodity).filter(
        Commodity.commodity_name == crop.crop_name
    ).first()

    if not commodity:
        return {
            "message": "Commodity not found"
        }

    # ----------------------------
    # Find State
    # ----------------------------
    state = db.query(State).filter(
        State.state_name == farm.state
    ).first()

    if not state:
        return {
            "message": "State not found"
        }

    # ----------------------------
    # Find District
    # ----------------------------
    district = db.query(District).filter(
        District.district_name == farm.district
    ).first()

    if not district:
        return {
            "message": "District not found"
        }

    # ----------------------------
    # Find Markets
    # ----------------------------
    markets = db.query(Market).filter(
        Market.district_id == district.id
    ).all()

    if not markets:
        return {
            "message": "No markets found"
        }

    market_ids = []

    for market in markets:
        market_ids.append(
            market.market_id
        )

    # ----------------------------
    # Request Body
    # ----------------------------
    payload = {

        "commodity_id": commodity.commodity_id,

        "state_id": state.state_id,

        "district_id": [
            district.district_id
        ],

        "market_id": market_ids,

        "from_date": "2026-07-01",

        "to_date": "2026-07-18"

    }

    # ----------------------------
    # Call AGMARKNET API
    # ----------------------------
    response = requests.post(
        f"{AGMARKNET_BASE_URL}/agmarknet/prices",
        json=payload
    )

    return response.json()