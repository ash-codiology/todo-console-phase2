# Console Todo App (Phase I)

A lightweight, in-memory Python console application for managing tasks. Built with a 3-layer architecture (Presentation, Business Logic, Data Model) and strict type safety.

## Features

- **Add Task**: Capture task title and optional description.
- **View All Tasks**: Display tasks in a clean 80-char width table with status icons.
- **Update Task**: Modify title or description of existing tasks.
- **Toggle Status**: Mark tasks as complete `[x]` or incomplete `[ ]`.
- **Delete Task**: Permanently remove tasks from memory.

## Tech Stack

- **Python**: 3.12+
- **Dependency Management**: [UV](https://github.com/astral-sh/uv)
- **Testing**: Pytest
- **Type Checking**: Mypy (strict)

## Prerequisites

- [UV](https://github.com/astral-sh/uv) installed on your system.

## Getting Started

1. **Install Dependencies**:
   ```bash
   uv sync
   ```

2. **Run the Application**:
   ```bash
   uv run todo
   ```
   *Note: On Windows, use `uv run todo` to ensure the correct environment and encoding are handled.*

3. **Run Tests**:
   ```bash
   uv run pytest
   ```

4. **Run Type Checks**:
   ```bash
   uv run mypy src
   ```

## Design Architecture

- **`models.py`**: Immutable-like Task dataclass.
- **`manager.py`**: Business logic and in-memory storage (Dict).
- **`ui.py`**: Console input/output and table formatting.
- **`main.py`**: Application loop and event orchestration.

## License
MIT
