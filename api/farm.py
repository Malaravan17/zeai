from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import FarmCreate
from services import farm_service
from database.database import get_db

router = APIRouter()


@router.post("/farms")
def create_farm(farm: FarmCreate,
                db: Session = Depends(get_db)):
    return farm_service.add_farm(db, farm)


@router.get("/farms")
def get_all_farms(db: Session = Depends(get_db)):
    return farm_service.get_all_farms(db)


@router.get("/farms/{farm_id}")
def get_farm(farm_id: int,
             db: Session = Depends(get_db)):
    return farm_service.get_farm(db, farm_id)


@router.put("/farms/{farm_id}")
def update_farm(farm_id: int,
                farm: FarmCreate,
                db: Session = Depends(get_db)):
    return farm_service.update_farm(db, farm_id, farm)


@router.delete("/farms/{farm_id}")
def delete_farm(farm_id: int,
                db: Session = Depends(get_db)):
    return farm_service.delete_farm(db, farm_id)