from fastapi import APIRouter
from pydantic import BaseModel
from app.services.osm_places import fetch_nearby_restaurants

router = APIRouter(prefix="/recommend", tags=["Places"])

class PlaceReq(BaseModel):
    prompt: str
    lat: float
    lon: float

@router.post("")
def recommend(req: PlaceReq):
    places = fetch_nearby_restaurants(req.lat, req.lon)

    explanation = f"Found {len(places)} restaurants near you matching your request."

    return {
        "places": places,
        "explanation": explanation
    }
