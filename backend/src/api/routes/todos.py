from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from src.database.connection import get_session
from src.middleware.auth import get_current_user
from src.models.todo import Todo, TodoCreate, TodoRead, TodoUpdate
from src.models.user import User
from src.services import todo_service
from src.utils.exceptions import NotFoundException

router = APIRouter()

@router.get("/", response_model=List[TodoRead])
def read_todos(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve user's todos
    """
    todos = todo_service.get_todos_by_user(session, current_user.id)
    return todos

@router.post("/", response_model=TodoRead)
def create_todo(
    todo: TodoCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new todo
    """
    db_todo = todo_service.create_todo(session, todo, current_user.id)
    return db_todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(
    todo_id: str,
    todo_update: TodoUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a todo
    """
    # Verify user owns the todo before updating
    if not todo_service.check_todo_ownership(session, todo_id, current_user.id):
        raise NotFoundException(detail="Todo not found")

    db_todo = todo_service.update_todo(session, todo_id, todo_update, current_user.id)
    return db_todo

@router.delete("/{todo_id}")
def delete_todo(
    todo_id: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a todo
    """
    # Verify user owns the todo before deleting
    if not todo_service.check_todo_ownership(session, todo_id, current_user.id):
        raise NotFoundException(detail="Todo not found")

    todo_service.delete_todo(session, todo_id, current_user.id)
    return {"message": "Todo deleted successfully"}

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(
    todo_id: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve a specific todo by ID
    """
    db_todo = todo_service.get_todo_by_id(session, todo_id, current_user.id)
    if not db_todo:
        raise NotFoundException(detail="Todo not found")
    return db_todo


@router.patch("/{todo_id}/toggle", response_model=TodoRead)
def toggle_todo_completion(
    todo_id: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Toggle a todo's completion status
    """
    # Verify user owns the todo before toggling
    if not todo_service.check_todo_ownership(session, todo_id, current_user.id):
        raise NotFoundException(detail="Todo not found")

    db_todo = todo_service.toggle_todo_completion(session, todo_id, current_user.id)
    return db_todo