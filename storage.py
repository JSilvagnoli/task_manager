import json
from task import Task
from datetime import datetime 

def save_json(task_list, filename = "data.json"):
    with open(filename, "w") as outfile:
        task_list_json = [
            convert_to_dict(task)
            for task in task_list
        ]
        json.dump(task_list_json, outfile)

def load_json(file_to_load): 
    if file_to_load is None:
        return []

    #convert back from list of dictionaries to list of task objects
    with open(file_to_load, 'r') as data_file: 
        data = json.load(data_file)
        task_list = convert_from_dict(data)
        return task_list

def convert_to_dict(task):
    return {
        "task_id": task.task_id,
        "task_name": task.task_name,
        "completion_status": task.completion_status,
        "priority": task.priority,
        "category": task.category,
        "due_date":
	        task.due_date.strftime("%Y/%m/%d")
	        if task.due_date is not None
	        else None
    }

def convert_from_dict(data):
    task_list = []
    
    for item in data:
        if item["due_date"] is not None:
            item["due_date"] = datetime.strptime(
                item["due_date"],
                "%Y/%m/%d"
            )
        task_list.append(Task(**item))
    return task_list