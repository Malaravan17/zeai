from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class Market(Base):

    __tablename__ = "markets"

    id = Column(Integer, primary_key=True)

    market_id = Column(Integer, unique=True)

    market_name = Column(String(100))

    district_id = Column(
        Integer,
        ForeignKey("districts.id")
    )

    district = relationship(
        "District",
        back_populates="markets"
    )