"""
Presentation layer for the Todo Application.
Handles console input/output and task formatting.
"""
from typing import List, Optional
from .models import Task

class ConsoleUI:
    """
    Handles all user interaction, formatting, and console output.
    
    This class is pure presentation layer and contains no business logic.
    """
    
    def display_menu(self) -> None:
        """Display the main application menu."""
        print("\n" + "="*80)
        print("                         TODO APP - TASK MANAGER")
        print("="*80)
        print("\nWhat would you like to do?")
        print("\n  [1] Add New Task")
        print("  [2] View All Tasks")
        print("  [3] Update Task")
        print("  [4] Mark Task Complete/Incomplete")
        print("  [5] Delete Task")
        print("  [6] Exit")
        
    def get_menu_choice(self) -> str:
        """
        Get and return user's menu selection.
        
        Returns:
            The trimmed string input from the user.
        """
        return input("\nEnter your choice (1-6): ").strip()

    def get_add_task_input(self) -> tuple[str, str]:
        """
        Collect title and description for a new task.
        
        Returns:
            A tuple of (title, description).
        """
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional, press Enter to skip): ").strip()
        return title, description

    def get_update_task_input(self, current_task: Task) -> tuple[Optional[str], Optional[str]]:

        """
        Collect updated title and description for an existing task.
        
        Args:
            current_task: The task as it currently exists.
            
        Returns:
            A tuple of (optional title, optional description).
        """
        print("\n--- Update Task ---")
        print(f"Current title: {current_task.title}")
        new_title = input("Enter new title (or press Enter to keep current): ").strip()
        
        print(f"Current description: {current_task.description}")
        new_desc = input("Enter new description (or press Enter to keep current): ").strip()
        
        return (new_title if new_title else None, 
                new_desc if new_desc else None)

    def get_task_id_input(self, action: str) -> Optional[int]:
        """
        Prompt user for a task ID and validate numeric input.
        
        Args:
            action: The operation being performed (for messaging).
            
        Returns:
            The integer ID if valid, None otherwise.
        """
        try:
            val = input(f"Enter task ID to {action}: ").strip()
            if not val:
                return None
            return int(val)
        except ValueError:
            self.display_error("Invalid input. Please enter a numeric task ID.")
            return None

    def display_error(self, message: str) -> None:
        """Display an error message to the console."""
        print(f"\n[ERROR] {message}")


    def display_success(self, message: str) -> None:
        """Display a success message to the console."""
        print(f"\n[SUCCESS] {message}")


    def display_tasks_table(self, tasks: List[Task]) -> None:
        """
        Display tasks in a formatted 80-character width table.
        
        Args:
            tasks: List of Task objects to display.
        """
        if not tasks:
            print("\nNo tasks found. Add your first task!")
            return
            
        print("\n" + "="*80)
        print(f"{'ID':<5} {'Status':<8} {'Title':<30} {'Description':<35}")
        print("="*80)
        
        for task in tasks:
            status_icon = "[x]" if task.status else "[ ]"
            # Truncate title and description for table view (Total width: Title=30, Desc=35)
            title = (task.title[:28] + "..") if len(task.title) > 30 else task.title
            desc = (task.description[:33] + "..") if len(task.description) > 35 else task.description
            
            print(f"{task.id:<5} {status_icon:<8} {title:<30} {desc:<35}")
            
        print("="*80)
