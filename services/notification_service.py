from sqlalchemy.orm import Session
from models.notification import Notification


def get_notifications(db: Session):

    notifications = db.query(Notification).all()

    return notifications


def get_notification(db: Session,
                     notification_id: int):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    return notification


def mark_as_read(db: Session,
                 notification_id: int):

    notification = db.query(Notification).filter(
        Notification.id == notification_id
    ).first()

    notification.is_read = True

    db.commit()
    db.refresh(notification)

    return notification