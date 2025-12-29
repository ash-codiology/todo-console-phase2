"""
TaskService for MedTrack Todo Agent.

Implements CRUD operations for Task objects with validation.
"""
from typing import List, Optional
from ..models.task import Task
from ..utils.validators import validate_task_data


class TaskService:
    """
    Service class for managing Task operations.

    Handles all CRUD operations for tasks with proper validation.
    """

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str, priority: str = "medium",
                 category: str = "health", due_date: Optional[str] = None,
                 reminder_time: Optional[str] = None,
                 recurrence_pattern: Optional[str] = None) -> Task:
        """
        Add a new task to the list with validation.

        Args:
            title: Task title
            description: Task description
            priority: Task priority (high/medium/low)
            category: Task category (home/work/health/exercise)
            due_date: Due date in YYYY-MM-DD format
            reminder_time: Reminder time in HH:MM format
            recurrence_pattern: Recurrence pattern (daily/weekly/monthly/none)

        Returns:
            Created Task object
        """
        # Validate input data
        errors = validate_task_data(
            title=title,
            description=description,
            priority=priority,
            category=category,
            due_date=due_date,
            reminder_time=reminder_time,
            recurrence_pattern=recurrence_pattern
        )

        if errors:
            raise ValueError(f"Validation errors: {'; '.join(errors)}")

        # Create new task
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            category=category,
            due_date=due_date,
            reminder_time=reminder_time,
            recurrence_pattern=recurrence_pattern
        )

        # Add to tasks list and increment ID
        self.tasks.append(task)
        self.next_id += 1

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the list.

        Returns:
            List of all Task objects
        """
        return self.tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None,
                    description: Optional[str] = None, priority: Optional[str] = None,
                    category: Optional[str] = None, due_date: Optional[str] = None,
                    reminder_time: Optional[str] = None,
                    recurrence_pattern: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task with provided values.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)
            priority: New priority (optional)
            category: New category (optional)
            due_date: New due date (optional)
            reminder_time: New reminder time (optional)
            recurrence_pattern: New recurrence pattern (optional)

        Returns:
            Updated Task object if successful, None if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        # Prepare update data
        update_data = {}
        if title is not None:
            update_data['title'] = title
        if description is not None:
            update_data['description'] = description
        if priority is not None:
            update_data['priority'] = priority
        if category is not None:
            update_data['category'] = category
        if due_date is not None:
            update_data['due_date'] = due_date
        if reminder_time is not None:
            update_data['reminder_time'] = reminder_time
        if recurrence_pattern is not None:
            update_data['recurrence_pattern'] = recurrence_pattern

        # Validate update data if any fields are being updated
        if update_data:
            errors = validate_task_data(
                title=update_data.get('title', task.title),
                description=update_data.get('description', task.description),
                priority=update_data.get('priority', task.priority),
                category=update_data.get('category', task.category),
                due_date=update_data.get('due_date', task.due_date),
                reminder_time=update_data.get('reminder_time', task.reminder_time),
                recurrence_pattern=update_data.get('recurrence_pattern', task.recurrence_pattern)
            )

            if errors:
                raise ValueError(f"Validation errors: {'; '.join(errors)}")

        # Update task fields
        for key, value in update_data.items():
            setattr(task, key, value)

        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        """
        Toggle a task's status between "Pending" and "Completed".

        Args:
            task_id: ID of the task to toggle

        Returns:
            Updated Task object if successful, None if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        # Toggle status
        if task.status == "Pending":
            task.status = "Completed"
            # Set completion time when marking as completed
            from datetime import datetime
            task.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            task.status = "Pending"
            # Clear completion time when marking as pending
            task.completed_at = None

        return task

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            Next available ID
        """
        return self.next_id