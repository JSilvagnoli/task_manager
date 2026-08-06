import task
import datetime

def add_task(task_data, task_list):
    new_task = task.Task(
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
    for task in task_list:
        current_id = getattr(task, "task_id")
        if current_id >= next_available_id:
            next_available_id = current_id + 1
    return next_available_id

def delete_task(task_list, task_to_delete):
    task_index = None

    for index, task in enumerate(task_list):
        if task == task_to_delete:
            task_index = index
            break

    if task_index is not None:
        task_list.pop(task_index)
    else:
        raise ValueError("That task cannot be found and therefore cannot be deleted.")

def find_task_by_exact_name(task_list, choice):
    for task in task_list:
        if choice == task.task_name:
            return task
    return None

def find_tasks_by_partial_name(task_list, choice):
    found_tasks = []
    for task in task_list:
        if choice.lower() in task.task_name.lower():
            found_tasks.append(task)
    return found_tasks

def stats(task_list):
    total = len(task_list)
    complete = sum(1 for Task in task_list if Task.completion_status)

    return {
        "total": total,
        "complete": complete,
        "incomplete": total - complete,
        "percentage": (complete / total) * 100 if total else 0
        }

def sort_by(sort_method, task_list):
    sorted = SORT_METHOD[str(sort_method)](task_list)
    return sorted

def sort_alphabetical(task_list):
    sorted_list = sorted(task_list, key = lambda x: x.task_name)
    return sorted_list

def sort_priority(task_list):
    sorted_list = sorted(task_list, key = _priority_sort_helper)
    return sorted_list

def _priority_sort_helper(task):
    if task.priority == "High":
        return 0
    elif task.priority == "Medium":
        return 1
    elif task.priority == "Low":
        return 2
    else:
        return 3

def sort_date(task_list):
    sorted_list = sorted(task_list, key = _due_date_sort_helper, reverse = True)
    return sorted_list

def _due_date_sort_helper(task):
    if task.due_date is None:
        return datetime.min
    return task.due_date

SORT_METHOD = {
    "a": sort_alphabetical,
    "p": sort_priority,
    "d": sort_date
}