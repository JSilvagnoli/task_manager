from datetime import datetime

import task_manager

class Task:
    TASK_FIELDS = {
        "1": "task_name",
        "2": "completion_status",
        "3": "priority",
        "4": "category",
        "5": "due_date"
    }

    def __init__(self, task_id, task_name, completion_status = False, priority = None, category = None, due_date = None):
        self.task_id = task_id
        self.task_name = task_name
        self.completion_status = completion_status
        self.priority = priority
        self.category = category
        self.due_date = due_date

    def validate_task(self):
        for value in Task.FIELD_VALIDATION:
            Task.FIELD_VALIDATION[value](getattr(self, value))

    def validate_task_name_not_empty(value):
        if not value.strip():
            raise ValueError("Task name cannot be blank.")

    def validate_task_completion(value):
        if not isinstance(value, bool):
            raise TypeError("Completion status must be True or False.")

    def validate_task_priority(value):
        if value is None:
            return
    
        if value not in ("High", "Medium", "Low"):
            raise ValueError("Priority must be either Low, Medium, or High")

    def validate_task_category(value):
        if value is None:
            return
    
        if not value.strip():
            raise ValueError("Category cannot be blank")

    def validate_task_due_date(value):
        if not value.strip():
            raise ValueError("Due date cannot be blank.")
    
        try:
            datetime.strptime(value, "%Y/%m/%d")
        except ValueError:
            raise ValueError("Invalid date format. Please use (YYYY/MM/DD) format.")

    def update_task_field(self, field_to_update, value_to_update):
        chosen_field = Task.TASK_FIELDS[field_to_update]
        Task.FIELD_VALIDATION[chosen_field](value_to_update)
        setattr(self, chosen_field, value_to_update)

    FIELD_VALIDATION = {
        "task_name": validate_task_name_not_empty,
        "completion_status": validate_task_completion,
        "priority": validate_task_priority,
        "category": validate_task_category,
        "due_date": validate_task_due_date
    }
            
    def task_info(self):
        return(
            f"ID: {self.task_id} | "
            f"Task Name: {self.task_name} | "
            f"Completed: {self.completion_status} | "
            f"Priority: {self.priority} | "
            f"Category: {self.category} | "
            f"Due Date: {self.due_date} "
            )