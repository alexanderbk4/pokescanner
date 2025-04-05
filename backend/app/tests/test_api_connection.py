import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.services.pokemon_tcg_client import PokemonTCGClient

def test_api_connection():
    """Test the connection to the Pokemon TCG API."""
    load_dotenv()
    api_key = os.getenv('POKEMON_TCG_API_KEY')
    
    if not api_key:
        print("Error: POKEMON_TCG_API_KEY not found in environment variables")
        return False
    
    client = PokemonTCGClient(api_key)
    
    try:
        # Try to fetch a single card to test the connection
        response = client.get_cards(limit=1)
        if response and 'data' in response:
            print("✅ Successfully connected to Pokemon TCG API!")
            print(f"Retrieved card: {response['data'][0]['name']}")
            return True
        else:
            print("❌ Failed to retrieve card data")
            return False
    except Exception as e:
        print(f"❌ Error connecting to API: {str(e)}")
        return False

if __name__ == "__main__":
    test_api_connection() 