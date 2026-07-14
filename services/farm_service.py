from sqlalchemy.orm import Session

from models.farm import Farm
from schemas import FarmCreate


# =====================================
# Create Farm
# =====================================
def add_farm(
    db: Session,
    farm: FarmCreate
):

    new_farm = Farm(
        user_id=farm.user_id,
        farm_name=farm.farm_name,
        district=farm.district,
        state=farm.state,
        latitude=farm.latitude,
        longitude=farm.longitude,
        area=farm.area,
        soil_type=farm.soil_type,
        irrigation_type=farm.irrigation_type
    )

    db.add(new_farm)
    db.commit()
    db.refresh(new_farm)

    return new_farm


# =====================================
# Get All Farms
# =====================================
def get_all_farms(db: Session):

    farms = db.query(Farm).all()

    return farms


# =====================================
# Get Farm By ID
# =====================================
def get_farm(
    db: Session,
    farm_id: int
):

    farm = db.query(Farm).filter(
        Farm.id == farm_id
    ).first()

    return farm


# =====================================
# Update Farm
# =====================================
def update_farm(
    db: Session,
    farm_id: int,
    farm: FarmCreate
):

    existing_farm = db.query(Farm).filter(
        Farm.id == farm_id
    ).first()

    existing_farm.user_id = farm.user_id
    existing_farm.farm_name = farm.farm_name
    existing_farm.district = farm.district
    existing_farm.state = farm.state
    existing_farm.latitude = farm.latitude
    existing_farm.longitude = farm.longitude
    existing_farm.area = farm.area
    existing_farm.soil_type = farm.soil_type
    existing_farm.irrigation_type = farm.irrigation_type

    db.commit()
    db.refresh(existing_farm)

    return existing_farm


# =====================================
# Delete Farm
# =====================================
def delete_farm(
    db: Session,
    farm_id: int
):

    farm = db.query(Farm).filter(
        Farm.id == farm_id
    ).first()

    db.delete(farm)
    db.commit()

    return {
        "message": "Farm Deleted Successfully"
    }