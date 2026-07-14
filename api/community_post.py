from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import CommunityPostCreate
from services import community_post_service
from database.database import get_db

router = APIRouter()


@router.post("/posts")
def create_post(post: CommunityPostCreate,
                db: Session = Depends(get_db)):
    return community_post_service.add_post(db, post)


@router.get("/posts")
def get_all_posts(db: Session = Depends(get_db)):
    return community_post_service.get_all_posts(db)


@router.get("/posts/{post_id}")
def get_post(post_id: int,
             db: Session = Depends(get_db)):
    return community_post_service.get_post(db, post_id)


@router.put("/posts/{post_id}")
def update_post(post_id: int,
                post: CommunityPostCreate,
                db: Session = Depends(get_db)):
    return community_post_service.update_post(db, post_id, post)


@router.delete("/posts/{post_id}")
def delete_post(post_id: int,
                db: Session = Depends(get_db)):
    return community_post_service.delete_post(db, post_id)