from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import CommentCreate
from services import comment_service
from database.database import get_db

router = APIRouter()


@router.post("/comments")
def create_comment(comment: CommentCreate,
                   db: Session = Depends(get_db)):
    return comment_service.add_comment(db, comment)


@router.get("/posts/{post_id}/comments")
def get_comments(post_id: int,
                 db: Session = Depends(get_db)):
    return comment_service.get_comments(db, post_id)


@router.put("/comments/{comment_id}")
def update_comment(comment_id: int,
                   comment: CommentCreate,
                   db: Session = Depends(get_db)):
    return comment_service.update_comment(db, comment_id, comment)


@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int,
                   db: Session = Depends(get_db)):
    return comment_service.delete_comment(db, comment_id)