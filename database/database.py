from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.base import Base


DATABASE_URL = "postgresql://postgres:malar@localhost:5432/zeai"


engine = create_engine(
    DATABASE_URL
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()