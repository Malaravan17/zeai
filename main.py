from fastapi import FastAPI

from api.user import router as user_router
from api.farm import router as farm_router
from api.crop_season import router as crop_season_router
from api.farm_activity import router as farm_activity_router
from api.disease_report import router as disease_report_router
from api.chat import router as chat_router
from api.notification import router as notification_router
from api.community_post import router as community_post_router
from api.comment import router as comment_router
from database.database import engine
from database.base import Base
from api import weather


from models.user import User
from models.farm import Farm
from models.chat_history import ChatHistory
from models.crop_season import CropSeason
from models.farm_activity import FarmActivity
from models.disease_report import DiseaseReport
from models.notification import Notification
from models.community_post import CommunityPost
from models.comment import Comment

app = FastAPI(
    title="AI Farmer Advisory System",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(farm_router)
app.include_router(crop_season_router)
app.include_router(farm_activity_router)
app.include_router(disease_report_router)
app.include_router(chat_router)
app.include_router(notification_router)
app.include_router(community_post_router)
app.include_router(comment_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Farmer Advisory System"
    }

app.include_router(
    weather.router,                                                     #WEATHER API ROUTER
    tags=["Weather"]
)