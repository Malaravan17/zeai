from sqlalchemy.orm import Session
from models.commodity import Commodity


def sync_commodities(db: Session, commodities: list):

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


def get_all_commodities(db: Session):

    commodities = db.query(Commodity).all()

    return commodities