from fastapi import APIRouter
from schemas import FarmActivityCreate
from services import farm_activity_service

router = APIRouter()


@router.post("/activities")
def create_activity(activity: FarmActivityCreate):
    return farm_activity_service.add_activity(activity)


@router.get("/activities")
def get_all_activities():
    return farm_activity_service.get_all_activities()


@router.get("/activities/{activity_id}")
def get_activity(activity_id: int):
    return farm_activity_service.get_activity(activity_id)


@router.put("/activities/{activity_id}")
def update_activity(activity_id: int,
                    activity: FarmActivityCreate):
    return farm_activity_service.update_activity(
        activity_id,
        activity
    )


@router.delete("/activities/{activity_id}")
def delete_activity(activity_id: int):
    return farm_activity_service.delete_activity(activity_id)