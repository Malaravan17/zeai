import requests
from sqlalchemy.orm import Session

from config.settings import AGMARKNET_BASE_URL, AGMARKNET_API_KEY

from models.farm import Farm
from models.crop_season import CropSeason
from models.commodity import Commodity
from models.state import State
from models.district import District
from models.market import Market


# =============================================
# Common Headers
# =============================================

# =============================================
# Fetch Commodities From AGMARKNET
# =============================================

HEADERS = {
    "Authorization": f"Bearer {AGMARKNET_API_KEY}"
}

def fetch_all_commodities():
    response = requests.get(
        f"{AGMARKNET_BASE_URL}/agmarknet/commodities",
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["output"]["data"]

# =============================================
# Sync Commodities To Database
# =============================================

def sync_commodities(
    db: Session,
    commodities: list
):

    inserted = 0

    for commodity in commodities:

        existing = db.query(Commodity).filter(
            Commodity.commodity_id == commodity["commodity_id"]
        ).first()

        if existing is None:

            db.add(
                Commodity(
                    commodity_id=commodity["commodity_id"],
                    commodity_name=commodity["commodity_name"]
                )
            )

            inserted += 1

    db.commit()

    return {
        "message": "Commodities Synced Successfully",
        "inserted": inserted
    }


# =============================================
# Read Commodities
# =============================================

def get_all_commodities(db: Session):

    return db.query(Commodity).all()


# =============================================
# Sync Markets For A Farm's Active Crop
# =============================================

def sync_markets_for_farm(
    db: Session,
    farm_id: int
):
    farm = db.query(Farm).filter(Farm.id == farm_id).first()

    if not farm:
        return {"message": "Farm not found"}

    crop = db.query(CropSeason).filter(
        CropSeason.farm_id == farm_id,
        CropSeason.status == "active"
    ).first()

    if not crop:
        return {"message": "No active crop found"}

    commodity = db.query(Commodity).filter(
        Commodity.commodity_name == crop.crop_name
    ).first()

    if not commodity:
        return {"message": "Commodity not found"}

    state = db.query(State).filter(
        State.state_name == farm.state
    ).first()

    if not state:
        return {"message": "State not found"}

    district = db.query(District).filter(
        District.district_name == farm.district,
        District.state_id == state.id
    ).first()

    if not district:
        return {"message": "District not found"}

    payload = {
        "commodity_id": commodity.commodity_id,
        "state_id": state.state_id,
        "district_id": district.district_id,
        "indicator": "price"
    }

    response = requests.post(
        f"{AGMARKNET_BASE_URL}/agmarknet/markets",
        headers=HEADERS,
        json=payload,
        timeout=30
    )
    response.raise_for_status()

    markets = response.json()["output"]["data"]
    inserted = 0

    for market in markets:
        existing = db.query(Market).filter(
            Market.market_id == market["market_id"]
        ).first()

        if existing is None:
            db.add(
                Market(
                    market_id=market["market_id"],
                    market_name=market["market_name"],
                    district_id=district.id
                )
            )
            inserted += 1

    db.commit()

    return {
        "message": "Markets Synced Successfully",
        "inserted": inserted,
        "available_from_ceda": len(markets)
    }


# =============================================
# Get Market Prices
# =============================================

# def get_market_prices(
#     db: Session,
#     farm_id: int
# ):

#     # ----------------------------
#     # Find Farm
#     # ----------------------------

#     farm = db.query(Farm).filter(
#         Farm.id == farm_id
#     ).first()

#     if not farm:
#         return {
#             "message": "Farm not found"
#         }

#     # ----------------------------
#     # Find Active Crop
#     # ----------------------------

#     crop = db.query(CropSeason).filter(
#         CropSeason.farm_id == farm_id,
#         CropSeason.status == "active"
#     ).first()

#     if not crop:
#         return {
#             "message": "No active crop found"
#         }

#     # ----------------------------
#     # Find Commodity
#     # ----------------------------

#     commodity = db.query(Commodity).filter(
#         Commodity.commodity_name == crop.crop_name
#     ).first()

#     if not commodity:
#         return {
#             "message": "Commodity not found"
#         }

#     # ----------------------------
#     # Find State
#     # ----------------------------

#     state = db.query(State).filter(
#         State.state_name == farm.state
#     ).first()

#     if not state:
#         return {
#             "message": "State not found"
#         }

#     # ----------------------------
#     # Find District
#     # ----------------------------

#     district = db.query(District).filter(
#         District.district_name == farm.district,
#         District.state_id == state.id
#     ).first()

#     if not district:
#         return {
#             "message": "District not found"
#         }

#     # ----------------------------
#     # Find Markets
#     # ----------------------------

#     markets = db.query(Market).filter(
#         Market.district_id == district.id
#     ).all()

#     market_ids = [
#         market.market_id
#         for market in markets
#     ]
    

#     # ----------------------------
#     # Payload
#     # ----------------------------

#     payload = {

#         "commodity_id": commodity.commodity_id,

#         "state_id": state.state_id,

#         "district_id": [
#             district.district_id
#         ],

#         "from_date": "2026-07-01",

#         "to_date": "2026-07-18"

#     }

#     # The CEDA prices API supports district-level requests without market IDs.
#     if market_ids:
#         payload["market_id"] = market_ids

#     print("\n========== MARKET REQUEST ==========")
#     print(payload)
#     print("====================================\n")

#     # ----------------------------
#     # Call API
#     # ----------------------------

#     response = requests.post(
#         f"{AGMARKNET_BASE_URL}/agmarknet/prices",
#         headers=HEADERS,
#         json=payload
#     )

#     print("\n========== MARKET RESPONSE ==========")
#     print("Status:", response.status_code)
#     print("Response:", response.text)
#     print("=====================================\n")

#     response.raise_for_status()

#     return response.json()
