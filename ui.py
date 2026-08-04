import task_manager
from datetime import datetime

# Display menu options
def display_menu():
    print("==== TASK MANAGER ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Search")
    print("6. Statistics")
    print("7. Sort")
    print("8. Save")
    print("9. Load")
    print("10. Quit")

    while True:
        choice = input("Choice: ")
        if choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
            return choice

        print("Invalid choice. Please enter 1, 2, 3... 10")

def prompt_input_for_task():
    return {
        "task_name": input("Please enter your task's name: "),
        "completion_status": get_valid_task_completion_status(),
        "priority": get_valid_task_priority(),
        "category": input("Please enter your task's category: "),
        "due_date": input("Please enter your task's due date. Example (2000/01/01): ")
    }

def select_task(task_list):
    if not task_list:
        print("No tasks found.")
        return None

    while True:
        choice = input("Which task would you like to update? ")
        task = task_manager.find_task_by_exact_name(task_list, choice)
        if task:
            return task

        print ("Task does not exist. Please choose another task to update.")

def prompt_update_field():
    while True:
        choice = input("Would you like to update 1. Task Name, 2. Completion Status, 3. Priority, 4. Category, 5. Due Date? (Type number, 1, 2, 3, etc.) ")
        if choice in ("1", "2", "3", "4", "5"):
            return choice

        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

def prompt_update_value(field_to_update):
    match int(field_to_update):
        case 1:
            return input("Please enter this task's new name: ")
        case 2:
            return get_valid_task_completion_status()
        case 3:
            return get_valid_task_priority()
        case 4:
            return input("Please enter this task's category: ")
        case 5: 
            return input("Please enter a due date for this task. Example (2000/01/01): ")

def get_valid_task_completion_status():
    while True:
        choice = input("Please enter this task's completion status. Type True for complete, False for incomplete: ").lower()
        if choice == "true":
            return True
        elif choice == "false":
            return False
        else:
            print("Invalid completion status. Please enter True or False: ")

def get_valid_task_priority():
     while True:
        choice = input("Please enter this task's priority -> Low, Medium, or High: ").lower()
        if choice in ("low", "medium", "high"):
            return choice.title()
        
        print("Invalid priority. Please enter Low, Medium, or High")

def prompt_delete_task(task_list):
    while True:
        choice = input("Which task would you like to delete? ")
        task = task_manager.find_task_by_exact_name(task_list, choice)
        if task:
            return task
    
        print("Task does not exist. Please choose another task to delete.")

def prompt_search(task_list):
    while True:
        choice = input("Which task would you like to search for? ")
        found_tasks = task_manager.find_tasks_by_partial_name(task_list, choice)
        if (found_tasks):
            return found_tasks

        print("No Task/s found. Please choose another task to search for.")

def display_found_tasks(tasks):
    print("Found Task/s: ")
    for task in tasks:
        print(task.task_info())

def display_stats(stats):
    print(f"Total Tasks: {stats['total']}")
    print(f"Completed: {stats['complete']}")
    print(f"Incomplete: {stats['incomplete']}")
    print(f"Percentage: {stats['percentage']:.2f}%")

def method_to_sort_tasks():
    while True:
        choice = input(
            "Sort tasks Alphabetically (a), Priority (p), Due Date (d): "
        ).lower()

        if choice in ("a", "p", "d"):
            return choice

        print("Invalid choice. Please enter a, p, or d.")

def file_to_load():
    while True:
        choice = input(
            "Would you like to load the default file (d), another file (a), or none (n)? "
            ).lower()

        if choice == "d":
            return "data.json"
        elif choice == "a":
            return input(
                "(Example: data.json)\n" +
                "Enter JSON filename: "
                )
        elif choice == "n":
            return

        print ("Invalid choice. Please enter d, a, or n.")