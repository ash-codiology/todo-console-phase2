from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlmodel import Session
from src.config import settings
from src.models.user import User
from src.database.connection import get_session
from src.utils.exceptions import UnauthorizedException
import os

security = HTTPBearer()

def verify_token(token: str) -> dict:
    """Verify the JWT token and return the payload"""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise UnauthorizedException("Could not validate credentials")
        return payload
    except JWTError:
        raise UnauthorizedException("Could not validate credentials")

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session)
) -> User:
    """Get the current user from the token"""
    token_data = verify_token(credentials.credentials)
    email = token_data.get("sub")

    # We need to query by email
    from sqlmodel import select
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()

    if user is None:
        raise UnauthorizedException("User not found")

    return user