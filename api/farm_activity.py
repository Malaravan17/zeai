from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import FarmActivityCreate
from services import farm_activity_service
from database.database import get_db

router = APIRouter()


@router.post("/activities")
def create_activity(activity: FarmActivityCreate,
                    db: Session = Depends(get_db)):
    return farm_activity_service.add_activity(db, activity)


@router.get("/activities")
def get_all_activities(db: Session = Depends(get_db)):
    return farm_activity_service.get_all_activities(db)


@router.get("/activities/{activity_id}")
def get_activity(activity_id: int,
                 db: Session = Depends(get_db)):
    return farm_activity_service.get_activity(db, activity_id)


@router.put("/activities/{activity_id}")
def update_activity(activity_id: int,
                    activity: FarmActivityCreate,
                    db: Session = Depends(get_db)):
    return farm_activity_service.update_activity(db, activity_id, activity)


@router.delete("/activities/{activity_id}")
def delete_activity(activity_id: int,
                    db: Session = Depends(get_db)):
    return farm_activity_service.delete_activity(db, activity_id)