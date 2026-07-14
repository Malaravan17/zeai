from schemas import CommentCreate


def add_comment(comment: CommentCreate):

    return {
        "message": "Comment Added Successfully",
        "comment": comment
    }


def get_comments(post_id: int):

    return {
        "message": "Comments for Post",
        "post_id": post_id,
        "data": []
    }


def update_comment(comment_id: int,
                   comment: CommentCreate):

    return {
        "message": "Comment Updated Successfully",
        "comment_id": comment_id,
        "comment": comment
    }


def delete_comment(comment_id: int):

    return {
        "message": "Comment Deleted Successfully",
        "comment_id": comment_id
    }