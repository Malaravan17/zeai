from sqlalchemy.orm import Session
from models.chat_history import ChatHistory

from schemas import ChatHistoryCreate


def add_chat(db: Session, chat: ChatHistoryCreate):

    new_chat = ChatHistory(
        user_id=chat.user_id,
        question=chat.question,
        answer=chat.answer
    )

    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)

    return new_chat


def get_all_chats(db: Session):

    chats = db.query(ChatHistory).all()

    return chats


def get_chat(db: Session, chat_id: int):

    chat = db.query(ChatHistory).filter(
        ChatHistory.id == chat_id
    ).first()

    return chat


def delete_chat(db: Session, chat_id: int):

    chat = db.query(ChatHistory).filter(
        ChatHistory.id == chat_id
    ).first()

    db.delete(chat)
    db.commit()

    return {
        "message": "Chat Deleted Successfully"
    }