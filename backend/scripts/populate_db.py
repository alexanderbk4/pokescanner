from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models
from datetime import date

def populate_initial_data():
    db = SessionLocal()
    
    try:
        # Create some initial sets
        sets = [
            models.CardSet(
                name="Base Set",
                code="BS1",
                release_date=date(1999, 1, 9),
                total_cards=102
            ),
            models.CardSet(
                name="Jungle",
                code="JU",
                release_date=date(1999, 6, 16),
                total_cards=64
            ),
            models.CardSet(
                name="Fossil",
                code="FO",
                release_date=date(1999, 10, 10),
                total_cards=62
            )
        ]
        
        for card_set in sets:
            db.add(card_set)
        
        db.commit()
        
        # Create some sample cards
        cards = [
            models.Card(
                name="Charizard",
                set_name="Base Set",
                set_code="BS1",
                card_number="4/102",
                rarity="Rare Holo",
                image_url="https://images.pokemontcg.io/base1/4_hires.png"
            ),
            models.Card(
                name="Blastoise",
                set_name="Base Set",
                set_code="BS1",
                card_number="2/102",
                rarity="Rare Holo",
                image_url="https://images.pokemontcg.io/base1/2_hires.png"
            ),
            models.Card(
                name="Venusaur",
                set_name="Base Set",
                set_code="BS1",
                card_number="15/102",
                rarity="Rare Holo",
                image_url="https://images.pokemontcg.io/base1/15_hires.png"
            )
        ]
        
        for card in cards:
            db.add(card)
        
        db.commit()
        print("Successfully populated database with initial data!")
        
    except Exception as e:
        print(f"Error populating database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    # Create all tables
    models.Base.metadata.create_all(bind=engine)
    # Populate initial data
    populate_initial_data() 