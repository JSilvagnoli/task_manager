TASK_FIELDS = {
    1: "task",
    2: "completed",
    3: "priority",
    4: "category",
    5: "due_date"
}

# Add a task to the list
def add_task(task_list, task):
    task_list.append(task)
    return task_list

# Create a new task
def create_task(task_name, completed=False, priority=None, category=None, due_date=None):
    return {
        "task": task_name,
        "completed": completed,
        "priority": priority,
        "category": category,
        "due_date": due_date
        }

def find_task(task_list, task_to_update):
    for task in task_list:
        if task["task"] == task_to_update:
            return task

def update_task_field(task, field_to_update, value_to_update):
    chosen_field = TASK_FIELDS.get(int(field_to_update))
    task[chosen_field] = value_to_update
    
def delete_task(task_list, task_name):   
    for task in task_list:
        if task["task"] == task_name:
            task_list.remove(task)
            return True
    return False

# Search
def search(task_list, search_term):
    results = []

    for task in task_list:
        if search_term.lower() in task["task"].lower():
            results.append(task)

    return results
            
def task_info(task):
    return(
        f"Task Name: {task.get('task')} | "
        f"Completed: {task.get('completed')} | "
        f"Priority: {task.get('priority')} | "
        f"Category: {task.get('category')} | "
        f"Due Date: {task.get('due_date')} "
        )

# Displays statistics
def stats(task_list):
    total = len(task_list)
    complete = sum(1 for task in task_list if task["completed"])

    return {
        "total": total,
        "complete": complete,
        "incomplete": total - complete,
        "percentage": (complete / total) * 100 if total else 0
        }

def sort_alphabetical(task_list):
    return sorted(task_list, key = lambda x: x["task"])

def sort_priority(task_list):
    return sorted(task_list, key=_priority_sort_helper)

def _priority_sort_helper(task):
    if task["priority"] == "High":
        return 0
    elif task["priority"] == "Medium":
        return 1
    else:
        return 2

def sort_date(task_list):
    return sorted(task_list, key = lambda x: x["due_date"], reverse = True)
