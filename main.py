import sys
import task
import storage
import task_manager
import ui

def main():
	task_list = storage.load_json(ui.file_to_load())

	while True:
		task_list = handle_menu_choice(ui.display_menu(), task_list)

def handle_menu_choice(user_input, task_list):
	handler = COMMANDS.get(user_input)
	if handler:
		return handler(task_list)
	
	print("Invalid input.")
	return task_list

def display_menu():
	ui.display_menu() 

def view_tasks(task_list):
	ui.display_found_tasks(task_list)
	return task_list

def handle_add_task(task_list):
	task_data = ui.prompt_input_for_task()
	task_list = task_manager.add_task(task_data, task_list)
	return task_list

def update_task(task_list):
	selected_task = ui.select_task(task_list)
	field = ui.prompt_update_field()
	value = ui.prompt_update_value(field)
	selected_task.update_task_field(field, value)
	return task_list

def delete_task(task_list):
	task_to_delete = ui.prompt_delete_task(task_list)
	task_manager.delete_task(task_list, task_to_delete)
	return task_list

def search_tasks_by_name(task_list):
	found_tasks = ui.prompt_search(task_list)
	ui.display_found_tasks(found_tasks)
	return task_list

def stats(task_list):
	statistics = task_manager.stats(task_list)
	ui.display_stats(statistics)
	return task_list

def sort(task_list):
	sort_method = ui.method_to_sort_tasks()
	sorted_tasks = task_manager.sort_by(sort_method, task_list)
	ui.display_found_tasks(sorted_tasks)
	return task_list

def save(task_list):
	storage.save_json(task_list)
	return task_list

def load():
	return storage.load_json(ui.file_to_load())

def close_program():
	sys.exit()

COMMANDS = {
	"1": view_tasks,
	"2": handle_add_task,
	"3": update_task,
	"4": delete_task,
	"5": search_tasks_by_name,
	"6": stats,
	"7": sort,
	"8": save,
	"9": load,
	"10": close_program
}

if __name__ == "__main__":
	main()