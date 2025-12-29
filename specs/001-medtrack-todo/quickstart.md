# Quickstart Guide: MedTrack Todo Agent

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional, for environment management)

## Setup

1. **Clone or create the project structure**:
   ```bash
   mkdir -p src/medtrack_todo/{models,services,utils}
   ```

2. **Create the project files** as outlined in the implementation plan:
   - `src/medtrack_todo/main.py` - CLI application entry point
   - `src/medtrack_todo/models/task.py` - Task data model
   - `src/medtrack_todo/services/task_service.py` - Task operations
   - `src/medtrack_todo/utils/validators.py` - Input validation utilities

3. **Install dependencies** (if any are added in the future):
   ```bash
   uv sync  # If using UV with pyproject.toml
   # OR
   pip install -r requirements.txt  # If using requirements.txt
   ```

## Running the Application

1. **Execute the main application**:
   ```bash
   python src/medtrack_todo/main.py
   ```

2. **Follow the on-screen menu prompts**:
   - Use numeric input (1-6) to navigate the menu
   - Follow prompts for each operation
   - Exit with option 6 to see the motivational message

## Basic Operations

### Adding a Task
1. Select option 1 from the main menu
2. Enter the task title when prompted
3. Enter the task description when prompted
4. The system will auto-generate an ID and set status to "Pending"

### Viewing Tasks
1. Select option 2 from the main menu
2. All tasks will be displayed in tabular format
3. Tasks with advanced attributes will have them stored but not displayed in Phase I

### Updating a Task
1. Select option 3 from the main menu
2. Enter the task ID when prompted
3. Enter new title and description when prompted

### Deleting a Task
1. Select option 4 from the main menu
2. Enter the task ID when prompted
3. Confirm the deletion when prompted

### Marking Task Complete/Incomplete
1. Select option 5 from the main menu
2. Enter the task ID when prompted
3. The system will toggle the status between "Pending" and "Completed"

### Exiting
1. Select option 6 from the main menu
2. The application will display a thank you message and random motivational quote

## Advanced Attributes (Future Features)

While not displayed in Phase I, the application stores the following attributes for future functionality:
- Priority (high/medium/low)
- Category (home/work/health/exercise)
- Due date (YYYY-MM-DD format)
- Reminder time (HH:MM format)
- Recurrence pattern (daily/weekly/monthly)

These will be implemented in future phases while maintaining the same underlying data structure.

## Troubleshooting

- **Invalid input**: Ensure numeric input for menu options (1-6)
- **Task not found**: Verify the task ID exists in the system
- **Empty fields**: Title and description cannot be empty when adding/updating tasks