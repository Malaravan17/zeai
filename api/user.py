from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from schemas import UserCreate
from services import user_service
from database.database import get_db

router = APIRouter()


@router.post("/users")
def create_user(user: UserCreate,db: Session = Depends(get_db)):

    return user_service.add_user(db, user)


@router.get("/users")
def get_all_users( db: Session = Depends(get_db)):
    return user_service.get_all_users(db)


@router.get("/users/{user_id}")
def get_user(user_id: int,db: Session = Depends(get_db)):
    return user_service.get_user(db,user_id)


@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    return user_service.update_user(user_id, user)


@router.delete("/users/{user_id}")
def delete_user(user_id: int,db: Session = Depends(get_db)):
    return user_service.delete_user(user_id,db)