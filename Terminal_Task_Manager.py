import sys
import re
import json

# List of tasks and statuses
def main():
    task_list = [
            {"task": "Buy Milk", "completed": False},
            {"task": "Wash Car", "completed": True},
            {"task": "Study Python", "completed": False}
            ]

    while True:
        choice = display_menu()
        task_list = choices(choice, task_list)

# Display menu options
def display_menu():
    print("==== TASK MANAGER ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Create Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Search")
    print("7. Statistics")
    print("8. Save")
    print("9. Load")
    print("10. Quit")

    return input("Choice: ")

# Dispaly individual tasks and statuses
def display_tasks(task_list):
    for index in task_list:
        print_task_info(index)

# Add a task to the list
def add_task(task_list):
    print("Please type the name of your task")
    task_name = input()
    print("Please type the completion status of your task - True/False")
    status = input().lower() == "true"

    new_task = create_task(task_name, status)
    task_list.append(new_task)

# Create a new task
def create_task(task_name, completed=False):
    return {
        "task": task_name,
        "completed": completed
        }

# Change status of task
def update_task(task_list):
    print("Which task would you like to update?")
    task_to_update = input()
    print("Type True for complete, False for incomplete")
    status = input().lower() == "true"
    for index in task_list:
        if index["task"] == task_to_update:
            index["completed"] = status
            break

# Delete task
def delete_task(task_list):
    print("Which task would you like to delete?")
    task_to_delete = input()
    for index in task_list:
        if index["task"] == task_to_delete:
            task_list.remove(index)
            break

# Search
def search(task_list):
    print("Enter task to search for")
    task_to_find = input()
    for index in task_list:
        if task_to_find.lower() in index["task"].lower():
            print_task_info(index)
            
# Helper to print task information
def print_task_info(index):
    if index["completed"]:
        print("[X] " + index.get("task"))
    else:
        print("[] " + index.get("task"))

# Displays statistics
def stats(task_list):
    total = len(task_list)
    complete = 0
    incomplete = 0
    percent = 0
    for index in task_list:
        if index["completed"]:
            complete += 1
        else:
            incomplete += 1
    if len(task_list) > 0:
        percent = (complete/total) * 100
    print("Total Tasks: " + str(total))
    print("Completed Tasks: " + str(complete))
    print("Remaining Tasks: " + str(incomplete))
    print("Completion Percentage: " + str(f"{percent:.2f}") + "%")

# Save to JSON
def save_file(task_list):
    with open("data.json", "w") as outfile:
        json.dump(task_list, outfile)

# Load from JSON
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

# Load from JSON 
def load_file(file_to_load): 
    with open(file_to_load, 'r') as data_file: 
        loaded_file = json.load(data_file) 

    return loaded_file

def choices(user_input, task_list):
    match int(user_input):
        case 1:
            display_tasks(task_list)
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