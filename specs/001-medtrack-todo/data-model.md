# Data Model: MedTrack Todo Agent

## Task Entity

### Attributes

| Field | Type | Default | Required | Description |
|-------|------|---------|----------|-------------|
| id | int | Auto-generated | Yes | Unique identifier, auto-incremented |
| title | str | N/A | Yes | Medicine or health task name |
| description | str | N/A | Yes | Dose, timing, notes |
| status | str | "Pending" | Yes | "Pending" or "Completed" |
| priority | str | "medium" | No | "high", "medium", "low" - for future filtering |
| category | str | "health" | No | "home", "work", "health", "exercise" - for future organization |
| due_date | str | null | No | Optional due date in YYYY-MM-DD format - for future reminders |
| reminder_time | str | null | No | Optional reminder time in HH:MM format - for future notifications |
| recurrence_pattern | str | null | No | Optional recurrence pattern - for future recurring tasks |
| created_at | str | Current timestamp | Yes | Timestamp of task creation - for future analytics |
| completed_at | str | null | No | Optional timestamp when task was completed - for future analytics |

### Validation Rules

1. **id**: Must be unique, auto-generated, positive integer
2. **title**: Required, non-empty string, max 200 characters
3. **description**: Required, non-empty string, max 500 characters
4. **status**: Must be either "Pending" or "Completed"
5. **priority**: If provided, must be one of "high", "medium", "low"
6. **category**: If provided, must be one of "home", "work", "health", "exercise"
7. **due_date**: If provided, must be in YYYY-MM-DD format
8. **reminder_time**: If provided, must be in HH:MM format
9. **recurrence_pattern**: If provided, must be one of "daily", "weekly", "monthly", "none"

### State Transitions

- **Status**: "Pending" ↔ "Completed" (toggle operation)
- **created_at**: Set once on creation, never modified
- **completed_at**: Set when status changes to "Completed", cleared when status changes back to "Pending"

## TaskList Entity

### Attributes

| Field | Type | Description |
|-------|------|-------------|
| tasks | List[Task] | Collection of Task objects in memory |
| next_id | int | Next available ID for auto-generation |

### Operations

1. **Add Task**: Add new task to the list, auto-generate ID
2. **Get All Tasks**: Return all tasks in the list
3. **Get Task by ID**: Return specific task by ID
4. **Update Task**: Modify existing task by ID
5. **Delete Task**: Remove task by ID
6. **Toggle Status**: Change task status between "Pending" and "Completed"

### Validation Rules

1. No duplicate IDs allowed
2. ID must exist for update/delete operations
3. Tasks list must not exceed memory constraints