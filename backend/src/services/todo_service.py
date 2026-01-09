from sqlmodel import Session, select
from typing import List, Optional
from src.models.todo import Todo, TodoCreate, TodoUpdate
from src.models.user import User
from src.utils.exceptions import NotFoundException, ForbiddenException

def get_todos_by_user(session: Session, user_id: str) -> List[Todo]:
    """Get all todos for a specific user"""
    statement = select(Todo).where(Todo.user_id == user_id)
    return session.exec(statement).all()

def get_todo_by_id(session: Session, todo_id: str, user_id: str) -> Optional[Todo]:
    """Get a specific todo by ID for a specific user"""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    return session.exec(statement).first()

def check_todo_ownership(session: Session, todo_id: str, user_id: str) -> bool:
    """Check if a user owns a specific todo"""
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    todo = session.exec(statement).first()
    return todo is not None

def create_todo(session: Session, todo_create: TodoCreate, user_id: str) -> Todo:
    """Create a new todo for a user"""
    db_todo = Todo(
        title=todo_create.title,
        description=todo_create.description,
        completed=todo_create.completed,
        user_id=user_id
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def update_todo(session: Session, todo_id: str, todo_update: TodoUpdate, user_id: str) -> Todo:
    """Update a specific todo for a user"""
    db_todo = get_todo_by_id(session, todo_id, user_id)

    if not db_todo:
        raise NotFoundException(detail="Todo not found")

    # Update the todo with provided fields
    for field, value in todo_update.dict(exclude_unset=True).items():
        setattr(db_todo, field, value)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def delete_todo(session: Session, todo_id: str, user_id: str) -> bool:
    """Delete a specific todo for a user"""
    db_todo = get_todo_by_id(session, todo_id, user_id)

    if not db_todo:
        raise NotFoundException(detail="Todo not found")

    session.delete(db_todo)
    session.commit()
    return True

def toggle_todo_completion(session: Session, todo_id: str, user_id: str) -> Todo:
    """Toggle the completion status of a todo"""
    db_todo = get_todo_by_id(session, todo_id, user_id)

    if not db_todo:
        raise NotFoundException(detail="Todo not found")

    db_todo.completed = not db_todo.completed
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo