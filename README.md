# Pokémon Card Scanner

A web application for browsing and managing Pokémon card collections.

## Features

- Real-time card scanning using phone camera
- Augmented reality price overlay
- Card browsing interface
- Price tracking and history
- Integration with PriceCharting API

## Tech Stack

- **Frontend**: React, JavaScript, Tailwind CSS
- **Backend**: Python, FastAPI
- **Database**: MySQL

## Project Structure

```
pokemon-scanner/
├── backend/           # FastAPI backend
│   ├── app/          # Application code
│   ├── tests/        # Backend tests
│   └── requirements.txt
├── frontend/         # React frontend
│   ├── src/         # Source code
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
# Edit .env with your database credentials and desired port
```

4. Initialize the database:
```bash
python scripts/populate_db.py
```

5. Start the backend server:
```bash
uvicorn app.main:app --reload --port 8000  # or your preferred port
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
# Edit .env with your backend API URL and desired port
```

3. Start the development server:
```bash
npm start
```

## Commit History

1. Initial project setup
   - Created basic project structure
   - Set up FastAPI backend
   - Created database models for cards and sets

2. Database Implementation
   - Implemented SQLAlchemy models
   - Created database initialization script
   - Added sample data population

3. API Development
   - Created CRUD endpoints for cards and sets
   - Implemented CORS middleware
   - Added error handling

4. Frontend Setup
   - Created React application structure
   - Set up routing with React Router
   - Implemented Tailwind CSS

5. Frontend Components
   - Created SetList and CardList components
   - Implemented API integration
   - Added loading and error states

6. Configuration Updates
   - Made ports configurable via environment variables
   - Updated API URL configuration
   - Added environment variable support

## Environment Variables

### Backend (.env)
```
DATABASE_URL=mysql://user:password@localhost/pokemon_cards
API_URL=http://localhost:8000
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:8000
REACT_APP_PORT=3000
```

## Development Guidelines

- Follow the coding standards outlined in the project documentation
- Write tests for new features
- Use feature branches for development
- Keep the documentation up to date

## API Documentation

The backend API documentation is available at `/docs` when running the development server.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 