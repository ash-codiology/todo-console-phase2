# Quickstart Guide: Console Todo App

**Feature**: 001-console-todo-app  
**Date**: 2026-01-02

## Prerequisites

- **Python**: 3.12 or higher
- **UV**: Python package manager ([install instructions](https://github.com/astral-sh/uv))
- **Operating System**: Windows, macOS, or Linux with terminal access

### Check Python Version

```bash
python --version
# Should output: Python 3.12.x or higher
```

### Install UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify installation
uv --version
```

## Setup Instructions

### 1. Navigate to Project Directory

```bash
cd todo-app/todo-console-app
```

### 2. Initialize UV Project (First Time Only)

```bash
# Create virtual environment
uv venv

# Install development dependencies
uv add --dev pytest
```

### 3. Verify Project Structure

Your directory should look like this:

```
todo-console-app/
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       ├── manager.py
│       └── ui.py
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_manager.py
│   └── test_ui.py
├── pyproject.toml
├── README.md
└── .venv/              # Created by uv venv
```

## Running the Application

### Option 1: Via UV (Recommended)

```bash
uv run python src/todo_app/main.py
```

### Option 2: Activate Virtual Environment

```bash
# Activate venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Run application
python src/todo_app/main.py

# Deactivate when done
deactivate
```

## Using the Application

### Main Menu

When you launch the app, you'll see:

```
================================================================================
                         📝 TODO APP - TASK MANAGER
================================================================================

Current Tasks:
No tasks found. Add your first task!

What would you like to do?

  [1] Add New Task
  [2] View All Tasks
  [3] Update Task
  [4] Mark Task Complete/Incomplete
  [5] Delete Task
  [6] Exit

Enter your choice (1-6):
```

### Example Workflow

#### 1. Add a Task

```
Enter your choice (1-6): 1

--- Add New Task ---
Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, eggs, bread

✓ Task added successfully! (ID: 1)
```

#### 2. View Tasks

Tasks auto-display after each operation:

```
================================================================================
ID    Status   Title                          Description                        
================================================================================
1     [ ]      Buy groceries                  Milk, eggs, bread                  
================================================================================
```

#### 3. Mark Task Complete

```
Enter your choice (1-6): 4

--- Toggle Task Status ---
Enter task ID: 1

✓ Task marked as complete!

================================================================================
ID    Status   Title                          Description                        
================================================================================
1     [x]      Buy groceries                  Milk, eggs, bread                  
================================================================================
```

#### 4. Update Task

```
Enter your choice (1-6): 3

--- Update Task ---
Enter task ID to update: 1
Current title: Buy groceries
Enter new title (or press Enter to keep current): Buy groceries and snacks
Current description: Milk, eggs, bread
Enter new description (or press Enter to keep current): Milk, eggs, bread, chips

✓ Task updated successfully!
```

#### 5. Delete Task

```
Enter your choice (1-6): 5

--- Delete Task ---
Enter task ID to delete: 1

✓ Task 1 deleted successfully!
```

#### 6. Exit

```
Enter your choice (1-6): 6

Thank you for using TODO APP! Goodbye! 👋
```

## Running Tests

### Run All Tests

```bash
uv run pytest
```

### Run Specific Test File

```bash
uv run pytest tests/test_manager.py
```

### Verbose Output

```bash
uv run pytest -v
```

### Example Test Output

```
========================= test session starts ==========================
collected 8 items

tests/test_manager.py ........                                   [100%]

========================== 8 passed in 0.05s ===========================
```

## Common Tasks

### Add More Dependencies

```bash
# Add runtime dependency
uv add requests

# Add development dependency
uv add --dev black
```

### Update Dependencies

```bash
uv sync
```

### Code Formatting (Optional)

```bash
# Install Black formatter
uv add --dev black

# Format all code
uv run black src/ tests/
```

### Type Checking (Optional)

```bash
# Install mypy
uv add --dev mypy

# Run type checker
uv run mypy src/todo_app/
```

## Troubleshooting

### Issue: "Python 3.12 not found"

**Solution**: Install Python 3.12+ from [python.org](https://www.python.org/downloads/) and ensure it's in your PATH.

### Issue: "uv: command not found"

**Solution**: Install UV using instructions in Prerequisites section, then restart your terminal.

### Issue: "Module 'todo_app' not found"

**Solution**: Ensure you're running from `todo-console-app/` directory and `src/todo_app/__init__.py` exists.

### Issue: "Virtual environment not activated"

**Solution**: Use `uv run` prefix (Option 1) to avoid manual activation.

## Project Development Workflow

### 1. Make Code Changes

Edit files in `src/todo_app/`

### 2. Run Application to Test

```bash
uv run python src/todo_app/main.py
```

### 3. Write/Update Tests

Add tests in `tests/`

### 4. Run Tests

```bash
uv run pytest
```

### 5. Format Code (if using Black)

```bash
uv run black src/ tests/
```

### 6. Type Check (if using mypy)

```bash
uv run mypy src/todo_app/
```

## Configuration Files

### pyproject.toml

Located at `todo-console-app/pyproject.toml`:

```toml
[project]
name = "todo-app"
version = "0.1.0"
description = "Console-based todo application for personal task management"
requires-python = ">=3.12"
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=7.4.0"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## Key Features

- ✅ **Add Tasks**: Title + description
- ✅ **View Tasks**: Formatted table with status indicators
- ✅ **Update Tasks**: Modify title or description
- ✅ **Toggle Status**: Mark complete `[x]` or incomplete `[ ]`
- ✅ **Delete Tasks**: Permanent removal by ID
- ✅ **In-Memory Storage**: Data persists during session only
- ✅ **Auto-Display**: Task table shows after every operation

## Limitations (Phase I)

- **No Persistence**: Tasks lost when app closes (Phase II will add file storage)
- **Single User**: No authentication or multi-user support
- **No Sorting/Filtering**: Tasks display in ID order only
- **English Only**: UI prompts and messages in English

## Next Steps

- **Phase II**: Add file persistence (save/load tasks from JSON)
- **Enhanced Features**: Tags, priorities, due dates
- **Advanced UI**: Colors, pagination, search

## Support

For issues or questions, refer to:
- [Specification](file:///c:/Users/Dell/Desktop/phase-1/todo-app/specs/001-console-todo-app/spec.md)
- [Implementation Plan](file:///c:/Users/Dell/Desktop/phase-1/todo-app/specs/001-console-todo-app/plan.md)
- [Data Model](file:///c:/Users/Dell/Desktop/phase-1/todo-app/specs/001-console-todo-app/data-model.md)
