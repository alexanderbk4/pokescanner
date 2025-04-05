from typing import Dict, List
from sqlalchemy.orm import Session
from .pokemon_tcg_client import PokemonTCGClient
from ..models import Card, CardSet
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class CardSyncService:
    def __init__(self, db: Session):
        self.db = db
        api_key = os.getenv("POKEMON_TCG_API_KEY", "")
        self.tcg_client = PokemonTCGClient(api_key)

    def sync_sets(self) -> None:
        """Sync all card sets from the Pokémon TCG API."""
        page = 1
        while True:
            response = self.tcg_client.get_sets(page=page)
            sets_data = response.get("data", [])
            
            if not sets_data:
                break

            for set_data in sets_data:
                # Try different date formats
                release_date = None
                if set_data.get("releaseDate"):
                    date_formats = ["%Y-%m-%d", "%Y/%m/%d"]
                    for date_format in date_formats:
                        try:
                            release_date = datetime.strptime(set_data["releaseDate"], date_format).date()
                            break
                        except ValueError:
                            continue

                card_set = CardSet(
                    name=set_data["name"],
                    code=set_data["id"],
                    release_date=release_date,
                    total_cards=set_data.get("total")
                )
                
                # Check if set exists
                existing_set = self.db.query(CardSet).filter(CardSet.code == set_data["id"]).first()
                if existing_set:
                    # Update existing set
                    for key, value in card_set.__dict__.items():
                        if not key.startswith("_"):
                            setattr(existing_set, key, value)
                else:
                    # Add new set
                    self.db.add(card_set)
            
            self.db.commit()
            page += 1

    def sync_cards(self, set_code: str = None) -> None:
        """Sync cards from the Pokémon TCG API."""
        page = 1
        while True:
            response = self.tcg_client.get_cards(page=page, set_id=set_code)
            cards_data = response.get("data", [])
            
            if not cards_data:
                break

            for card_data in cards_data:
                # Get or create card set
                set_code = card_data["set"]["id"]
                card_set = self.db.query(CardSet).filter(CardSet.code == set_code).first()
                if not card_set:
                    # If set doesn't exist, sync it first
                    self.sync_sets()
                    card_set = self.db.query(CardSet).filter(CardSet.code == set_code).first()

                # Create or update card
                card = Card(
                    name=card_data.get("name", "Unknown"),
                    set_name=card_data["set"].get("name", "Unknown"),
                    set_code=set_code,
                    card_number=card_data.get("number", "0"),
                    rarity=card_data.get("rarity", "Unknown"),
                    image_url=card_data.get("images", {}).get("large")
                )

                # Check if card exists
                existing_card = self.db.query(Card).filter(
                    Card.set_code == set_code,
                    Card.card_number == card_data.get("number", "0")
                ).first()

                if existing_card:
                    # Update existing card
                    for key, value in card.__dict__.items():
                        if not key.startswith("_"):
                            setattr(existing_card, key, value)
                else:
                    # Add new card
                    self.db.add(card)
            
            self.db.commit()
            page += 1

    def sync_all(self) -> None:
        """Sync all sets and cards."""
        self.sync_sets()
        self.sync_cards() 