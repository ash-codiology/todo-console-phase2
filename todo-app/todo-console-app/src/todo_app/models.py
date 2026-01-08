from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    """
    Represents a todo task.
    
    Attributes:
        id: Unique integer identifier (auto-assigned)
        title: Short description of the task (required, non-empty)
        description: Detailed information (optional, can be empty)
        status: Completion state (False=incomplete, True=complete)
        created_at: Timestamp of task creation
    """
    id: int
    title: str
    description: str
    status: bool
    created_at: datetime
