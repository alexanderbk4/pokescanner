#!/bin/bash

# Exit on error
set -e

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
BACKEND_DIR="$(dirname "$SCRIPT_DIR")"

echo "🚀 Starting Pokémon Card data sync..."

# Check if virtual environment exists
if [ ! -d "$BACKEND_DIR/venv" ]; then
    echo "❌ Virtual environment not found. Creating one..."
    cd "$BACKEND_DIR"
    python -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source "$BACKEND_DIR/venv/bin/activate"

# Install requirements if not already installed
echo "📦 Checking requirements..."
pip install -r "$BACKEND_DIR/requirements.txt"

# Run the sync script
echo "🔄 Syncing card data..."
python -c "
import sys
import os
sys.path.append(os.path.dirname('$BACKEND_DIR'))
from app.database import get_db
from app.services.card_sync_service import CardSyncService

try:
    db = next(get_db())
    sync_service = CardSyncService(db)
    sync_service.sync_all()
    print('✅ Sync completed successfully!')
except Exception as e:
    print(f'❌ Error during sync: {str(e)}')
    sys.exit(1)
"

echo "✨ Card data sync complete! 🎉" 