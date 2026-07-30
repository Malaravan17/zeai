from sqlalchemy.orm import Session
import requests
from config.settings import AGMARKNET_BASE_URL,AGMARKNET_API_KEY
from models.district import District
from models.state import State

HEADERS = {
    "Authorization": f"Bearer {AGMARKNET_API_KEY}"
}

def fetch_all_geographies():
    response = requests.get(
        f"{AGMARKNET_BASE_URL}/agmarknet/geographies",
        headers=HEADERS,
        timeout=30
    )
    response.raise_for_status()
    return response.json()["output"]["data"]


def sync_districts(db: Session, districts: list):

    for district in districts:

        state = db.query(State).filter(
            State.state_id == district["census_state_id"]
        ).first()

        if state is None:
            continue

        existing = db.query(District).filter(
            District.district_id == district["census_district_id"]
        ).first()

        if existing is None:

            new_district = District(

                district_id=district["census_district_id"],

                district_name=district["census_district_name"],

                state_id=state.id

            )

            db.add(new_district)

    db.commit()

    return {
        "message": "Districts Synced Successfully"
    }


def get_all_districts(db: Session):

    districts = db.query(District).all()

    return districts