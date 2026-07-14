def get_notifications():

    return {
        "message": "All Notifications",
        "data": []
    }


def get_notification(notification_id: int):

    return {
        "message": "Notification Found",
        "notification_id": notification_id
    }


def mark_as_read(notification_id: int):

    return {
        "message": "Notification Marked as Read",
        "notification_id": notification_id
    }