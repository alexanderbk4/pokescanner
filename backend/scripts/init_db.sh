#!/bin/bash

# Exit on error
set -e

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
BACKEND_DIR="$(dirname "$SCRIPT_DIR")"

echo "🚀 Initializing Pokémon Card Scanner database..."

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

# Run the database initialization script
echo "🗄️ Creating database tables..."
python -c "
import sys
import os
sys.path.append(os.path.dirname('$BACKEND_DIR'))
from app.database.init_db import init_db

try:
    init_db()
    print('✅ Database initialization completed successfully!')
except Exception as e:
    print(f'❌ Error during database initialization: {str(e)}')
    sys.exit(1)
"

echo "✨ Database initialization complete! 🎉" 