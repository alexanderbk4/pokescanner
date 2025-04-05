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
        # Get all sets from the database
        sets = db.execute(text("SELECT code FROM card_sets")).fetchall()
        
        for set_code in sets:
            print(f"\nSyncing set: {set_code[0]}")
            try:
                sync_service.sync_cards(set_code[0])
                print(f"Successfully synced set {set_code[0]}")
            except Exception as e:
                print(f"Error syncing set {set_code[0]}: {str(e)}")
                continue
        
        print("\nAll sets have been synced!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    sync_all_sets() 