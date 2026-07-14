from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import Base


class Comment(Base):

    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)

    post_id = Column(Integer,ForeignKey("community_posts.id"))

    user_id = Column(Integer,ForeignKey("users.id"))

    comment = Column(String(1000))

    created_at = Column(DateTime,default=datetime.utcnow)

    post = relationship("CommunityPost",back_populates="comments")

    user = relationship("User",back_populates="comments")