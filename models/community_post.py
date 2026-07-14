from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database.base import Base


class CommunityPost(Base):

    __tablename__ = "community_posts"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer,ForeignKey("users.id"))

    title = Column(String(200))

    description = Column(String(1000))

    image_path = Column(String(255))

    created_at = Column(DateTime,default=datetime.utcnow)

    user = relationship("User",back_populates="community_post")

    comments = relationship("Comment",back_populates="post")