"""
Task data model for MedTrack Todo Agent.

Contains the Task class with all required attributes for Phase I
including future-proof fields for advanced features.
"""
from datetime import datetime
from typing import Optional, Dict, Any


class Task:
    """
    Represents a patient health action (medication dose or health activity).

    Attributes:
        id: Unique identifier, auto-incremented
        title: Medicine or health task name
        description: Dose, timing, notes
        status: "Pending" or "Completed"
        priority: "high", "medium", "low" - for future filtering
        category: "home", "work", "health", "exercise" - for future organization
        due_date: Optional due date in YYYY-MM-DD format - for future reminders
        reminder_time: Optional reminder time in HH:MM format - for future notifications
        recurrence_pattern: Optional recurrence pattern - for future recurring tasks
        created_at: Timestamp of task creation - for future analytics
        completed_at: Optional timestamp when task was completed - for future analytics
    """

    def __init__(
        self,
        id: int,
        title: str,
        description: str,
        status: str = "Pending",
        priority: str = "medium",
        category: str = "health",
        due_date: Optional[str] = None,
        reminder_time: Optional[str] = None,
        recurrence_pattern: Optional[str] = None,
        created_at: Optional[str] = None,
        completed_at: Optional[str] = None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.reminder_time = reminder_time
        self.recurrence_pattern = recurrence_pattern
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed_at = completed_at

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Task object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "category": self.category,
            "due_date": self.due_date,
            "reminder_time": self.reminder_time,
            "recurrence_pattern": self.recurrence_pattern,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create a Task object from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            status=data.get("status", "Pending"),
            priority=data.get("priority", "medium"),
            category=data.get("category", "health"),
            due_date=data.get("due_date"),
            reminder_time=data.get("reminder_time"),
            recurrence_pattern=data.get("recurrence_pattern"),
            created_at=data.get("created_at"),
            completed_at=data.get("completed_at")
        )

    def __repr__(self) -> str:
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}')"