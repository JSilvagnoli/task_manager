from datetime import datetime

class Task:
    TASK_FIELDS = {
        "1": "task_name",
        "2": "completion_status",
        "3": "priority",
        "4": "category",
        "5": "due_date"
    }

    def __init__(self, task_id, task_name, completion_status, priority, category, due_date):
        self.task_id = task_id
        self.task_name = task_name
        self.completion_status = completion_status
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.validate_task()

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return (
            self.task_id == other.task_id and 
            self.task_name == other.task_name and
            self.completion_status == other.completion_status and 
            self.priority == other.priority and
            self.category == other.category and
            self.due_date == other.due_date
        )

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
        if value not in ("Low", "Medium", "High", ""):
            raise ValueError("Priority must be either Low, Medium, High, or leave it blank for no priority.")

    def validate_task_category(value):
        if value == "":
            return
        
        if not isinstance(value, str):
            raise TypeError("Category must be either a string or blank.")

    def validate_task_due_date(value):
        if value is None:
            return
    
        if not isinstance(value, datetime):
            raise TypeError("Due date must be a datetime object or None.")

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