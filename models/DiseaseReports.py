from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class DiseaseReport(Base):

    __tablename__ = "disease_reports"

    id = Column(Integer, primary_key=True)

    farm_id = Column(Integer,ForeignKey("farms.id"))

    crop_name = Column(String(100))

    image_path = Column(String(255))

    disease_name = Column(String(100))

    confidence = Column(Float)

    treatment = Column(String(500))

    report_date = Column(Date)

    farm = relationship("Farm",back_populates="disease_reports")