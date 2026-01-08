import sys
from todo_app.manager import TaskManager
from todo_app.ui import ConsoleUI

def main() -> None:
    """Entry point for the Console Todo Application."""
    manager = TaskManager()
    ui = ConsoleUI()
    
    while True:
        # Requirement FR-008: Always refresh and display table if tasks exist
        tasks = manager.get_all_tasks()
        if tasks:
            ui.display_tasks_table(tasks)
        
        ui.display_menu()
        choice = ui.get_menu_choice()
        
        if choice == "1":
            title, description = ui.get_add_task_input()
            try:
                task_id = manager.add_task(title, description)
                ui.display_success(f"Task added successfully! (ID: {task_id})")
            except ValueError as e:
                ui.display_error(str(e))
        elif choice == "2":
            # Phase 4: View All Tasks (redundant but explicit)
            ui.display_tasks_table(manager.get_all_tasks())
        elif choice == "3":
            # Phase 5: Update Task
            task_id_opt = ui.get_task_id_input("update")
            if task_id_opt is not None:
                task = manager.get_task(task_id_opt)

                if not task:
                    ui.display_error("Task ID not found.")
                else:
                    new_title, new_desc = ui.get_update_task_input(task)
                    try:
                        manager.update_task(task_id, new_title, new_desc)
                        ui.display_success("Task updated successfully!")
                    except ValueError as e:
                        ui.display_error(str(e))
        elif choice == "4":
            # Phase 6: Toggle Status
            toggle_id_opt = ui.get_task_id_input("toggle status")
            if toggle_id_opt is not None:
                if manager.toggle_task_status(toggle_id_opt):

                    ui.display_success("Task status toggled successfully!")
                else:
                    ui.display_error("Task ID not found.")
        elif choice == "5":
            # Phase 7: Delete Task
            delete_id_opt = ui.get_task_id_input("delete")
            if delete_id_opt is not None:
                if manager.delete_task(delete_id_opt):

                    ui.display_success("Task deleted successfully!")
                else:
                    ui.display_error("Task ID not found.")
        elif choice == "6":
            print("\nThank you for using TODO APP! Goodbye!")
            sys.exit(0)
        else:
            ui.display_error("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
