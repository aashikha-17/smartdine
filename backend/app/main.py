from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.seed_data import seed_restaurants
from app.routes import recommend, restaurants, surprise

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartDine API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommend.router)
app.include_router(restaurants.router)
app.include_router(surprise.router)

@app.on_event("startup")
def startup():
    seed_restaurants()
