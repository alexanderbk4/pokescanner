from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.services.card_sync_service import CardSyncService
from app import models
import os
from dotenv import load_dotenv

load_dotenv()

def sync_base_set():
    # Create database tables
    models.Base.metadata.create_all(bind=engine)
    
    # Create a database session
    db = SessionLocal()
    
    try:
        # Initialize the sync service
        sync_service = CardSyncService(db)
        
        # Sync only Base Set cards
        print("Syncing Base Set cards...")
        sync_service.sync_cards(set_code="base1")
        
        print("Successfully synced Base Set cards!")
        
    except Exception as e:
        print(f"Error syncing cards: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    sync_base_set() 