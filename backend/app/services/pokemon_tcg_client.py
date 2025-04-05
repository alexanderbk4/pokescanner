import requests
from typing import Dict, List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class PokemonTCGClient:
    BASE_URL = "https://api.pokemontcg.io/v2"
    
    def __init__(self):
        self.api_key = os.getenv("POKEMON_TCG_API_KEY")
        self.headers = {
            "X-Api-Key": self.api_key
        } if self.api_key else {}

    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make a request to the Pokémon TCG API."""
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_cards(self, 
                 page: int = 1, 
                 page_size: int = 250,
                 query: Optional[str] = None) -> Dict:
        """Get cards with optional search query."""
        params = {
            "page": page,
            "pageSize": page_size
        }
        if query:
            params["q"] = query
        return self._make_request("cards", params)

    def get_sets(self, 
                page: int = 1, 
                page_size: int = 250) -> Dict:
        """Get all card sets."""
        params = {
            "page": page,
            "pageSize": page_size
        }
        return self._make_request("sets", params)

    def get_card_by_id(self, card_id: str) -> Dict:
        """Get a specific card by its ID."""
        return self._make_request(f"cards/{card_id}")

    def get_set_by_id(self, set_id: str) -> Dict:
        """Get a specific set by its ID."""
        return self._make_request(f"sets/{set_id}")

    def search_cards(self, 
                    name: Optional[str] = None,
                    set_code: Optional[str] = None,
                    rarity: Optional[str] = None,
                    card_type: Optional[str] = None) -> Dict:
        """Search for cards with various filters."""
        query_parts = []
        if name:
            query_parts.append(f"name:{name}")
        if set_code:
            query_parts.append(f"set.id:{set_code}")
        if rarity:
            query_parts.append(f"rarity:{rarity}")
        if card_type:
            query_parts.append(f"types:{card_type}")
        
        query = " AND ".join(query_parts) if query_parts else None
        return self.get_cards(query=query) 