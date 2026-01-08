from typing import Dict, List, Optional
from datetime import datetime
from .models import Task

class TaskManager:
    """
    Handles in-memory storage and business logic for tasks.
    
    Attributes:
        _tasks: Dictionary mapping task IDs to Task objects.
        _next_id: Counter for auto-incrementing task IDs.
    """
    
    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1
        
    def _generate_id(self) -> int:
        """
        Generate a unique auto-incrementing ID.
        
        Returns:
            The next available integer ID.
        """
        new_id = self._next_id
        self._next_id += 1
        return new_id

    def _validate_title(self, title: str) -> bool:
        """Validate task title is non-empty."""
        return bool(title and title.strip())

    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task and return its ID.
        
        Args:
            title: The task title (must be non-empty).
            description: Optional task description.
            
        Returns:
            The ID of the newly created task.
            
        Raises:
            ValueError: If the title is empty.
        """
        if not self._validate_title(title):
            raise ValueError("Title cannot be empty")
            
        task_id = self._generate_id()
        task = Task(
            id=task_id,
            title=title.strip(),
            description=description.strip(),
            status=False,
            created_at=datetime.now()
        )
        self._tasks[task_id] = task
        return task_id

    def get_task(self, task_id: int) -> Optional[Task]:

        """
        Retrieve a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve.
            
        Returns:
            The Task object if found, None otherwise.
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Return all tasks in creation order (by ID).
        
        Returns:
            A list of all Task objects.
        """
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title and/or description.
        
        Args:
            task_id: The ID of the task to update.
            title: New title (if provided).
            description: New description (if provided).
            
        Returns:
            True if updated successfully, False if task_id not found.
            
        Raises:
            ValueError: If the new title is empty.
        """
        task = self.get_task(task_id)
        if not task:
            return False
            
        if title is not None:
            if not self._validate_title(title):
                raise ValueError("Title cannot be empty")
            task.title = title.strip()
            
        if description is not None:
            task.description = description.strip()
            
        return True

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle the status of a task between complete and incomplete.
        
        Args:
            task_id: The ID of the task to toggle.
            
        Returns:
            True if toggled successfully, False if task_id not found.
        """
        task = self.get_task(task_id)
        if not task:
            return False
            
        task.status = not task.status
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Permanently remove a task.
        
        Args:
            task_id: The ID of the task to delete.
            
        Returns:
            True if deleted successfully, False if task_id not found.
        """
        if task_id not in self._tasks:
            return False
            
        del self._tasks[task_id]
        return True


