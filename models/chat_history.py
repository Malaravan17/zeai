from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.base import Base


class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer,ForeignKey("users.id"))

    question = Column(String(1000))

    answer = Column(String(3000))

    timestamp = Column(DateTime,default=datetime.utcnow)

    user = relationship("User",back_populates="chat_history")