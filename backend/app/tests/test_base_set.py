import os
from dotenv import load_dotenv
from app.services.pokemon_tcg_client import PokemonTCGClient

def test_find_base_set():
    """Test finding and fetching the base set cards."""
    load_dotenv()
    api_key = os.getenv('POKEMON_TCG_API_KEY')
    
    if not api_key:
        print("Error: POKEMON_TCG_API_KEY not found in environment variables")
        return False
    
    client = PokemonTCGClient(api_key)
    
    try:
        # Get all sets
        response = client.get_sets()
        if not response or 'data' not in response:
            print("❌ Failed to retrieve sets data")
            return False
        
        # Find the base set (should be named "Base" or similar)
        base_set = None
        for set_data in response['data']:
            if set_data['name'].lower() in ['base', 'base set']:
                base_set = set_data
                break
        
        if not base_set:
            print("❌ Could not find the base set")
            return False
        
        print(f"✅ Found base set: {base_set['name']} (ID: {base_set['id']})")
        
        # Get cards from the base set
        cards = client.get_cards(set_id=base_set['id'])
        if not cards or 'data' not in cards:
            print("❌ Failed to retrieve base set cards")
            return False
        
        print(f"✅ Successfully retrieved {len(cards['data'])} cards from the base set")
        print("\nAll cards in the base set:")
        for card in sorted(cards['data'], key=lambda x: int(x['number'])):
            rarity = card.get('rarity', 'N/A')
            print(f"{card['number']}/102: {card['name']} ({rarity})")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_find_base_set() 