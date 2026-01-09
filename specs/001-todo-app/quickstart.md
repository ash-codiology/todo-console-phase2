# Quickstart Guide: Todo App Full-Stack Implementation

**Feature**: Todo App Full-Stack Implementation
**Date**: 2026-01-08
**Branch**: 001-todo-app

## Prerequisites

- Python 3.11+
- Node.js 18+ and npm/yarn
- PostgreSQL (local or Neon Serverless instance)
- Git

## Setup Instructions

### 1. Clone and Initialize Repository

```bash
git clone <repository-url>
cd <repository-root>
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn sqlmodel python-multipart psycopg2-binary python-dotenv better-exceptions

# Set up environment variables
cp .env.example .env
# Edit .env with your database connection details
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
# or
yarn install

# Set up environment variables
cp .env.example .env.local
# Edit .env.local with your backend API URL
```

### 4. Database Configuration

1. Set up Neon Serverless PostgreSQL instance
2. Update database connection string in backend `.env`
3. Run initial migrations (when available)

### 5. Running the Applications

#### Backend
```bash
cd backend
uvicorn src.api.main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
npm run dev
# or
yarn dev
```

## Key Endpoints

### Backend API
- Base URL: `http://localhost:8000/api`
- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

### Frontend
- Development: `http://localhost:3000`
- Production build: `npm run build && npm start`

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql+psycopg2://username:password@host:port/database
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## Development Commands

### Backend
```bash
# Run tests
pytest

# Format code
black src/

# Check types
mypy src/
```

### Frontend
```bash
# Run tests
npm test
# or
yarn test

# Build for production
npm run build
# or
yarn build
```