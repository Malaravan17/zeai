from schemas import UserCreate


def add_user(user: UserCreate):

    return {
        "message": "User Created Successfully",
        "user": user
    }


def get_all_users():

    return {
        "message": "All Users",
        "data": []
    }


def get_user(user_id: int):

    return {
        "message": "User Found",
        "user_id": user_id
    }


def update_user(user_id: int,
                user: UserCreate):

    return {
        "message": "User Updated Successfully",
        "user_id": user_id,
        "user": user
    }


def delete_user(user_id: int):

    return {
        "message": "User Deleted Successfully",
        "user_id": user_id
    }