#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Pokémon Card Scanner setup..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "📦 Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# Install system dependencies
echo "📦 Installing system dependencies..."
brew install mysql rust node python@3.11

# Start MySQL service
echo "🔌 Starting MySQL service..."
brew services start mysql

# Wait for MySQL to start
echo "⏳ Waiting for MySQL to start..."
sleep 5

# Create database
echo "🗄️ Creating database..."
mysql -u root -e "CREATE DATABASE IF NOT EXISTS pokemon_cards;"

# Set up backend
echo "🔧 Setting up backend..."
cd backend
python3.11 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt

# Set up frontend
echo "🔧 Setting up frontend..."
cd ../frontend
npm install

echo "✨ Setup complete! 🎉"
echo "To start the backend server:"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  uvicorn app.main:app --reload"
echo ""
echo "To start the frontend development server:"
echo "  cd frontend"
echo "  npm start" 