from schemas import ChatHistoryCreate


def add_chat(chat: ChatHistoryCreate):

    return {
        "message": "Chat Saved Successfully",
        "chat": chat
    }


def get_all_chats():

    return {
        "message": "All Chats",
        "data": []
    }


def get_chat(chat_id: int):

    return {
        "message": "Chat Found",
        "chat_id": chat_id
    }


def delete_chat(chat_id: int):

    return {
        "message": "Chat Deleted",
        "chat_id": chat_id
    }