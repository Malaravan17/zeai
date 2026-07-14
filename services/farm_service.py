from schemas import FarmCreate


def add_farm(farm: FarmCreate):

    return {
        "message": "Farm Created Successfully",
        "farm": farm
    }


def get_all_farms():

    return {
        "message": "All Farms",
        "data": []
    }


def get_farm(farm_id: int):

    return {
        "message": "Farm Found",
        "farm_id": farm_id
    }


def update_farm(
        farm_id: int,
        farm: FarmCreate
):

    return {
        "message": "Farm Updated Successfully",
        "farm_id": farm_id,
        "farm": farm
    }


def delete_farm(farm_id: int):

    return {
        "message": "Farm Deleted Successfully",
        "farm_id": farm_id
    }