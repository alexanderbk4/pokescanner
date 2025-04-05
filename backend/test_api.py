import os
from dotenv import load_dotenv
import requests

def test_api_connection():
    """Test the connection to the Pokemon TCG API."""
    load_dotenv()
    api_key = os.getenv('POKEMON_TCG_API_KEY')
    
    if not api_key:
        print("Error: POKEMON_TCG_API_KEY not found in environment variables")
        return False
    
    headers = {
        "X-Api-Key": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        # Try to fetch a single card to test the connection
        response = requests.get(
            "https://api.pokemontcg.io/v2/cards",
            headers=headers,
            params={"page": 1, "pageSize": 1}
        )
        response.raise_for_status()
        data = response.json()
        
        if data and 'data' in data:
            print("✅ Successfully connected to Pokemon TCG API!")
            print(f"Retrieved card: {data['data'][0]['name']}")
            return True
        else:
            print("❌ Failed to retrieve card data")
            return False
    except Exception as e:
        print(f"❌ Error connecting to API: {str(e)}")
        return False

if __name__ == "__main__":
    test_api_connection() 