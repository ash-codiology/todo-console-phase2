from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Annotated
from src.database.connection import get_session
from src.models.user import User, UserCreate, UserRead
from src.services import auth_service
from src.utils.exceptions import ValidationException

router = APIRouter()

@router.post("/signup", response_model=UserRead)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    """
    Register a new user
    """
    try:
        db_user = auth_service.create_user(session, user)
        return db_user
    except ValidationException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during registration"
        )

@router.post("/signin")
def login_user(user_credentials: UserCreate, session: Session = Depends(get_session)):
    """
    Authenticate user and return access token
    """
    db_user = auth_service.authenticate_user(session, user_credentials.email, user_credentials.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token = auth_service.create_access_token(data={"sub": db_user.email, "user_id": db_user.id})

    return {"access_token": access_token, "token_type": "bearer", "user_id": db_user.id}