from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Restaurant
from app.recommender import recommend as recommend_logic

router = APIRouter(prefix="/recommend", tags=["Recommend"])

@router.get("")
def recommend_route(
    prompt: str,
    user_lat: float,
    user_lon: float,
    db: Session = Depends(get_db)
):
    restaurants = db.query(Restaurant).all()
    return recommend_logic(prompt, restaurants, user_lat, user_lon)
