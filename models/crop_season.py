from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class CropSeason(Base):

    __tablename__ = "crop_seasons"

    id = Column(Integer, primary_key=True)

    farm_id = Column(Integer, ForeignKey("farms.id"))

    crop_name = Column(String(100), nullable=False)

    variety = Column(String(100))

    sowing_date = Column(Date)

    expected_harvest = Column(Date)

    growth_stage = Column(String(50))

    status = Column(String(50))

    farm = relationship("Farm", back_populates="crop_seasons")
    activities = relationship("FarmActivity",back_populates="crop_season")