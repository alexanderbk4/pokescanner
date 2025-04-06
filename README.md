# Pokémon Card Scanner

A comprehensive web application for browsing, tracking, and managing Pokémon Trading Card Game (TCG) collections. The application provides a rich interface for viewing card details, tracking prices, and managing collections.

## Features

- **Card Browsing Interface**
  - Browse cards from all Pokémon TCG sets
  - Filter and search cards by set, rarity, and name
  - View high-resolution card images
  - Detailed card information including set details and rarity

- **Price Tracking**
  - Historical price data for cards
  - Price trends and market analysis
  - Integration with Pokémon TCG API for real-time data

- **Collection Management**
  - Track your personal card collection
  - Organize cards by set and condition
  - Calculate collection value

## Tech Stack

- **Frontend**: React, JavaScript, Tailwind CSS
- **Backend**: Python, FastAPI
- **Database**: MySQL
- **APIs**: Pokémon TCG API

## Project Structure

```
pokemon-scanner/
├── backend/           # FastAPI backend
│   ├── app/          # Application code
│   │   ├── models/   # Database models
│   │   ├── services/ # Business logic
│   │   └── schemas/  # Pydantic models
│   ├── scripts/      # Utility scripts
│   ├── tests/        # Backend tests
│   └── requirements.txt
├── frontend/         # React frontend
│   ├── src/         # Source code
│   │   ├── components/ # React components
│   │   ├── pages/     # Page components
│   │   └── services/  # API services
│   ├── public/      # Static files
│   └── package.json
└── README.md
```

## Setup Instructions

### Backend Setup

1. Create and activate a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials and Pokémon TCG API key
```

4. Initialize the database:
```bash
# Sync all card sets and their cards
python scripts/sync_all_sets.py
```

5. Start the backend server:
```bash
uvicorn app.main:app --reload --port 8003
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your backend API URL
```

3. Start the development server:
```bash
npm start
```

## Current Status

The application currently provides:
- Complete card database with all Pokémon TCG sets
- Card browsing interface with filtering capabilities
- High-resolution card images
- Set-based organization

Planned features not yet implemented:
- Price tracking and historical data
- Collection management
- User authentication

## Future Goals

1. **Enhanced Collection Management**
   - User authentication and personal collections
   - Card condition tracking
   - Collection value calculation

2. **Advanced Price Tracking**
   - Real-time price updates
   - Price history visualization
   - Market trend analysis

3. **Mobile Integration**
   - Mobile-friendly interface
   - Card scanning capabilities
   - Augmented reality features

4. **Social Features**
   - Collection sharing
   - Trading platform
   - Community marketplace

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 