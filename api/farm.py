from fastapi import APIRouter
from schemas import FarmCreate
from services import farm_service

router = APIRouter()


# Create
@router.post("/farms")
def create_farm(farm: FarmCreate):
    return farm_service.add_farm(farm)


# Read All
@router.get("/farms")
def get_all_farms():
    return farm_service.get_all_farms()


# Read One
@router.get("/farms/{farm_id}")
def get_farm(farm_id: int):
    return farm_service.get_farm(farm_id)


# Update
@router.put("/farms/{farm_id}")
def update_farm(
        farm_id: int,
        farm: FarmCreate
):
    return farm_service.update_farm(
        farm_id,
        farm
    )


# Delete
@router.delete("/farms/{farm_id}")
def delete_farm(farm_id: int):
    return farm_service.delete_farm(farm_id)