import sys
import os
from datetime import datetime
from sqlalchemy import text

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.card_sync_service import CardSyncService
from app.database import SessionLocal

def sync_all_sets():
    db = SessionLocal()
    sync_service = CardSyncService(db)
    
    try:
        # First, sync all sets to get the complete list
        print("Syncing all sets from the API...")
        sync_service.sync_sets()
        
        # Get all sets from the database, ordered by release date
        sets = db.execute(text("""
            SELECT code 
            FROM card_sets 
            ORDER BY release_date DESC
        """)).fetchall()
        
        # Skip the first 100 sets and sync the rest
        new_sets = sets[100:]
        total_sets = len(new_sets)
        print(f"\nFound {total_sets} new sets to sync")
        
        # Sync cards for each new set
        for i, set_code in enumerate(new_sets, 1):
            print(f"\nSyncing set {i}/{total_sets}: {set_code[0]}")
            try:
                sync_service.sync_cards(set_code[0])
                print(f"Successfully synced set {set_code[0]}")
            except Exception as e:
                print(f"Error syncing set {set_code[0]}: {str(e)}")
                continue
        
        print("\nAll new sets have been synced!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    sync_all_sets() 