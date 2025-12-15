from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cuisine = Column(String, nullable=False)
    price_range = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    image_url = Column(String, nullable=False)

    # ✅ ADD THIS INIT (KEY FIX)
    def __init__(
        self,
        name: str,
        cuisine: str,
        price_range: str,
        rating: float,
        latitude: float,
        longitude: float,
        image_url: str
    ):
        self.name = name
        self.cuisine = cuisine
        self.price_range = price_range
        self.rating = rating
        self.latitude = latitude
        self.longitude = longitude
        self.image_url = image_url
