import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Restaurant

router = APIRouter(prefix="/surprise")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("")
def surprise(db: Session = Depends(get_db)):
    restaurants = db.query(Restaurant).all()
    r = random.choice(restaurants)

    return {
        "id": r.id,
        "name": r.name,
        "cuisine": r.cuisine,
        "rating": r.rating,
        "latitude": r.latitude,
        "longitude": r.longitude,
        "image_url": r.image_url,
        "reason": "Feeling adventurous? Here’s a surprise pick!"
    }
