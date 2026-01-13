from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, todos
from src.config import settings

app = FastAPI(title="Todo API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://todo-console-frontend.vercel.app",
        "https://todo-console-frontend-flv70szde-ashfa-shakeels-projects.vercel.app",
        "http://localhost:3000",  # For local development
        "http://localhost:3001",  # Alternative local dev port
        "http://localhost:3002",  # Another alternative
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/todos", tags=["todos"])

@app.get("/")
def read_root():
    return {"message": "Todo API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}