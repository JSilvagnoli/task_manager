from datetime import datetime, date

from task import Task

def add_task(task_data, task_list):
    new_task = Task(
        next_available_id(task_list),
		task_data["task_name"],
		task_data["completion_status"],
		task_data["priority"],
		task_data["category"],
		task_data["due_date"]
	)
    task_list.append(new_task)

def next_available_id(task_list):
    next_available_id = 1
    for current_task in task_list:
        current_id = getattr(current_task, "task_id")
        if current_id >= next_available_id:
            next_available_id = current_id + 1
    return next_available_id

def delete_task(task_list, task_to_delete):
    task_index = None

    for index, selected_task in enumerate(task_list):
        if selected_task == task_to_delete:
            task_index = index
            break

    if task_index is not None:
        task_list.pop(task_index)
    else:
        raise ValueError("That task cannot be found and therefore cannot be deleted.")

def find_task_by_exact_name(task_list, choice):
    for found_task in task_list:
        if choice == found_task.task_name:
            return found_task
    return None

def find_tasks_by_partial_name(task_list, choice):
    found_tasks = []
    for found_task in task_list:
        if choice.lower() in found_task.task_name.lower():
            found_tasks.append(found_task)
    return found_tasks

def stats(task_list):
    current_date = date.today()
    print(current_date)
    total = len(task_list)
    complete = sum(1 for Task in task_list if Task.completion_status)
    overdue = sum(1 for Task in task_list if Task.due_date is not None and Task.due_date.date() < current_date and Task.completion_status == False)
    due_today = sum(1 for Task in task_list if Task.due_date is not None and Task.due_date.date() == current_date and Task.completion_status == False)
    high_priority_remaining = sum(1 for Task in task_list if Task.priority == "High" and Task.completion_status == False)

    return {
        "total": total,
        "complete": complete,
        "incomplete": total - complete,
        "overdue": overdue,
        "due_today": due_today,
        "high_priority_remaining": high_priority_remaining,
        "percentage_completed": (complete / total) * 100 if total else 0
        }

def sort_by(sort_method, task_list):
    sorted = SORT_METHOD[str(sort_method)](task_list)
    return sorted

def sort_alphabetical(task_list):
    sorted_list = sorted(task_list, key = lambda x: x.task_name)
    return sorted_list

def sort_priority(task_list):
    sorted_list = sorted(task_list, key = lambda x: (_priority_sort_helper(x), x.task_name))
    return sorted_list

def _priority_sort_helper(task_to_sort):
    if task_to_sort.priority == "High":
        return 0
    elif task_to_sort.priority == "Medium":
        return 1
    elif task_to_sort.priority == "Low":
        return 2
    else:
        return 3

def sort_date(task_list):
    sorted_list = sorted(task_list, key = lambda x: (_due_date_sort_helper(x), x.task_name), reverse = True)
    return sorted_list

def _due_date_sort_helper(task_to_sort):
    if task_to_sort.due_date is None:
        return datetime.min
    return task_to_sort.due_date

SORT_METHOD = {
    "a": sort_alphabetical,
    "p": sort_priority,
    "d": sort_date
}