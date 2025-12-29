"""
Constants for MedTrack Todo Agent.

Contains application-wide constants and configuration values.
"""


# Application constants
APP_NAME = "MedTrack Todo"
APP_VERSION = "1.0.0"
HEALTH_MESSAGE = "Your health matters 🌱"

# Valid values for task attributes
VALID_PRIORITIES = ["high", "medium", "low"]
VALID_CATEGORIES = ["home", "work", "health", "exercise"]
VALID_STATUSES = ["Pending", "Completed"]
VALID_RECURRENCE_PATTERNS = ["daily", "weekly", "monthly", "none"]

# Default values
DEFAULT_PRIORITY = "medium"
DEFAULT_CATEGORY = "health"
DEFAULT_STATUS = "Pending"

# Validation limits
MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 500

# Menu options
MENU_OPTIONS = {
    1: "Add Task",
    2: "View Task List",
    3: "Update Task",
    4: "Delete Task",
    5: "Mark Task Complete / Incomplete",
    6: "Exit"
}

# Motivational quotes
MOTIVATIONAL_QUOTES = [
    "Taking your medicine on time is an act of self-care.",
    "Small health steps today prevent big problems tomorrow.",
    "Consistency is the key to recovery.",
    "Every dose counts — stay committed to your health.",
    "Your dedication today ensures a healthier tomorrow."
]

# Error messages
ERROR_MESSAGES = {
    "invalid_menu_option": "Invalid option. Please select a number from 1 to 6.",
    "task_id_not_found": "Task ID not found. Please try again.",
    "empty_title_description": "Title/Description cannot be empty.",
    "invalid_date_format": "Date must be in YYYY-MM-DD format.",
    "invalid_time_format": "Time must be in HH:MM format."
}