"""
Validation utilities for MedTrack Todo Agent.

Contains functions for validating task data and user inputs.
"""
import re
from typing import List


def validate_task_data(title: str, description: str, priority: str = "medium",
                      category: str = "health", due_date: str = None,
                      reminder_time: str = None, recurrence_pattern: str = None) -> List[str]:
    """
    Validate task data and return a list of validation errors.

    Args:
        title: Task title to validate
        description: Task description to validate
        priority: Task priority to validate
        category: Task category to validate
        due_date: Due date to validate (optional)
        reminder_time: Reminder time to validate (optional)
        recurrence_pattern: Recurrence pattern to validate (optional)

    Returns:
        List of validation error messages (empty if no errors)
    """
    errors = []

    # Validate title
    if not title or not title.strip():
        errors.append("Title cannot be empty")
    elif len(title.strip()) > 200:
        errors.append("Title cannot exceed 200 characters")

    # Validate description
    if not description or not description.strip():
        errors.append("Description cannot be empty")
    elif len(description.strip()) > 500:
        errors.append("Description cannot exceed 500 characters")

    # Validate priority
    valid_priorities = ["high", "medium", "low"]
    if priority not in valid_priorities:
        errors.append(f"Priority must be one of: {', '.join(valid_priorities)}")

    # Validate category
    valid_categories = ["home", "work", "health", "exercise"]
    if category not in valid_categories:
        errors.append(f"Category must be one of: {', '.join(valid_categories)}")

    # Validate due_date if provided
    if due_date:
        # Check if it's in YYYY-MM-DD format
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_pattern, due_date):
            errors.append("Due date must be in YYYY-MM-DD format")

    # Validate reminder_time if provided
    if reminder_time:
        # Check if it's in HH:MM format
        time_pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
        if not re.match(time_pattern, reminder_time):
            errors.append("Reminder time must be in HH:MM format")

    # Validate recurrence_pattern if provided
    if recurrence_pattern:
        valid_patterns = ["daily", "weekly", "monthly", "none"]
        if recurrence_pattern not in valid_patterns:
            errors.append(f"Recurrence pattern must be one of: {', '.join(valid_patterns)}")

    return errors


def validate_menu_choice(choice: str, min_choice: int = 1, max_choice: int = 6) -> bool:
    """
    Validate a menu choice is a valid number within the specified range.

    Args:
        choice: User input to validate
        min_choice: Minimum valid choice (default 1)
        max_choice: Maximum valid choice (default 6)

    Returns:
        True if valid, False otherwise
    """
    try:
        choice_num = int(choice)
        return min_choice <= choice_num <= max_choice
    except ValueError:
        return False


def validate_task_id(task_id: str, max_id: int = None) -> bool:
    """
    Validate a task ID is a positive integer.

    Args:
        task_id: Task ID to validate
        max_id: Maximum valid ID (optional)

    Returns:
        True if valid, False otherwise
    """
    try:
        task_id_num = int(task_id)
        if task_id_num <= 0:
            return False
        if max_id and task_id_num > max_id:
            return False
        return True
    except ValueError:
        return False