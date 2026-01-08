# Implementation Plan: Console Todo App

**Branch**: `001-console-todo-app` | **Date**: 2026-01-02 | **Spec**: [spec.md](file:///c:/Users/Dell/Desktop/phase-1/todo-app/specs/001-console-todo-app/spec.md)  
**Input**: Feature specification from `specs/001-console-todo-app/spec.md`

## Summary

Build an in-memory Python console application for personal task management supporting 5 core operations: Add, List, Update, Toggle Status, and Delete tasks. Implementation uses Python 3.12+, UV for dependency management, and a clean MVC-like architecture with strict layer separation. Data persists only during application session with auto-incrementing task IDs and dataclass models.

## Technical Context

**Language/Version**: Python 3.12+  
**Primary Dependencies**: Standard library only (no external runtime dependencies), pytest for testing framework  
**Storage**: In-memory (List/Dict structures) - no file or database persistence in Phase I  
**Testing**: pytest with test structure prepared for future TDD  
**Target Platform**: Cross-platform CLI (Windows, macOS, Linux via standard terminal)  
**Project Type**: Single console application  
**Performance Goals**: <3s startup, instant operations (<100ms) for 50+ tasks, table rendering <200ms  
**Constraints**: Standard library only (except dev dependencies), 88-char line length, PEP 8 compliance  
**Scale/Scope**: Personal use, single user, 50-100 tasks typical workload, no concurrency requirements

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Phase 0 Check

- ✅ **I. Clean Code & PEP 8**: Plan specifies PEP 8 compliance, 88-char lines, meaningful names
- ✅ **II. Modularity & Separation of Concerns**: 3-layer architecture (ConsoleUI → TaskManager → Task model) with clear boundaries
- ✅ **III. Type Safety**: Dataclasses for Task model, type hints required for all functions/methods
- ✅ **IV. Documentation Standards**: Google-style docstrings required, README with setup instructions
- ✅ **V. Simplicity & Standard Libraries**: Standard library only, no external runtime dependencies, simple auto-increment IDs
- ✅ **VI. UV-Based Dependency Management**: UV for project setup, virtual env, dependency management

**Pre-Research Status**: ✅ PASS (no violations)

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── cli-interface.md # Console interface specification
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
todo-console-app/
├── src/
│   └── todo_app/
│       ├── __init__.py       # Package initialization
│       ├── main.py           # Entry point, main loop, dependency wiring
│       ├── models.py         # Task dataclass definition
│       ├── manager.py        # TaskManager (business logic + in-memory storage)
│       └── ui.py             # ConsoleUI (presentation layer, input/output)
├── tests/
│   ├── __init__.py
│   ├── test_models.py        # Task model validation tests
│   ├── test_manager.py       # TaskManager CRUD tests
│   └── test_ui.py            # ConsoleUI formatting tests (optional)
├── pyproject.toml            # UV project configuration, dependencies
├── README.md                 # Setup instructions, usage guide
└── .gitignore                # Python/UV ignores
```

**Structure Decision**: Single project structure selected. Console application doesn't require backend/frontend separation. All code resides in `todo-console-app/src/todo_app/` with pytest tests in `todo-console-app/tests/`. UV manages project via `pyproject.toml` at `todo-console-app/` root.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations to justify. Architecture adheres to all constitutional principles.

## Phase 0: Research & Technology Validation

### Research Tasks

1. **Python 3.12+ dataclasses best practices**
   - Confirm `@dataclass` decorator for Task model
   - frozen vs mutable dataclasses (choose mutable for status updates)
   - Type hints within dataclass fields

2. **UV project initialization workflow**
   - Commands: `uv init`, `uv venv`, `uv add --dev pytest`
   - pyproject.toml structure for Python 3.12+ requirement
   - Virtual environment activation on Windows/Unix

3. **In-memory storage patterns**
   - Dict[int, Task] vs List[Task] trade-offs (choose Dict for O(1) lookup by ID)
   - Auto-increment ID generation strategy
   - Task ID persistence across delete operations

4. **pytest setup for console applications**
   - Test structure without fixtures (Phase I: basic asserts)
   - Mocking user input for ConsoleUI tests (defer to Phase II)
   - Running tests: `uv run pytest` or activate venv then `pytest`

5. **Console table formatting options**
   - Standard library only: manual formatting vs basic string alignment
   - Column width calculation for dynamic content
   - Status indicator rendering ([ ] vs [x])

See [research.md](file:///c:/Users/Dell/Desktop/phase-1/todo-app/specs/001-console-todo-app/research.md) for detailed findings.

## Phase 1: Design & Detailed Specification

### Architecture Layers

```
┌─────────────────────────────────────┐
│         main.py (Entry Point)       │
│   - Initializes TaskManager         │
│   - Initializes ConsoleUI           │
│   - Runs main menu loop             │
└────────────┬────────────────────────┘
             │
             ├─────────────────────────────────┐
             │                                 │
┌────────────▼──────────────┐   ┌──────────────▼─────────────┐
│   ui.py (ConsoleUI)       │   │  manager.py (TaskManager)  │
│   Presentation Layer      │   │  Business Logic Layer      │
│                           │   │                            │
│   - display_menu()        │   │  - add_task()              │
│   - get_user_input()      │   │  - get_task()              │
│   - display_tasks_table() │   │  - get_all_tasks()         │
│   - display_error()       │   │  - update_task()           │
│   - display_success()     │   │  - delete_task()           │
│                           │   │  - toggle_task_status()    │
│   NO business logic       │   │  - _generate_id()          │
│   NO direct model access  │   │                            │
└───────────────────────────┘   │  NO UI code                │
                                │  Uses models.Task          │
                                └────────────┬───────────────┘
                                             │
                                ┌────────────▼───────────────┐
                                │  models.py (Task)          │
                                │  Data Layer                │
                                │                            │
                                │  @dataclass Task:          │
                                │    - id: int               │
                                │    - title: str            │
                                │    - description: str      │
                                │    - status: bool          │
                                │    - created_at: datetime  │
                                │                            │
                                │  UI-agnostic               │
                                │  Framework-independent     │
                                └────────────────────────────┘
```

### Data Model

See [data-model.md](file:///c:/Users/Dell/Desktop/phase-1/todo-app/specs/001-console-todo-app/data-model.md) for complete entity definitions, validation rules, and state transitions.

### Interface Contracts

See [contracts/cli-interface.md](file:///c:/Users/Dell/Desktop/phase-1/todo-app/specs/001-console-todo-app/contracts/cli-interface.md) for menu structure, command flow, input/output specifications, and error handling.

### Quickstart Guide

See [quickstart.md](file:///c:/Users/Dell/Desktop/phase-1/todo-app/specs/001-console-todo-app/quickstart.md) for setup instructions, running the app, and example usage.

## Post-Phase 1 Constitution Check

- ✅ **I. Clean Code & PEP 8**: Architecture diagram shows focused, single-responsibility modules. Function names descriptive.
- ✅ **II. Modularity & Separation of Concerns**: Three layers strictly separated - ConsoleUI → TaskManager → Task. No cross-layer violations.
- ✅ **III. Type Safety**: Task dataclass enforces types. All methods will use type hints (enforced in tasks).
- ✅ **IV. Documentation Standards**: Module docstrings, class docstrings, README with examples planned.
- ✅ **V. Simplicity & Standard Libraries**: Dict storage, auto-increment IDs, manual table formatting - all stdlib.
- ✅ **VI. UV-Based Dependency Management**: pyproject.toml defines project, UV commands in quickstart.

**Post-Design Status**: ✅ PASS (all principles maintained)

## Implementation Phases (for /sp.tasks)

When generating tasks with `/sp.tasks`, follow this order:

1. **Setup Phase**: UV project initialization, directory structure, pyproject.toml
2. **Data Layer**: models.py with Task dataclass
3. **Business Logic Layer**: manager.py with TaskManager class
4. **Presentation Layer**: ui.py with ConsoleUI class
5. **Integration**: main.py entry point and main loop
6. **Testing**: Basic pytest structure and example tests
7. **Documentation**: README, docstrings, type hints validation

Each phase includes constitution compliance checks for clean code, type safety, and modularity.
