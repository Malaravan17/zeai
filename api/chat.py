from fastapi import APIRouter
from schemas import ChatHistoryCreate
from services import chat_service

router = APIRouter()


@router.post("/chats")
def create_chat(chat: ChatHistoryCreate):
    return chat_service.add_chat(chat)


@router.get("/chats")
def get_all_chats():
    return chat_service.get_all_chats()


@router.get("/chats/{chat_id}")
def get_chat(chat_id: int):
    return chat_service.get_chat(chat_id)


@router.delete("/chats/{chat_id}")
def delete_chat(chat_id: int):
    return chat_service.delete_chat(chat_id)