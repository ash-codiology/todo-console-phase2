# Research: Console Todo App

**Feature**: 001-console-todo-app  
**Date**: 2026-01-02  
**Phase**: 0 (Technology Research & Validation)

## Overview

This document consolidates research findings for implementing a Python 3.12+ console todo application using UV, dataclasses, and in-memory storage with clean architecture principles.

---

## 1. Python 3.12+ Dataclasses Best Practices

### Decision
Use `@dataclass` decorator from standard library for Task model with mutable configuration.

### Rationale
- **Type Safety**: Dataclasses auto-generate `__init__` with type-checked parameters
- **Immutability Trade-off**: Need mutable dataclass to support status updates (toggle complete/incomplete)
- **Pythonic**: More concise than manual `__init__`, `__repr__`, `__eq__` methods
- **IDE Support**: Better autocomplete and refactoring with explicit field types

### Implementation Pattern

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    """Represents a todo task."""
    id: int
    title: str
    description: str
    status: bool  # True = complete, False = incomplete
    created_at: datetime
```

**Mutable vs Frozen**:
- ✅ Use mutable (default): Allows `task.status = True` for toggle operations
- ❌ Avoid `frozen=True`: Would require creating new Task instances for every status change (inefficient, complicates in-memory storage)

### Type Hints in Dataclass Fields
- All fields automatically typed via annotations
- Optional fields: Use `Optional[str]` or `str = ""` for defaults
- For this app: `description` defaults to `""` (empty string) when not provided

### Alternatives Considered
- **NamedTuple**: Rejected - immutable, awkward for status updates
- **Manual class**: Rejected - verbose, no advantage over dataclass
- **Plain dict**: Rejected - violates type safety principle, no IDE support

---

## 2. UV Project Initialization Workflow

### Decision
Use UV for all dependency and environment management with Python 3.12+ requirement in pyproject.toml.

### Commands

```bash
# Initialize new Python project
cd todo-console-app
uv init --python 3.12

# Create virtual environment
uv venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Unix/macOS:
source .venv/bin/activate

# Add development dependency
uv add --dev pytest

# Run application
uv run python src/todo_app/main.py

# Run tests
uv run pytest
```

### pyproject.toml Structure

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

### Rationale
- **Fast**: UV resolves dependencies faster than pip
- **Reproducible**: Lockfile ensures consistent environments
- **Simple**: `uv run` eliminates manual venv activation confusion
- **Constitution Compliant**: Principle VI mandates UV-only usage

### Alternatives Considered
- **pip + venv**: Rejected - slower, constitution requires UV
- **Poetry**: Rejected - additional tool, UV sufficient for simple project
- **Conda**: Rejected - heavyweight, constitution specifies UV

---

## 3. In-Memory Storage Patterns

### Decision
Use `Dict[int, Task]` with auto-incrementing integer ID generator.

### Implementation Pattern

```python
from typing import Dict, Optional
from models import Task

class TaskManager:
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1
    
    def _generate_id(self) -> int:
        """Generate next available task ID."""
        current_id = self._next_id
        self._next_id += 1
        return current_id
```

### Rationale
- **O(1) Lookup**: Dict provides constant-time access by ID for update/delete/toggle
- **Simple IDs**: Auto-increment integers (1, 2, 3...) are user-friendly in console displays
- **No External Dependencies**: No UUID library needed (simpler, faster)
- **ID Persistence**: `_next_id` counter never decrements, IDs never reused after deletion (spec requirement)

### Storage Structure Trade-offs

| Approach | Lookup Speed | Add Speed | Memory | List All Speed |
|----------|--------------|-----------|--------|----------------|
| `Dict[int, Task]` ✅ | O(1) | O(1) | Moderate | O(n) |
| `List[Task]` | O(n) | O(1) | Low | O(n) |

- Dict wins: Update/Delete/Toggle operations require ID lookups (primary use case)
- List disadvantage: Finding task by ID requires linear search through all tasks

### ID Generation Strategy
- Simple counter starting at 1
- Increment after each task creation
- Never reuse IDs (even after deletion) - spec edge case requirement
- No gaps tolerated (1, 2, 3, 4... sequence maintained for new tasks)

### Alternatives Considered
- **List[Task]**: Rejected - O(n) ID lookups inefficient
- **UUID**: Rejected - overkill for in-memory app, ugly in console display
- **Hash-based IDs**: Rejected - unnecessary complexity

---

## 4. Pytest Setup for Console Applications

### Decision
Create basic pytest structure with simple assertion-based tests. Defer input mocking to Phase II.

### Directory Structure

```text
tests/
├── __init__.py
├── test_models.py        # Task dataclass validation
├── test_manager.py       # TaskManager CRUD operations
└── test_ui.py            # ConsoleUI formatting (optional Phase I)
```

### Example Test Pattern

```python
# tests/test_manager.py
from datetime import datetime
from todo_app.manager import TaskManager

def test_add_task():
    manager = TaskManager()
    task_id = manager.add_task("Buy milk", "From store")
    
    assert task_id == 1
    task = manager.get_task(task_id)
    assert task.title == "Buy milk"
    assert task.description == "From store"
    assert task.status is False

def test_toggle_task_status():
    manager = TaskManager()
    task_id = manager.add_task("Test task", "")
    
    manager.toggle_task_status(task_id)
    task = manager.get_task(task_id)
    assert task.status is True
    
    manager.toggle_task_status(task_id)
    task = manager.get_task(task_id)
    assert task.status is False
```

### Running Tests

```bash
# Option 1: Via UV (recommended)
uv run pytest

# Option 2: After venv activation
pytest

# Verbose output
uv run pytest -v

# Specific test file
uv run pytest tests/test_manager.py
```

### Rationale
- **Simple Start**: Basic assertion tests verify core logic without mocking complexity
- **Future-Ready**: Structure supports Phase II TDD with fixtures and input mocking
- **Fast Feedback**: Unit tests run in <1s for 50+ tests
- **Constitution Compliant**: Principle IV requires tests, even if not TDD-first in Phase I

### Input Mocking (Deferred to Phase II)
- ConsoleUI uses `input()` - requires `unittest.mock.patch` or `pytest-mock`
- Phase I: Manual testing via console interaction (spec acceptance criteria)
- Phase II: Automated UI tests with mocked stdin

### Alternatives Considered
- **No tests**: Rejected - constitution requires test structure
- **Full TDD upfront**: Deferred - spec prioritizes functional delivery, tests supportive
- **Integration tests only**: Rejected - unit tests catch logic bugs faster

---

## 5. Console Table Formatting Options

### Decision
Manual formatting with Python string methods and basic alignment for clean, readable tables.

### Implementation Pattern

```python
def display_tasks_table(self, tasks: List[Task]) -> None:
    """Display tasks in formatted table."""
    if not tasks:
        print("\nNo tasks found. Add your first task!")
        return
    
    # Header
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Status':<8} {'Title':<30} {'Description':<35}")
    print("="*80)
    
    # Rows
    for task in tasks:
        status_icon = "[x]" if task.status else "[ ]"
        title = task.title[:28] + ".." if len(task.title) > 30 else task.title
        desc = task.description[:33] + ".." if len(task.description) > 35 else task.description
        
        print(f"{task.id:<5} {status_icon:<8} {title:<30} {desc:<35}")
    
    print("="*80 + "\n")
```

### Column Widths
- **ID**: 5 chars (supports up to 99999 tasks)
- **Status**: 8 chars (`[ ]` or `[x]` with padding)
- **Title**: 30 chars (truncate with ".." if longer)
- **Description**: 35 chars (truncate with ".." if longer)
- **Total Line Width**: 80 chars (fits standard 80-char terminal)

### Rationale
- **Standard Library Only**: No external dependencies (tabulate, rich) required
- **Simple**: String formatting with f-strings and `.ljust()` / `<` alignment
- **Readable**: Clear visual separation with "=" borders, aligned columns
- **Truncation**: Prevents ultra-wide tables from wrapping (keeps table compact)
- **Constitution Compliant**: Principle V mandates stdlib-only, avoid over-engineering

### Status Indicators
- Incomplete: `[ ]` (spec requirement FR-007)
- Complete: `[x]` (spec requirement FR-007)

### Alternatives Considered
- **`tabulate` library**: Rejected - violates stdlib-only constraint
- **`rich` library**: Rejected - overkill, adds dependency
- **CSV format**: Rejected - not human-friendly for console
- **Full descriptions (no truncation)**: Rejected - causes wide tables, poor UX

---

## Technology Stack Summary

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Language | Python 3.12+ | Modern features, type hints, dataclasses |
| Package Manager | UV | Fast, reproducible, constitution-mandated |
| Data Model | `@dataclass` | Type-safe, concise, built-in |
| Storage | `Dict[int, Task]` | O(1) lookups, simple auto-increment IDs |
| Testing | pytest | Industry standard, simple setup |
| Table Formatting | String f-formatting | Stdlib-only, sufficient for needs |
| Type Checking | mypy (recommended) | Enforce type safety (Principle III) |
| Code Style | Black (optional) | Auto-format to PEP 8, 88-char lines |

**All Runtime Dependencies**: None (stdlib-only)  
**Development Dependencies**: pytest, mypy (optional), black (optional)

---

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Large task titles overflow table | Medium | Truncate at 30 chars with ".." indicator |
| Many tasks (>100) slow table rendering | Low | Python string ops fast enough for 1000s of tasks |
| User unfamiliar with UV | Medium | Quickstart provides exact commands, fallback to venv activation |
| Type hint violations missed | Medium | Recommend mypy in README, add to quality gates |

---

## Next Steps

Proceed to **Phase 1: Design & Contracts**:
1. Create data-model.md (Task entity definition)
2. Create contracts/cli-interface.md (Menu structure, command flow)
3. Create quickstart.md (Setup, run, usage)
4. Update agent context files
