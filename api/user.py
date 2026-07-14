from fastapi import APIRouter
from schemas import UserCreate
from services import user_service

router = APIRouter()


@router.post("/users")
def create_user(user: UserCreate):
    return user_service.add_user(user)


@router.get("/users")
def get_all_users():
    return user_service.get_all_users()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return user_service.get_user(user_id)


@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    return user_service.update_user(user_id, user)


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return user_service.delete_user(user_id)