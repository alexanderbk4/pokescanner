import os
import json
from dotenv import load_dotenv
from app.services.pokemon_tcg_client import PokemonTCGClient

def test_card_details():
    """Test to examine all available fields for a card."""
    load_dotenv()
    api_key = os.getenv('POKEMON_TCG_API_KEY')
    
    if not api_key:
        print("Error: POKEMON_TCG_API_KEY not found in environment variables")
        return False
    
    client = PokemonTCGClient(api_key)
    
    try:
        # Get base set Charizard
        response = client.get_cards(set_id='base1')
        if not response or 'data' not in response:
            print("❌ Failed to retrieve cards")
            return False
        
        # Find Charizard (card number 4)
        charizard = None
        for card in response['data']:
            if card['number'] == '4':
                charizard = card
                break
        
        if not charizard:
            print("❌ Could not find Charizard")
            return False
        
        # Print all fields
        print("\nAll fields for Base Set Charizard:")
        print(json.dumps(charizard, indent=2))
        
        # Print size estimate
        card_size = len(json.dumps(charizard).encode('utf-8'))
        print(f"\nEstimated size for this card: {card_size / 1024:.2f} KB")
        
        # Estimate total size for 102 cards
        total_size = card_size * 102
        print(f"Estimated total size for 102 cards: {total_size / 1024:.2f} KB ({total_size / 1024 / 1024:.2f} MB)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_card_details() 