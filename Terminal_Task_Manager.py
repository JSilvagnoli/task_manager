import sys
import re
import json

# List of tasks and statuses
def main():
    task_list = [
    {"task": "Wash Car", "completed": True, "priority": "Low", "category": "Cleaning", "date": "2026/03/01"},
    {"task": "Study Python", "completed": False, "priority": "High", "category": "Education", "date": "2027/12/15"},
    {"task": "Buy Milk", "completed": False, "priority": "Medium", "category": "Groceries", "date": "2026/05/28"}
    ]

    while True:
        choice = display_menu()
        task_list = choices(choice, task_list)

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
def view_tasks(task_list):
    for task in task_list:
        print_task_info(task)

# Add a task to the list
def add_task(task_list):
    print("Please type the name of your task")
    task_name = input()
    print("Please type the completion status of your task - True/False")
    status = input().lower() == "true"
    print("Please enter the priority of this task - Low, Medium, High")
    priority = input()
    print("Please add a category for this task - Work, Studying, Etc.")
    category = input()
    print("Please add a due date for this task - YYYY/MM/DD")
    due_date = input()

    new_task = create_task(task_name, status, priority, category, due_date)
    task_list.append(new_task)

# Create a new task
def create_task(task_name, completed=False, priority=None, category=None, due_date=None):
    return {
        "task": task_name,
        "completed": completed,
        "priority": priority,
        "category": category,
        "date": due_date
        }

# Change status of task
def update_task(task_list):
    task_update = task_to_update()
    field_update = field_to_update()
    value_update = value_to_update(field_update)
    task = find_task_to_update(task_list, task_update)
    update_task_field(task, field_update, value_update)

def task_to_update():
    print("Which task would you like to update?")
    task_to_update = input()
    return task_to_update

def field_to_update():
    print("Would you like to update the 1. Task Name, 2. Completion Status, 3. Priority, 4. Category, 5. Due Date? (Type number, 1, 2, 3, etc.)")
    field_to_update = input()
    return field_to_update

def value_to_update(field_to_update):
    match int(field_to_update):
        case 1:
            print("Please enter this task's new name")
            value_to_update = input()
        case 2:
            print("Type True for complete, False for incomplete")
            value_to_update = input()
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


def find_task_to_update(task_list, task_to_update):
    for task in task_list:
        if task["task"] == task_to_update:
            return task

def update_task_field(task, field_to_update, value_to_update):
    fields = {1: "task", 2: "completed", 3: "priority", 4: "category", 5: "date"}
    chosen_field = fields.get(int(field_to_update))
    task[str(chosen_field)] = value_to_update

# Delete task
def delete_task(task_list):
    print("Which task would you like to delete?")
    task_to_delete = input()
    for task in task_list:
        if task["task"] == task_to_delete:
            task_list.remove(task)
            break

# Search
def search(task_list):
    print("Enter task to search for")
    task_to_find = input()
    for task in task_list:
        if task_to_find.lower() in task["task"].lower():
            print_task_info(task)
            
# Helper to print task information
def print_task_info(task):
    print("Task Name: " + task.get("task") + 
          " | Completed: " + str(task.get("completed")) + 
          " | Priority: " + str(task.get("priority")) + 
          " | Category: " + str(task.get("category")) + 
          " | Due Date: " + str(task.get("date"))
          )

# Displays statistics
def stats(task_list):
    total = len(task_list)
    complete = 0
    incomplete = 0
    percent = 0
    for task in task_list:
        if task["completed"]:
            complete += 1
        else:
            incomplete += 1
    if len(task_list) > 0:
        percent = (complete/total) * 100
    print("Total Tasks: " + str(total))
    print("Completed Tasks: " + str(complete))
    print("Remaining Tasks: " + str(incomplete))
    print("Completion Percentage: " + str(f"{percent:.2f}") + "%")

def sort_alphabetical(task_list):
    return sorted(task_list, key = lambda x: x["task"])

def sort_priority(task_list):
    return sorted(task_list, key=priority_sort_helper)

def priority_sort_helper(task):
    if task["priority"] == "High":
        return 0
    elif task["priority"] == "Medium":
        return 1
    else:
        return 2

def sort_date(task_list):
    return sorted(task_list, key = lambda x: x["date"], reverse = True)

def save_file(task_list):
    with open("data.json", "w") as outfile:
        json.dump(task_list, outfile)

def file_to_load():
    print("Would you like to load the default file (d), or another file (a)?")
    choice = input().lower()
    if choice == "d":
        file_to_load = "data.json"
    else:
        print("Please type the name of your json file saved in the same folder as this project. Example: data.json")
        file_to_load = input()
    
    loaded_file = load_file(file_to_load)
    return loaded_file

def load_file(file_to_load): 
    with open(file_to_load, 'r') as data_file: 
        loaded_file = json.load(data_file) 

    return loaded_file

def choices(user_input, task_list):
    match int(user_input):
        case 1:
            #task_list = sort_alphabetical(task_list)
            #task_list = sort_priority(task_list)
            task_list = sort_date(task_list)
            view_tasks(task_list)
        case 2:
            add_task(task_list)
        case 3:
            update_task(task_list)
        case 4:
            delete_task(task_list)
        case 5: 
            search(task_list)
        case 6:
            stats(task_list)
        case 7:
            save_file(task_list)
        case 8: 
            task_list = file_to_load()
        case 9:
            sys.exit()
        case _:
            display_menu() 

    return task_list

main()