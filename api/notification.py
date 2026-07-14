from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services import notification_service
from database.database import get_db

router = APIRouter()


@router.get("/notifications")
def get_notifications(db: Session = Depends(get_db)):
    return notification_service.get_notifications(db)


@router.get("/notifications/{notification_id}")
def get_notification(notification_id: int,
                     db: Session = Depends(get_db)):
    return notification_service.get_notification(db, notification_id)


@router.patch("/notifications/{notification_id}/read")
def mark_as_read(notification_id: int,
                 db: Session = Depends(get_db)):
    return notification_service.mark_as_read(db, notification_id)