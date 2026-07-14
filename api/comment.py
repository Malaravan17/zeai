from fastapi import APIRouter
from schemas import CommentCreate
from services import comment_service

router = APIRouter()


@router.post("/comments")
def create_comment(comment: CommentCreate):
    return comment_service.add_comment(comment)


@router.get("/posts/{post_id}/comments")
def get_comments(post_id: int):
    return comment_service.get_comments(post_id)


@router.put("/comments/{comment_id}")
def update_comment(comment_id: int,
                   comment: CommentCreate):
    return comment_service.update_comment(
        comment_id,
        comment
    )


@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int):
    return comment_service.delete_comment(comment_id)