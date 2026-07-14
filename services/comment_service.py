from sqlalchemy.orm import Session
from models.comment import Comment

from schemas import CommentCreate


def add_comment(db: Session,
                comment: CommentCreate):

    new_comment = Comment(
        post_id=comment.post_id,
        user_id=comment.user_id,
        comment=comment.comment
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


def get_comments(db: Session,
                 post_id: int):

    comments = db.query(Comment).filter(
        Comment.post_id == post_id
    ).all()

    return comments


def update_comment(db: Session,
                   comment_id: int,
                   comment: CommentCreate):

    existing_comment = db.query(Comment).filter(
        Comment.id == comment_id
    ).first()

    existing_comment.post_id = comment.post_id
    existing_comment.user_id = comment.user_id
    existing_comment.comment = comment.comment

    db.commit()
    db.refresh(existing_comment)

    return existing_comment


def delete_comment(db: Session,
                   comment_id: int):

    comment = db.query(Comment).filter(
        Comment.id == comment_id
    ).first()

    db.delete(comment)
    db.commit()

    return {
        "message": "Comment Deleted Successfully"
    }