import sys
import task
import storage
import ui

def main():
    task_list = storage.load_file(ui.file_to_load())

    while True:
        task_list = choices(ui.display_menu(), task_list)

def choices(user_input, task_list):
    match int(user_input):
        case 1:
            ui.display_tasks(task_list)
        case 2:
            task_data = ui.prompt_input_for_task()

            new_task = task.create_task(
                task_data["task"],
                task_data["completed"],
                task_data["priority"],
                task_data["category"],
                task_data["due_date"]
            )
            return task.add_task(task_list, new_task)
        case 3:
            task_name = ui.prompt_task_name(task_list)

            field = ui.prompt_update_field()

            value = ui.prompt_update_value(field)

            selected_task = task.find_task_by_name(task_list, task_name)

            task.update_task_field(selected_task, field, value)
        case 4:
            task.delete_task(task_list, ui.prompt_delete_task(task_list))
        case 5: 
            ui.display_tasks(task.search(task_list, ui.prompt_search(task_list)))
        case 6:
            statistics = task.stats(task_list)
            ui.display_stats(statistics)
        case 7:
            sort_method = ui.method_to_sort_tasks()
            return task.sort_by(sort_method, task_list)
        case 8:
            storage.save_file(task_list)
        case 9: 
            filename = ui.file_to_load()
            return storage.load_file(filename)
        case 10:
            sys.exit()
        case _:
            ui.display_menu() 

    return task_list


if __name__ == "__main__":
    main()