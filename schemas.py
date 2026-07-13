from datetime import date
from pydantic import BaseModel


# ==========================
# User
# ==========================

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    preferred_language: str


# ==========================
# Farm
# ==========================

class FarmCreate(BaseModel):
    user_id: int
    farm_name: str
    district: str
    state: str
    latitude: float
    longitude: float
    area: float
    soil_type: str
    irrigation_type: str


# ==========================
# Crop Season
# ==========================

class CropSeasonCreate(BaseModel):
    farm_id: int
    crop_name: str
    variety: str
    sowing_date: date
    expected_harvest: date
    growth_stage: str
    status: str


# ==========================
# Farm Activity
# ==========================

class FarmActivityCreate(BaseModel):
    crop_season_id: int
    activity_date: date
    activity_type: str
    description: str
    notes: str


# ==========================
# Disease Report
# ==========================

class DiseaseReportCreate(BaseModel):
    farm_id: int
    crop_name: str
    image_path: str
    disease_name: str
    confidence: float
    report_date: date


# ==========================
# Chat History
# ==========================

class ChatHistoryCreate(BaseModel):
    user_id: int
    question: str
    answer: str
    module: str


# ==========================
# Notification
# ==========================

class NotificationCreate(BaseModel):
    user_id: int
    title: str
    message: str
    notification_type: str


# ==========================
# Community Post
# ==========================

class CommunityPostCreate(BaseModel):
    user_id: int
    title: str
    description: str
    image_path: str


# ==========================
# Comment
# ==========================

class CommentCreate(BaseModel):
    post_id: int
    user_id: int
    comment: str