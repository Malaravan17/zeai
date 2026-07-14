from schemas import CropSeasonCreate


def add_crop_season(crop: CropSeasonCreate):

    return {
        "message": "Crop Season Added",
        "crop": crop
    }


def get_all_crop_seasons():

    return {
        "message": "All Crop Seasons",
        "data": []
    }


def get_crop_season(crop_id: int):

    return {
        "message": "Crop Season Found",
        "crop_id": crop_id
    }


def update_crop_season(
        crop_id: int,
        crop: CropSeasonCreate
):

    return {
        "message": "Crop Season Updated",
        "crop_id": crop_id,
        "crop": crop
    }


def delete_crop_season(crop_id: int):

    return {
        "message": "Crop Season Deleted",
        "crop_id": crop_id
    }