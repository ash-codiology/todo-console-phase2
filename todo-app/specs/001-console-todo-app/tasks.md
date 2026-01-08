# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/cli-interface.md, research.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure using UV

- [x] T001 Create project directory structure `todo-console-app/src/todo_app/` and `todo-console-app/tests/`
- [x] T002 Initialize UV project with `uv init --python 3.12` in `todo-console-app/`
- [x] T003 [P] Configure `todo-console-app/pyproject.toml` with `pytest` dev dependency and project metadata

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure and base classes required for all features

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Implement `Task` dataclass in `todo-console-app/src/todo_app/models.py` per `data-model.md`
- [x] T005 Implement `TaskManager` class with in-memory storage and ID generator in `todo-console-app/src/todo_app/manager.py`
- [x] T006 Implement `ConsoleUI` class with basic formatted input/output methods in `todo-console-app/src/todo_app/ui.py`
- [x] T007 [P] Create basic `pytest` configuration and `__init__.py` files in `todo-console-app/tests/`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to quickly capture tasks with a title and optional description.

**Independent Test**: Run `main.py`, select "Add Task", provide title "Buy milk", verify success message and that task is assigned ID 1.

### Implementation for User Story 1

- [x] T008 [US1] Implement `TaskManager.add_task(title, description)` with validation in `todo-console-app/src/todo_app/manager.py`
- [x] T009 [US1] Implement `ConsoleUI.get_add_task_input()` in `todo-console-app/src/todo_app/ui.py`
- [x] T010 [US1] Implement main loop and Add Task menu integration in `todo-console-app/src/todo_app/main.py`
- [x] T011 [P] [US1] Create unit tests for task creation in `todo-console-app/tests/test_manager.py`

**Checkpoint**: Add Task feature functional and testable

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1) 🎯 MVP

**Goal**: Display all tasks in a formatted table with status indicators.

**Independent Test**: Add 2 tasks, select "View All Tasks", verify they appear in an 80-char width table with `[ ]` status.

### Implementation for User Story 2

- [x] T012 [US2] Implement `TaskManager.get_all_tasks()` in `todo-console-app/src/todo_app/manager.py`
- [x] T013 [US2] Implement `ConsoleUI.display_tasks_table(tasks)` as specified in `cli-interface.md` in `todo-console-app/src/todo_app/ui.py`
- [x] T014 [US2] Integrate View All Tasks and ensure table displays after every operation in `todo-console-app/src/todo_app/main.py`
- [x] T015 [P] [US2] Create unit tests for retrieving tasks in `todo-console-app/tests/test_manager.py`

**Checkpoint**: Full View/Add loop complete (MVP Scope reached)

---

## Phase 5: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Allow users to modify title or description of existing tasks.

**Independent Test**: select "Update Task", enter valid ID, provide new title, verify table reflects change.

### Implementation for User Story 3

- [x] T016 [US3] Implement `TaskManager.update_task(task_id, title, description)` in `todo-console-app/src/todo_app/manager.py`
- [x] T017 [US3] Implement `ConsoleUI.get_update_task_input(current_task)` in `todo-console-app/src/todo_app/ui.py`
- [x] T018 [US3] Integrate Update Task flow in `todo-console-app/src/todo_app/main.py`
- [x] T019 [P] [US3] Create unit tests for updating tasks in `todo-console-app/tests/test_manager.py`

**Checkpoint**: Task modification feature functional

---

## Phase 6: User Story 4 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Toggle task status between complete and incomplete.

**Independent Test**: select "Toggle Status", enter ID, verify status icon changes from `[ ]` to `[x]`.

### Implementation for User Story 4

- [x] T020 [US4] Implement `TaskManager.toggle_task_status(task_id)` in `todo-console-app/src/todo_app/manager.py`
- [x] T021 [US4] Integrate Toggle Status flow in `todo-console-app/src/todo_app/main.py`
- [x] T022 [P] [US4] Create unit tests for status toggling in `todo-console-app/tests/test_manager.py`

**Checkpoint**: Task completion tracking functional

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Permanently remove tasks from memory.

**Independent Test**: select "Delete Task", enter ID, verify task no longer appears in table.

### Implementation for User Story 5

- [x] T023 [US5] Implement `TaskManager.delete_task(task_id)` in `todo-console-app/src/todo_app/manager.py`
- [x] T024 [US5] Integrate Delete Task flow in `todo-console-app/src/todo_app/main.py`
- [x] T025 [P] [US5] Create unit tests for task deletion in `todo-console-app/tests/test_manager.py`

**Checkpoint**: All user stories functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, type safety, and final validation

- [x] T026 [P] Add Google-style docstrings to all modules in `todo-console-app/src/todo_app/`
- [x] T027 [P] Configure `mypy` for strict type checking in `todo-console-app/pyproject.toml`
- [x] T028 [P] Create comprehensive `todo-console-app/README.md` based on `quickstart.md`
- [x] T029 Run all tests via `uv run pytest` and perform final manual walkthrough of all 5 operations

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - MUST be first.
- **Foundational (Phase 2)**: Depends on Setup - BLOCKS all story implementation.
- **User Stories (Phases 3-7)**: All depend on Foundational.
  - US1 and US2 (P1) are the highest priority and should be completed first to reach MVP.
  - US3, US4, US5 follow in priority order.
- **Polish (Phase 8)**: Final step after all features are implemented.

### Parallel Opportunities

- Unit test tasks (`T011`, `T015`, etc.) can be written in parallel with their implementation.
- Docstrings (`T026`) and configuration (`T027`) can be done as soon as files exist.
- User stories could theoretically proceed in parallel once `manager.py` and `ui.py` base classes exist, but sequential implementation is recommended for this single-developer project.

---

## Implementation Strategy

### MVP First (User Stories 1 & 2)

1. Complete Phase 1 & 2 (Setup & Foundational).
2. Complete Phase 3 (Add Tasks) and Phase 4 (View Tasks).
3. **STOP and VALIDATE**: Verify the "Add -> View" loop works perfectly.

### Incremental Delivery

1. Foundation -> Solid core.
2. US1 + US2 -> Primary value (Add/List).
3. US3 + US4 -> Core management (Update/Complete).
4. US5 -> Cleanup (Delete).
5. Polish -> Production readiness.
