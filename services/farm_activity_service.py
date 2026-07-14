from schemas import FarmActivityCreate


def add_activity(activity: FarmActivityCreate):

    return {
        "message": "Activity Added Successfully",
        "activity": activity
    }


def get_all_activities():

    return {
        "message": "All Activities",
        "data": []
    }


def get_activity(activity_id: int):

    return {
        "message": "Activity Found",
        "activity_id": activity_id
    }


def update_activity(activity_id: int,
                    activity: FarmActivityCreate):

    return {
        "message": "Activity Updated Successfully",
        "activity_id": activity_id,
        "activity": activity
    }


def delete_activity(activity_id: int):

    return {
        "message": "Activity Deleted Successfully",
        "activity_id": activity_id
    }