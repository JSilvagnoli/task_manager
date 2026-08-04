import json
import task

def save_json(task_list, filename = "data.json"):
    with open(filename, "w") as outfile:
        task_list_json = [
            task.convert_to_dict()
            for task in task_list
        ]
        json.dump(task_list_json, outfile)

def load_json(file_to_load): 
    if file_to_load is None:
        return []

    #convert back from list of dictionaries to list of task objects
    with open(file_to_load, 'r') as data_file: 
        data = json.load(data_file)
        task_list = task.convert_from_dict(data)
        return task_list