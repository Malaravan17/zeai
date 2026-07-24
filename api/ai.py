from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from ai_services.ai_service import process_question

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.get("/test")
def test_ai(
    farm_id: int,
    question: str,
    db: Session = Depends(get_db)
):

    return process_question(
        db,
        farm_id,
        question
    )