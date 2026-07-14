from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import CropSeasonCreate
from services import crop_season_service
from database.database import get_db

router = APIRouter()


@router.post("/crop-seasons")
def create_crop_season(crop: CropSeasonCreate,
                       db: Session = Depends(get_db)):
    return crop_season_service.add_crop_season(db, crop)


@router.get("/crop-seasons")
def get_all_crop_seasons(db: Session = Depends(get_db)):
    return crop_season_service.get_all_crop_seasons(db)


@router.get("/crop-seasons/{crop_id}")
def get_crop_season(crop_id: int,
                    db: Session = Depends(get_db)):
    return crop_season_service.get_crop_season(db, crop_id)


@router.put("/crop-seasons/{crop_id}")
def update_crop_season(crop_id: int,
                       crop: CropSeasonCreate,
                       db: Session = Depends(get_db)):
    return crop_season_service.update_crop_season(db, crop_id, crop)


@router.delete("/crop-seasons/{crop_id}")
def delete_crop_season(crop_id: int,
                       db: Session = Depends(get_db)):
    return crop_season_service.delete_crop_season(db, crop_id)