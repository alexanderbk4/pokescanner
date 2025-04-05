from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import os
from dotenv import load_dotenv
from . import models, schemas
from .database import get_db, engine

# Load environment variables
load_dotenv()

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Pokémon Card Scanner API",
    description="Backend API for the Pokémon Card Scanner application",
    version="0.1.0"
)

# Get API URL from environment variable
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(request: Request):
    # Get the actual server URL from the request
    server_url = str(request.base_url).rstrip('/')
    return {
        "message": "Welcome to the Pokémon Card Scanner API",
        "server_url": server_url
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Card endpoints
@app.get("/cards/", response_model=List[schemas.Card])
def get_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cards = db.query(models.Card).offset(skip).limit(limit).all()
    return cards

@app.get("/cards/{card_id}", response_model=schemas.Card)
def get_card(card_id: int, db: Session = Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == card_id).first()
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

@app.get("/cards/set/{set_code}", response_model=List[schemas.Card])
def get_cards_by_set(set_code: str, db: Session = Depends(get_db)):
    cards = db.query(models.Card).filter(models.Card.set_code == set_code).all()
    return cards

# Set endpoints
@app.get("/sets/", response_model=List[schemas.CardSet])
def get_sets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sets = db.query(models.CardSet).offset(skip).limit(limit).all()
    return sets

@app.get("/sets/{set_code}", response_model=schemas.CardSetWithCards)
def get_set(set_code: str, db: Session = Depends(get_db)):
    card_set = db.query(models.CardSet).filter(models.CardSet.code == set_code).first()
    if card_set is None:
        raise HTTPException(status_code=404, detail="Set not found")
    
    cards = db.query(models.Card).filter(models.Card.set_code == set_code).all()
    return schemas.CardSetWithCards(
        **card_set.__dict__,
        cards=cards
    ) 