# Pokémon Card Scanner

An Android application that uses augmented reality to scan Pokémon cards and display real-time price information.

## Features

- Real-time card scanning using phone camera
- Augmented reality price overlay
- Card browsing interface
- Price tracking and history
- Integration with PriceCharting API

## Tech Stack

### Frontend
- React
- JavaScript
- Tailwind CSS
- Android Native Components

### Backend
- FastAPI (Python)
- MySQL
- Cloud Storage

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
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
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