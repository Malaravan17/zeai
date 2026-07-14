from sqlalchemy.orm import Session
from models.community_post import CommunityPost

from schemas import CommunityPostCreate


def add_post(db: Session,
             post: CommunityPostCreate):

    new_post = CommunityPost(
        user_id=post.user_id,
        title=post.title,
        description=post.description,
        image_path=post.image_path
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def get_all_posts(db: Session):

    posts = db.query(CommunityPost).all()

    return posts


def get_post(db: Session,
             post_id: int):

    post = db.query(CommunityPost).filter(
        CommunityPost.id == post_id
    ).first()

    return post


def update_post(db: Session,
                post_id: int,
                post: CommunityPostCreate):

    existing_post = db.query(CommunityPost).filter(
        CommunityPost.id == post_id
    ).first()

    existing_post.user_id = post.user_id
    existing_post.title = post.title
    existing_post.description = post.description
    existing_post.image_path = post.image_path

    db.commit()
    db.refresh(existing_post)

    return existing_post


def delete_post(db: Session,
                post_id: int):

    post = db.query(CommunityPost).filter(
        CommunityPost.id == post_id
    ).first()

    db.delete(post)
    db.commit()

    return {
        "message": "Post Deleted Successfully"
    }