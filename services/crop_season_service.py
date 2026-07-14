from sqlalchemy.orm import Session
from models.crop_season import CropSeason

from schemas import CropSeasonCreate


def add_crop_season(db: Session, crop: CropSeasonCreate):

    new_crop = CropSeason(
        farm_id=crop.farm_id,
        crop_name=crop.crop_name,
        variety=crop.variety,
        sowing_date=crop.sowing_date,
        expected_harvest=crop.expected_harvest,
        growth_stage=crop.growth_stage,
        status=crop.status
    )

    db.add(new_crop)
    db.commit()
    db.refresh(new_crop)

    return new_crop


def get_all_crop_seasons(db: Session):

    crops = db.query(CropSeason).all()

    return crops


def get_crop_season(db: Session, crop_id: int):

    crop = db.query(CropSeason).filter(
        CropSeason.id == crop_id
    ).first()

    return crop


def update_crop_season(db: Session,
                       crop_id: int,
                       crop: CropSeasonCreate):

    existing_crop = db.query(CropSeason).filter(
        CropSeason.id == crop_id
    ).first()

    existing_crop.farm_id = crop.farm_id
    existing_crop.crop_name = crop.crop_name
    existing_crop.variety = crop.variety
    existing_crop.sowing_date = crop.sowing_date
    existing_crop.expected_harvest = crop.expected_harvest
    existing_crop.growth_stage = crop.growth_stage
    existing_crop.status = crop.status

    db.commit()
    db.refresh(existing_crop)

    return existing_crop


def delete_crop_season(db: Session, crop_id: int):

    crop = db.query(CropSeason).filter(
        CropSeason.id == crop_id
    ).first()

    db.delete(crop)
    db.commit()

    return {
        "message": "Crop Season Deleted Successfully"
    }