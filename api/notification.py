from fastapi import APIRouter
from services import notification_service

router = APIRouter()


@router.get("/notifications")
def get_notifications():
    return notification_service.get_notifications()


@router.get("/notifications/{notification_id}")
def get_notification(notification_id: int):
    return notification_service.get_notification(notification_id)


@router.patch("/notifications/{notification_id}/read")
def mark_as_read(notification_id: int):
    return notification_service.mark_as_read(notification_id)