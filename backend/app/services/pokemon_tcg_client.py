import requests
from typing import Dict, List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class PokemonTCGClient:
    """Client for interacting with the Pokemon TCG API."""
    
    BASE_URL = "https://api.pokemontcg.io/v2"
    
    def __init__(self, api_key: str):
        """Initialize the client with an API key."""
        self.api_key = api_key
        self.headers = {
            "X-Api-Key": api_key,
            "Content-Type": "application/json"
        }
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make a request to the Pokemon TCG API."""
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_cards(self, limit: int = 250, page: int = 1, set_id: Optional[str] = None) -> Dict:
        """Get cards from the API with optional filtering."""
        params = {
            "page": page,
            "pageSize": limit
        }
        
        if set_id:
            params["q"] = f"set.id:{set_id}"
            
        return self._make_request("cards", params)
    
    def get_sets(self, limit: int = 250, page: int = 1) -> Dict:
        """Get card sets from the API."""
        params = {
            "page": page,
            "pageSize": limit
        }
        return self._make_request("sets", params)
    
    def get_set_by_id(self, set_id: str) -> Dict:
        """Get a specific card set by its ID."""
        return self._make_request(f"sets/{set_id}")

    def get_card_by_id(self, card_id: str) -> Dict:
        """Get a specific card by its ID."""
        return self._make_request(f"cards/{card_id}")

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