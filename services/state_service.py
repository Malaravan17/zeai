from sqlalchemy.orm import Session
from models.state import State
import requests
from config.settings import AGMARKNET_BASE_URL,AGMARKNET_API_KEY

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


def sync_states(db: Session, states: list):

    processed_state_ids = set()

    for state in states:
        ceda_state_id = state["census_state_id"]

        # Skip repeated state records returned for different districts
        if ceda_state_id in processed_state_ids:
            continue

        processed_state_ids.add(ceda_state_id)

        existing = db.query(State).filter(
            State.state_id == ceda_state_id
        ).first()

        if existing is None:
            db.add(
                State(
                    state_id=ceda_state_id,
                    state_name=state["census_state_name"]
                )
            )

    db.commit()

    return {
        "message": "States Synced Successfully"
    }


def get_all_states(db: Session):

    states = db.query(State).all()

    return states


