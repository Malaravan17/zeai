from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Farm(Base):

    __tablename__ = "farms"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    farm_name = Column(String(100), nullable=False)

    district = Column(String(100))

    state = Column(String(100))

    latitude = Column(Float)

    longitude = Column(Float)

    area = Column(Float)

    soil_type = Column(String(100))

    irrigation_type = Column(String(100))



    owner = relationship("User", back_populates="farms")
    crop_seasons = relationship("CropSeason",back_populates="farm")
    disease_reports = relationship("DiseaseReport",back_populates="farm")