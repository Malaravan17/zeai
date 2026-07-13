from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    phone = Column(String(20), unique=True, nullable=False)

    preferred_language = Column(String(30), default="English")



    farms = relationship("Farm", back_populates="owner")
    chat_history = relationship("ChatHistory",back_populates="user")
    notifications = relationship("Notification",back_populates="user")
    comments = relationship("Comment",back_populates="user")