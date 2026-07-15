from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class District(Base):

    __tablename__ = "districts"

    id = Column(Integer, primary_key=True)

    district_id = Column(Integer, unique=True)

    district_name = Column(String(100))

    state_id = Column(
        Integer,
        ForeignKey("states.id")
    )

    state = relationship(
        "State",
        back_populates="districts"
    )

    markets = relationship(
        "Market",
        back_populates="district"
    )