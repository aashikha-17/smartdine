from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Restaurant

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

@router.get("/popular")
def popular(db: Session = Depends(get_db)):
    return db.query(Restaurant).order_by(Restaurant.rating.desc()).limit(3).all()

@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    r = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Not found")
    return r
