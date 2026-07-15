import requests

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