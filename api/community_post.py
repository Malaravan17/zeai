from fastapi import APIRouter
from schemas import CommunityPostCreate
from services import community_post_service

router = APIRouter()


@router.post("/posts")
def create_post(post: CommunityPostCreate):
    return community_post_service.add_post(post)


@router.get("/posts")
def get_all_posts():
    return community_post_service.get_all_posts()


@router.get("/posts/{post_id}")
def get_post(post_id: int):
    return community_post_service.get_post(post_id)


@router.put("/posts/{post_id}")
def update_post(post_id: int,
                post: CommunityPostCreate):
    return community_post_service.update_post(
        post_id,
        post
    )


@router.delete("/posts/{post_id}")
def delete_post(post_id: int):
    return community_post_service.delete_post(post_id)