# Data Model: Todo App Full-Stack Implementation

**Feature**: Todo App Full-Stack Implementation
**Date**: 2026-01-08
**Branch**: 001-todo-app

## Entity Definitions

### User Entity
- **Description**: Represents an authenticated user in the system
- **Fields**:
  - `id`: UUID/string (Primary Key, auto-generated)
  - `email`: String (Required, unique, valid email format)
  - `created_at`: DateTime (Auto-generated timestamp)
  - `updated_at`: DateTime (Auto-generated timestamp, updated on changes)

### Todo Entity
- **Description**: Represents a task/todo item owned by a user
- **Fields**:
  - `id`: UUID/string (Primary Key, auto-generated)
  - `title`: String (Required, max 255 characters)
  - `description`: Text (Optional, max 1000 characters)
  - `completed`: Boolean (Default: false)
  - `user_id`: UUID/string (Foreign Key to User.id, required)
  - `created_at`: DateTime (Auto-generated timestamp)
  - `updated_at`: DateTime (Auto-generated timestamp, updated on changes)

## Relationships

### User → Todo (One-to-Many)
- **Type**: One user can own many todos
- **Constraint**: Foreign key relationship with cascade delete
- **Rule**: When a user is deleted, all their todos are also deleted
- **Access Pattern**: User can only access todos where user_id matches their id

## Validation Rules

### User Validation
- Email must be a valid email format
- Email must be unique across all users
- Email length must be between 5 and 255 characters

### Todo Validation
- Title is required and must be 1-255 characters
- Description is optional and limited to 1000 characters
- Completed status must be a boolean value
- User_id must reference an existing user
- User can only modify todos they own

## State Transitions

### Todo Completion
- **Initial State**: `completed = false`
- **Transition**: User can toggle completion status
- **Valid Transitions**: `false ↔ true` (bidirectional)
- **Validation**: Only the owner of the todo can change its completion status

## Indexes

### Required Indexes
- User.email: Unique index for fast lookup and validation
- Todo.user_id: Index for efficient retrieval of user's todos
- Todo.created_at: Index for chronological sorting
- Todo.completed: Index for filtering completed/pending todos

## Constraints

### Referential Integrity
- Todo.user_id must reference an existing User.id
- Cascade delete: When User is deleted, all associated Todos are deleted

### Business Logic Constraints
- Users can only access their own todos
- Todos cannot exist without a valid owner (user)
- Duplicate emails are not allowed