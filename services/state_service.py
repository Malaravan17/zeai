from sqlalchemy.orm import Session
from models.state import State
import requests
from config.settings import AGMARKNET_BASE_URL


def fetch_all_states():

    response = requests.get(
        f"{AGMARKNET_BASE_URL}/agmarknet/states"
    )

    states = response.json()

    return states

def sync_states(db: Session, states: list):

    for state in states:

        existing = db.query(State).filter(
            State.state_id == state["state_id"]
        ).first()

        if existing is None:

            new_state = State(
                state_id=state["state_id"],
                state_name=state["state_name"]
            )

            db.add(new_state)

    db.commit()

    return {
        "message": "States Synced Successfully"
    }


def get_all_states(db: Session):

    states = db.query(State).all()

    return states