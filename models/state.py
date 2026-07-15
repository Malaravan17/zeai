from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class State(Base):

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)

    state_id = Column(Integer, unique=True)

    state_name = Column(String(100), unique=True)

    districts = relationship(
        "District",
        back_populates="state"
    )