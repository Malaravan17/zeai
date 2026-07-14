from sqlalchemy.orm import Session
from models.user import User

from schemas import UserCreate


def add_user(db: Session, user: UserCreate):
    new_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        preferred_language=user.preferred_language        
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db: Session):
    users = db.query(User).all()

    return users


def get_user(db: Session, user_id: int):
     
    user = db.query(User).filter(
        User.id == user_id
    ).first()
     
    return user

def update_user(db: Session, user_id: int, user: UserCreate):

    existing_user = db.query(User).filter(
        User.id == user_id
    ).first()

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.phone = user.phone
    existing_user.preferred_language = user.preferred_language

    db.commit()
    db.refresh(existing_user)

    return existing_user
    


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    db.delete(user)
    db.commit()

    return {
        "message": "User Deleted Successfully"
    }