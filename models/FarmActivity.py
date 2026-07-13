from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from unittest.mock import Base


from app.database.base import Base


class FarmActivity(Base):

    __tablename__ = "farm_activities"

    id = Column(Integer, primary_key=True)

    crop_season_id = Column(Integer,ForeignKey("crop_seasons.id"))

    activity_date = Column(Date)

    activity_type = Column(String(100))

    description = Column(String(500))

    notes = Column(String(500))

    crop_season = relationship("CropSeason",back_populates="activities")