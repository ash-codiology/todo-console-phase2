"""
Main CLI application for MedTrack Todo Agent.

Implements the user interface and orchestrates the application flow.
"""
from typing import Optional
import random
from .services.task_service import TaskService
from .constants import (
    APP_NAME, APP_VERSION, HEALTH_MESSAGE, MOTIVATIONAL_QUOTES,
    MENU_OPTIONS, ERROR_MESSAGES, VALID_PRIORITIES, VALID_CATEGORIES
)
from .utils.validators import validate_menu_choice, validate_task_id


class MedTrackTodoApp:
    """
    Main application class for the MedTrack Todo CLI application.
    """

    def __init__(self):
        self.task_service = TaskService()

    def display_menu(self):
        """Display the main menu options."""
        print(f"\nWelcome to {APP_NAME}")
        print("Your Personal Medication Reminder\n")
        for key, value in MENU_OPTIONS.items():
            print(f"{key}. {value}")

    def get_user_input(self, prompt: str) -> str:
        """Get user input with a prompt."""
        return input(prompt).strip()

    def add_task(self):
        """Add a new task to the system."""
        print("\n--- Add Task ---")
        title = self.get_user_input("Enter task title: ")
        description = self.get_user_input("Enter task description: ")

        # Get optional advanced attributes
        print("\nOptional advanced attributes (press Enter to skip):")
        priority_input = self.get_user_input(f"Enter priority ({'/'.join(VALID_PRIORITIES)}, default: medium): ").strip()
        priority = priority_input if priority_input and priority_input in VALID_PRIORITIES else "medium"

        category_input = self.get_user_input(f"Enter category ({'/'.join(VALID_CATEGORIES)}, default: health): ").strip()
        category = category_input if category_input and category_input in VALID_CATEGORIES else "health"

        due_date = self.get_user_input("Enter due date (YYYY-MM-DD, optional): ").strip()
        due_date = due_date if due_date else None

        reminder_time = self.get_user_input("Enter reminder time (HH:MM, optional): ").strip()
        reminder_time = reminder_time if reminder_time else None

        recurrence_pattern = self.get_user_input("Enter recurrence (daily/weekly/monthly/none, optional): ").strip()
        recurrence_pattern = recurrence_pattern if recurrence_pattern in ["daily", "weekly", "monthly", "none"] else None

        try:
            task = self.task_service.add_task(
                title=title,
                description=description,
                priority=priority,
                category=category,
                due_date=due_date,
                reminder_time=reminder_time,
                recurrence_pattern=recurrence_pattern
            )
            print(f"Task '{task.title}' added successfully!")
        except ValueError as e:
            print(f"Error adding task: {e}")

    def view_tasks(self):
        """Display all tasks in the system."""
        print("\n--- View Task List ---")
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks available. Add a task first.")
            return

        # Print header
        print(f"{'ID':<3} | {'Title':<20} | {'Description':<30} | {'Status':<12} | {'Priority':<8} | {'Category':<8}")
        print("-" * 95)

        # Print each task
        for task in tasks:
            # Truncate long titles and descriptions for display
            title = task.title[:19] + '..' if len(task.title) > 19 else task.title
            description = task.description[:28] + '..' if len(task.description) > 28 else task.description
            print(f"{task.id:<3} | {title:<20} | {description:<30} | {task.status:<12} | {task.priority:<8} | {task.category:<8}")

    def update_task(self):
        """Update an existing task."""
        print("\n--- Update Task ---")
        task_id_input = self.get_user_input("Enter task ID to update: ").strip()

        if not validate_task_id(task_id_input, max_id=self.task_service.get_next_id() - 1):
            print(ERROR_MESSAGES["task_id_not_found"])
            return

        task_id = int(task_id_input)
        task = self.task_service.get_task_by_id(task_id)

        if not task:
            print(ERROR_MESSAGES["task_id_not_found"])
            return

        print(f"Current task: {task.title}")
        new_title = self.get_user_input(f"Enter new title (current: '{task.title}', press Enter to keep): ").strip()
        new_title = new_title if new_title else task.title

        new_description = self.get_user_input(f"Enter new description (current: '{task.description}', press Enter to keep): ").strip()
        new_description = new_description if new_description else task.description

        try:
            updated_task = self.task_service.update_task(
                task_id=task_id,
                title=new_title,
                description=new_description
            )
            if updated_task:
                print(f"Task '{updated_task.title}' updated successfully!")
            else:
                print(ERROR_MESSAGES["task_id_not_found"])
        except ValueError as e:
            print(f"Error updating task: {e}")

    def delete_task(self):
        """Delete a task."""
        print("\n--- Delete Task ---")
        task_id_input = self.get_user_input("Enter task ID to delete: ").strip()

        if not validate_task_id(task_id_input, max_id=self.task_service.get_next_id() - 1):
            print(ERROR_MESSAGES["task_id_not_found"])
            return

        task_id = int(task_id_input)
        task = self.task_service.get_task_by_id(task_id)

        if not task:
            print(ERROR_MESSAGES["task_id_not_found"])
            return

        confirm = self.get_user_input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            success = self.task_service.delete_task(task_id)
            if success:
                print(f"Task '{task.title}' deleted successfully!")
            else:
                print(ERROR_MESSAGES["task_id_not_found"])
        else:
            print("Deletion cancelled.")

    def toggle_task_status(self):
        """Toggle a task's status between pending and completed."""
        print("\n--- Mark Task Complete / Incomplete ---")
        task_id_input = self.get_user_input("Enter task ID to toggle status: ").strip()

        if not validate_task_id(task_id_input, max_id=self.task_service.get_next_id() - 1):
            print(ERROR_MESSAGES["task_id_not_found"])
            return

        task_id = int(task_id_input)
        task = self.task_service.get_task_by_id(task_id)

        if not task:
            print(ERROR_MESSAGES["task_id_not_found"])
            return

        toggled_task = self.task_service.toggle_task_status(task_id)
        if toggled_task:
            print(f"Task '{toggled_task.title}' marked as {toggled_task.status}.")
        else:
            print(ERROR_MESSAGES["task_id_not_found"])

    def exit_app(self):
        """Exit the application with a thank you message and random quote."""
        print(f"\nThank you for using {APP_NAME}. {HEALTH_MESSAGE}")
        random_quote = random.choice(MOTIVATIONAL_QUOTES)
        print(random_quote)

    def run(self):
        """Run the main application loop."""
        while True:
            self.display_menu()
            choice = self.get_user_input("\nSelect an option (1-6): ")

            if validate_menu_choice(choice):
                option = int(choice)
                if option == 1:
                    self.add_task()
                elif option == 2:
                    self.view_tasks()
                elif option == 3:
                    self.update_task()
                elif option == 4:
                    self.delete_task()
                elif option == 5:
                    self.toggle_task_status()
                elif option == 6:
                    self.exit_app()
                    break
            else:
                print(ERROR_MESSAGES["invalid_menu_option"])


def main():
    """Entry point for the application."""
    app = MedTrackTodoApp()
    app.run()


if __name__ == "__main__":
    main()