# MedTrack Todo Agent

A patient-centric medication and health task management CLI application designed to help patients manage medication adherence and health-related tasks.

## Overview

MedTrack Todo is a console-based application that allows patients to track their medication doses and health-related activities. The application provides a simple, user-friendly interface focused on medication adherence and health management.

## Features

- **Add Tasks**: Create new medication or health tasks with titles and descriptions
- **View Tasks**: Display all tasks in a tabular format with status indicators
- **Update Tasks**: Modify existing task details
- **Delete Tasks**: Remove tasks that are no longer needed
- **Mark Complete/Incomplete**: Track medication adherence by toggling task status
- **Motivational Messages**: Receive encouraging health quotes upon exit

## Advanced Attributes (Future Features)

The application stores additional attributes for future functionality:
- Priority levels (high/medium/low)
- Category classification (home/work/health/exercise)
- Due dates and reminder times
- Recurring task patterns

## Installation

1. Clone the repository
2. Ensure Python 3.13+ is installed
3. Navigate to the project directory

## Usage

Run the application with:
```bash
python -m src.medtrack_todo.main
```

The application will present a menu with the following options:
1. Add Task
2. View Task List
3. Update Task
4. Delete Task
5. Mark Task Complete / Incomplete
6. Exit

## Architecture

The application follows a clean architecture pattern:
- **Models**: Task data model with all attributes
- **Services**: Business logic for task operations
- **Utils**: Validation and helper functions
- **CLI**: User interface in main.py

## Data Model

Each task contains:
- ID: Unique identifier
- Title: Task name
- Description: Details about the task
- Status: Pending or Completed
- Priority: High/Medium/Low
- Category: Home/Work/Health/Exercise
- Due date: Optional due date
- Reminder time: Optional reminder
- Recurrence pattern: Optional recurrence
- Creation timestamp
- Completion timestamp

## Contributing

This project follows a spec-driven development approach. All changes should be made following the established patterns in the codebase.

## License

This project is part of the "The Evolution of Todo" series, demonstrating the progression from CLI to distributed cloud-native AI systems.