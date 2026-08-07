import json
from datetime import datetime

from task import Task

def save_json(task_list, filename = "data.json"):
    with open(filename, "w") as outfile:
        task_list_json = [
            convert_to_dict(task_to_use)
            for task_to_use in task_list
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

def convert_to_dict(task_to_convert):
    return {
        "task_id": task_to_convert.task_id,
        "task_name": task_to_convert.task_name,
        "completion_status": task_to_convert.completion_status,
        "priority": task_to_convert.priority,
        "category": task_to_convert.category,
        "due_date":
	        task_to_convert.due_date.strftime("%Y/%m/%d")
	        if task_to_convert.due_date is not None
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