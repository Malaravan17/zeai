from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database.base import Base


class Commodity(Base):

    __tablename__ = "commodities"

    id = Column(Integer, primary_key=True)

    commodity_id = Column(Integer, unique=True)

    commodity_name = Column(String(100))