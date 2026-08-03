import task

def add_task(task_data, task_list):
    new_task = task.Task(
				
		task_data["task_name"],
		task_data["completion_status"],
		task_data["priority"],
		task_data["category"],
		task_data["due_date"]
	)
    new_task.validate_task()
    task_list.append(new_task)

def delete_task(task_list, task_to_delete):   
    for task in task_list:
        if task == task_to_delete:
            task_list.remove(task_to_delete)
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
    task_list.sort(key = lambda x: x.task_name)

def sort_priority(task_list):
    task_list.sort(key = _priority_sort_helper)

def _priority_sort_helper(Task):
    if Task.priority == "High":
        return 0
    elif Task.priority == "Medium":
        return 1
    else:
        return 2

def sort_date(task_list):
    task_list.sort(reverse = True, key = lambda x: x.due_date)

SORT_METHOD = {
    "a": sort_alphabetical,
    "p": sort_priority,
    "d": sort_date
}