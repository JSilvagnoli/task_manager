import task

# Display menu options
def display_menu():
    print("==== TASK MANAGER ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Search")
    print("6. Statistics")
    print("7. Save")
    print("8. Load")
    print("9. Quit")

    return input("Choice: ")

# Dispaly individual tasks and statuses
def display_tasks(task_list):
    for item in task_list:
        print(task.task_info(item))

def prompt_input_for_task():
    task_name = input("Task name: ")
    status = input("Completed? True/False: ").lower() == "true"
    priority = input("Priority: ")
    category = input("Category: ")
    due_date = input("Due date: ")

    return {
        "task": task_name,
        "completed": status,
        "priority": priority,
        "category": category,
        "due_date": due_date
    }

def prompt_task_name():
    print("Which task would you like to update?")
    task_to_update = input()
    return task_to_update

def prompt_update_field():
    print("Would you like to update the 1. Task Name, 2. Completion Status, 3. Priority, 4. Category, 5. Due Date? (Type number, 1, 2, 3, etc.)")
    field_to_update = input()
    return field_to_update

def prompt_update_value(field_to_update):
    match int(field_to_update):
        case 1:
            print("Please enter this task's new name")
            value_to_update = input()
        case 2:
            print("Type True for complete, False for incomplete")
            value_to_update = input().lower() == "true"
        case 3:
            print("Please enter this task's priority -> Low, Medium, High")
            value_to_update = input()
        case 4:
            print("Please enter this task's category")
            value_to_update = input()
        case 5: 
            print("Please enter this task's due date")
            value_to_update = input()

    return value_to_update

def prompt_delete_task():
    return input("Which task would you like to delete? ")

def task_to_find():
    print("Enter task to search for")
    task_to_find = input()
    return task_to_find

def prompt_search():
    return input("Enter task to search for: ")

def display_stats(stats):
    print(f"Total Tasks: {stats['total']}")
    print(f"Completed: {stats['complete']}")
    print(f"Incomplete: {stats['incomplete']}")
    print(f"Percentage: {stats['percentage']:.2f}%")

def file_to_load():
    print("Would you like to load the default file (d), or another file (a)?")
    choice = input().lower()

    if choice == "d":
        file_to_load = "data.json"
    else:
        print("Please enter the name of your json file saved in the same folder as this project. Example: data.json")
        file_to_load = input()

    return file_to_load