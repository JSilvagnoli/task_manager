import json
from task import Task

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
        print(data)
        task_list = convert_from_dict(data)
        print(task_list)
        return task_list

def convert_to_dict(task):
        return vars(task)

def convert_from_dict(data):
    task_list = []
    for item in data:
        converted_data = Task(**item)
        task_list.append(converted_data)
    return task_list