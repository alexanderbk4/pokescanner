# Pokémon Card Scanner

A web and mobile application that allows users to scan Pokémon Trading Card Game (TCG) cards using their phone's camera to instantly view current market prices. The application currently provides a comprehensive card browsing interface, with the ultimate goal of becoming a real-time card scanning and pricing tool.

## Current Features

- **Card Database & Browsing**
  - Complete database of all Pokémon TCG sets
  - Browse and filter cards by set, rarity, and name
  - View high-resolution card images
  - Detailed card information including set details and rarity

## Primary Goal

The main objective of this project is to create a real-time card scanning application that:
- Uses phone camera to instantly identify Pokémon cards
- Overlays current market prices directly on the card image
- Provides price ranges based on card condition (Near Mint, Lightly Played, etc.)
- Updates prices in real-time from market data
- Works offline for previously scanned cards

## Future Features

1. **Real-time Card Scanning**
   - Camera-based card recognition
   - Augmented reality price overlay
   - Offline card database for quick identification
   - Multiple card scanning in one frame

2. **Advanced Price Tracking**
   - Real-time price updates from multiple sources
   - Price history visualization
   - Condition-based pricing
   - Market trend analysis

3. **Collection Management**
   - User authentication and personal collections
   - Card condition tracking
   - Collection value calculation
   - Export/import collection data

4. **Social Features**
   - Collection sharing
   - Trading platform
   - Community marketplace
   - Price alert notifications

## Tech Stack

- **Frontend**: React, JavaScript, Tailwind CSS
- **Backend**: Python, FastAPI
- **Database**: MySQL
- **APIs**: Pokémon TCG API
- **Mobile**: React Native (planned)
- **Computer Vision**: TensorFlow, OpenCV (planned)

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

## Development Roadmap

1. **Phase 1: Card Database & Browsing** (Current)
   - Complete card database implementation ✓
   - Basic browsing interface ✓
   - Set-based organization ✓

2. **Phase 2: Price Integration**
   - Price data collection system
   - Real-time price updates
   - Condition-based pricing

3. **Phase 3: Mobile Development**
   - React Native app development
   - Camera integration
   - Offline card database

4. **Phase 4: Computer Vision**
   - Card recognition model training
   - Real-time scanning implementation
   - AR price overlay

5. **Phase 5: Advanced Features**
   - Collection management
   - Social features
   - Market analysis tools

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 