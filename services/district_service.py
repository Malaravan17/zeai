from sqlalchemy.orm import Session

from models.district import District
from models.state import State


def sync_districts(db: Session, districts: list):

    for district in districts:

        state = db.query(State).filter(
            State.state_id == district["state_id"]
        ).first()

        if state is None:
            continue

        existing = db.query(District).filter(
            District.district_id == district["district_id"]
        ).first()

        if existing is None:

            new_district = District(

                district_id=district["district_id"],

                district_name=district["district_name"],

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