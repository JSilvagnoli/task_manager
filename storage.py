import json

def save_file(task_list, filename="data.json"):
    with open("data.json", "w") as outfile:
        json.dump(task_list, outfile)

def load_file(file_to_load): 
    if file_to_load is None:
        return []

    with open(file_to_load, 'r') as data_file: 
        return json.load(data_file)

