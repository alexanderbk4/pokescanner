from typing import Dict, List
from sqlalchemy.orm import Session
from .pokemon_tcg_client import PokemonTCGClient
from ..models import Card, CardSet, PriceHistory
from datetime import datetime

class CardSyncService:
    def __init__(self, db: Session):
        self.db = db
        self.tcg_client = PokemonTCGClient()

    def sync_sets(self) -> None:
        """Sync all card sets from the Pokémon TCG API."""
        page = 1
        while True:
            response = self.tcg_client.get_sets(page=page)
            sets_data = response.get("data", [])
            
            if not sets_data:
                break

            for set_data in sets_data:
                card_set = CardSet(
                    name=set_data["name"],
                    code=set_data["id"],
                    release_date=datetime.strptime(set_data["releaseDate"], "%Y-%m-%d").date() if set_data.get("releaseDate") else None,
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
            query = f"set.id:{set_code}" if set_code else None
            response = self.tcg_client.get_cards(page=page, query=query)
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
                    name=card_data["name"],
                    set_name=card_data["set"]["name"],
                    set_code=set_code,
                    card_number=card_data["number"],
                    rarity=card_data["rarity"],
                    image_url=card_data["images"]["large"] if "images" in card_data else None
                )

                # Check if card exists
                existing_card = self.db.query(Card).filter(
                    Card.set_code == set_code,
                    Card.card_number == card_data["number"]
                ).first()

                if existing_card:
                    # Update existing card
                    for key, value in card.__dict__.items():
                        if not key.startswith("_"):
                            setattr(existing_card, key, value)
                else:
                    # Add new card
                    self.db.add(card)

                # Add price history if available
                if "tcgplayer" in card_data and "prices" in card_data["tcgplayer"]:
                    prices = card_data["tcgplayer"]["prices"]
                    card_id = existing_card.id if existing_card else card.id
                    
                    price_history = PriceHistory(
                        card_id=card_id,
                        low_price=prices.get("normal", {}).get("low"),
                        mid_price=prices.get("normal", {}).get("mid"),
                        high_price=prices.get("normal", {}).get("high")
                    )
                    self.db.add(price_history)
            
            self.db.commit()
            page += 1

    def sync_all(self) -> None:
        """Sync all sets and cards."""
        self.sync_sets()
        self.sync_cards() 