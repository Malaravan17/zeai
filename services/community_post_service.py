from schemas import CommunityPostCreate


def add_post(post: CommunityPostCreate):

    return {
        "message": "Post Created Successfully",
        "post": post
    }


def get_all_posts():

    return {
        "message": "All Posts",
        "data": []
    }


def get_post(post_id: int):

    return {
        "message": "Post Found",
        "post_id": post_id
    }


def update_post(post_id: int,
                post: CommunityPostCreate):

    return {
        "message": "Post Updated Successfully",
        "post_id": post_id,
        "post": post
    }


def delete_post(post_id: int):

    return {
        "message": "Post Deleted Successfully",
        "post_id": post_id
    }