# CLI Interface Contract: Console Todo App

**Feature**: 001-console-todo-app  
**Date**: 2026-01-02  
**Type**: Command-Line Interface Specification

## Overview

This document specifies the console user interface contract, including menu structure, command flow, input/output formats, and error handling for the Todo App.

## Main Menu Structure

### Display Format

```
================================================================================
                         📝 TODO APP - TASK MANAGER
================================================================================

Current Tasks:
================================================================================
ID    Status   Title                          Description                        
================================================================================
1     [ ]      Buy groceries                  Milk, eggs, bread                  
2     [x]      Finish project report          Complete by Friday                 
================================================================================

What would you like to do?

  [1] Add New Task
  [2] View All Tasks
  [3] Update Task
  [4] Mark Task Complete/Incomplete
  [5] Delete Task
  [6] Exit

Enter your choice (1-6):
```

### Menu Behavior

- **Always Display**: Task table appears above menu after every operation
- **Empty State**: If no tasks exist, show "No tasks found. Add your first task!" instead of table
- **Continuous Loop**: Menu re-displays after each operation completes (except Exit)
- **Invalid Input**: Display "Invalid choice. Please enter a number between 1 and 6." and re-prompt

## Command Flows

### 1. Add New Task

```
Enter your choice (1-6): 1

--- Add New Task ---
Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, eggs, bread

✓ Task added successfully! (ID: 1)

[Task table displays with new task]
[Main menu re-displays]
```

#### Input Validation
- **Empty Title**: Display error "Title cannot be empty. Please try again." and return to menu
- **Empty Description**: Accept and store as `""`

---

### 2. View All Tasks

```
Enter your choice (1-6): 2

[Task table displays]
[Main menu re-displays]
```

#### Behavior
- Identical to task table always displayed above menu
- Redundant operation but included for explicit user action

---

### 3. Update Task

```
Enter your choice (1-6): 3

--- Update Task ---
Enter task ID to update: 1
Current title: Buy groceries
Enter new title (or press Enter to keep current): Buy groceries and snacks
Current description: Milk, eggs, bread
Enter new description (or press Enter to keep current): Milk, eggs, bread, chips

✓ Task updated successfully!

[Task table displays with updated task]
[Main menu re-displays]
```

#### Input Validation
- **Invalid ID**: Display error "Task ID not found. Please check the task list and try again."
- **Non-Numeric ID**: Display error "Invalid input. Please enter a numeric task ID."
- **Empty Title Update**: If user provides empty string when replacing title, display error "Title cannot be empty" and task remains unchanged
- **Empty Description Update**: Accept and store as `""`

#### Update Behavior
- Pressing Enter without typing keeps current value
- Only provided fields are updated (title-only, description-only, or both)

---

### 4. Mark Task Complete/Incomplete (Toggle)

```
Enter your choice (1-6): 4

--- Toggle Task Status ---
Enter task ID: 1

✓ Task marked as complete!

[Task table displays with updated status: [x]]
[Main menu re-displays]
```

#### Toggle Behavior
- **Incomplete → Complete**: Display "Task marked as complete!"
- **Complete → Incomplete**: Display "Task marked as incomplete!"
- Reversible unlimited times

#### Input Validation
- **Invalid ID**: Display error "Task ID not found. Please check the task list and try again."
- **Non-Numeric ID**: Display error "Invalid input. Please enter a numeric task ID."

---

### 5. Delete Task

```
Enter your choice (1-6): 5

--- Delete Task ---
Enter task ID to delete: 1

✓ Task 1 deleted successfully!

[Task table displays without deleted task]
[Main menu re-displays]
```

#### Input Validation
- **Invalid ID**: Display error "Task ID not found. Please check the task list and try again."
- **Non-Numeric ID**: Display error "Invalid input. Please enter a numeric task ID."

#### Deletion Behavior
- Permanent removal from memory
- No confirmation prompt (immediate deletion)
- ID never reused for future tasks

---

### 6. Exit

```
Enter your choice (1-6): 6

Thank you for using TODO APP! Goodbye! 👋

[Application terminates]
```

## Table Formatting Specification

### Column Layout

| Column | Width | Alignment | Content |
|--------|-------|-----------|---------|
| ID | 5 chars | Left | Integer task ID |
| Status | 8 chars | Left | `[ ]` or `[x]` |
| Title | 30 chars | Left | Truncate with ".." if >30 |
| Description | 35 chars | Left | Truncate with ".." if >35 |

**Total Width**: 80 characters (standard terminal compatibility)

### Implementation Example

```python
def display_tasks_table(self, tasks: List[Task]) -> None:
    """Display tasks in formatted table."""
    if not tasks:
        print("\nNo tasks found. Add your first task!")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Status':<8} {'Title':<30} {'Description':<35}")
    print("="*80)
    
    for task in tasks:
        status_icon = "[x]" if task.status else "[ ]"
        title = (task.title[:28] + "..") if len(task.title) > 30 else task.title
        desc = (task.description[:33] + "..") if len(task.description) > 35 else task.description
        
        print(f"{task.id:<5} {status_icon:<8} {title:<30} {desc:<35}")
    
    print("="*80 + "\n")
```

## Error Messages

### Standard Error Format

```
❌ [Error Message]
[Blank line]
[Return to main menu]
```

### Error Catalog

| Error Code | Error Message | Trigger Condition |
|------------|---------------|-------------------|
| ERR-001 | Title cannot be empty | Empty or whitespace-only title during add/update |
| ERR-002 | Task ID not found. Please check the task list and try again. | ID doesn't exist in storage |
| ERR-003 | Invalid input. Please enter a numeric task ID. | Non-numeric input where ID expected |
| ERR-004 | Invalid choice. Please enter a number between 1 and 6. | Menu choice outside 1-6 range |

## Success Messages

### Standard Success Format

```
✓ [Success Message]
[Blank line]
[Display updated task table]
[Return to main menu]
```

### Success Catalog

| Operation | Success Message |
|-----------|----------------|
| Add Task | Task added successfully! (ID: [id]) |
| Update Task | Task updated successfully! |
| Toggle Complete | Task marked as complete! |
| Toggle Incomplete | Task marked as incomplete! |
| Delete Task | Task [id] deleted successfully! |

## Input/Output Patterns

### Input Handling

```python
def get_user_input(self, prompt: str) -> str:
    """Get user input with prompt."""
    return input(prompt).strip()

def get_task_id_input(self) -> Optional[int]:
    """Get and validate task ID input."""
    try:
        task_id = int(input("Enter task ID: ").strip())
        return task_id
    except ValueError:
        self.display_error("Invalid input. Please enter a numeric task ID.")
        return None
```

### Output Formatting

- **Headers**: All caps, centered or left-aligned with visual separators
- **Tables**: Fixed-width columns with `=` borders
- **Messages**: Emoji icons for visual clarity (✓ success, ❌ error, 📝 branding)
- **Spacing**: Blank line before/after tables and messages for readability

## Accessibility Considerations

- **Plain Text**: No color codes (cross-platform terminal compatibility)
- **Visual Indicators**: Use ASCII symbols (`[ ]`, `[x]`) not just color
- **Clear Labels**: All prompts explicitly state what input is expected
- **Reversible Actions**: Toggle allows undo of status changes

## Performance Requirements

- **Table Rendering**: <200ms for up to 100 tasks
- **Menu Display**: <50ms (instant user perception)
- **Input Response**: <10ms from Enter keypress to action initiation

## Future Enhancements (Phase II+)

- Color coding for status (green = complete, yellow = incomplete)
- Pagination for large task lists (>50 tasks)
- Search/filter commands
- Sort options (by date, title, status)
- Bulk operations (delete all completed, mark all incomplete)
