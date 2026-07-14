from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import ChatHistoryCreate
from services import chat_service
from database.database import get_db

router = APIRouter()


@router.post("/chats")
def create_chat(chat: ChatHistoryCreate,
                db: Session = Depends(get_db)):
    return chat_service.add_chat(db, chat)


@router.get("/chats")
def get_all_chats(db: Session = Depends(get_db)):
    return chat_service.get_all_chats(db)


@router.get("/chats/{chat_id}")
def get_chat(chat_id: int,
             db: Session = Depends(get_db)):
    return chat_service.get_chat(db, chat_id)


@router.delete("/chats/{chat_id}")
def delete_chat(chat_id: int,
                db: Session = Depends(get_db)):
    return chat_service.delete_chat(db, chat_id)