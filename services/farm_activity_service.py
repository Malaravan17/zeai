from sqlalchemy.orm import Session
from models.farm_activity import FarmActivity

from schemas import FarmActivityCreate


def add_activity(db: Session, activity: FarmActivityCreate):

    new_activity = FarmActivity(
        crop_season_id=activity.crop_season_id,
        activity_date=activity.activity_date,
        activity_type=activity.activity_type,
        description=activity.description,
        notes=activity.notes
    )

    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity


def get_all_activities(db: Session):

    activities = db.query(FarmActivity).all()

    return activities


def get_activity(db: Session, activity_id: int):

    activity = db.query(FarmActivity).filter(
        FarmActivity.id == activity_id
    ).first()

    return activity


def update_activity(db: Session,
                    activity_id: int,
                    activity: FarmActivityCreate):

    existing_activity = db.query(FarmActivity).filter(
        FarmActivity.id == activity_id
    ).first()

    existing_activity.crop_season_id = activity.crop_season_id
    existing_activity.activity_date = activity.activity_date
    existing_activity.activity_type = activity.activity_type
    existing_activity.description = activity.description
    existing_activity.notes = activity.notes

    db.commit()
    db.refresh(existing_activity)

    return existing_activity


def delete_activity(db: Session, activity_id: int):

    activity = db.query(FarmActivity).filter(
        FarmActivity.id == activity_id
    ).first()

    db.delete(activity)
    db.commit()

    return {
        "message": "Activity Deleted Successfully"
    }