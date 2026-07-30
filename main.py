import sys
import task
import storage
import ui

def main():
    file = ui.file_to_load()
    task_list = storage.load_file(file)

    while True:
        choice = ui.display_menu()
        task_list = choices(choice, task_list)

def choices(user_input, task_list):
    match int(user_input):
        case 1:
            #sorted_tasks = sort_alphabetical(task_list)
            #sorted_tasks = sort_priority(task_list)
            sorted_tasks = task.sort_date(task_list)
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
            task_list = task.add_task(task_list, new_task)
        case 3:
            task_name = ui.prompt_task_name()

            field = ui.prompt_update_field()

            value = ui.prompt_update_value(field)

            selected_task = task.find_task(task_list, task_name)

            task.update_task_field(selected_task, field, value)
        case 4:
            task_name = ui.prompt_delete_task()
            task.delete_task(task_list, task_name)
        case 5: 
            search_term = ui.prompt_search()

            results = task.search(task_list, search_term)

            ui.display_tasks(results)
        case 6:
            statistics = task.stats(task_list)
            ui.display_stats(statistics)
        case 7:
            storage.save_file(task_list)
        case 8: 
            filename = ui.file_to_load()
            task_list = storage.load_file(filename)
        case 9:
            sys.exit()
        case _:
            ui.display_menu() 

    return task_list


if __name__ == "__main__":
    main()