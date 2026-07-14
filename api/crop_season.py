from fastapi import APIRouter
from schemas import CropSeasonCreate
from services import crop_season_service

router = APIRouter()


@router.post("/crop-seasons")
def create_crop_season(crop: CropSeasonCreate):
    return crop_season_service.add_crop_season(crop)


@router.get("/crop-seasons")
def get_all_crop_seasons():
    return crop_season_service.get_all_crop_seasons()


@router.get("/crop-seasons/{crop_id}")
def get_crop_season(crop_id: int):
    return crop_season_service.get_crop_season(crop_id)


@router.put("/crop-seasons/{crop_id}")
def update_crop_season(crop_id: int,
                       crop: CropSeasonCreate):
    return crop_season_service.update_crop_season(
        crop_id,
        crop
    )


@router.delete("/crop-seasons/{crop_id}")
def delete_crop_season(crop_id: int):
    return crop_season_service.delete_crop_season(crop_id)