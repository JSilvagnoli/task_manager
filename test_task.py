import unittest

from task import Task
from datetime import datetime

class TestTask(unittest.TestCase):
    def test_task_creation_valid_data(self):
        task = Task(
            task_id=1,
            task_name = "Buy Milk",
            completion_status = False,
            priority = "High",
            category = "Groceries",
            due_date = datetime(2026,7,30)
        )

        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.task_name, "Buy Milk")
        self.assertFalse(task.completion_status)
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.category, "Groceries")
        self.assertEqual(task.due_date, datetime(2026,7,30))

    def test_task_creation_without_optional_values(self):
        task = Task(
            task_id = 20,
            task_name = "Study Python",
            completion_status = True,
            priority = "",
            category = "",
            due_date = None
        )

        self.assertEqual(task.task_id, 20)
        self.assertEqual(task.task_name, "Study Python")
        self.assertTrue(task.completion_status)
        self.assertEqual(task.priority, "")
        self.assertEqual(task.category, "")
        self.assertIsNone(task.due_date, None)

    def test_task_creation_blank_task_name(self): 
        with self.assertRaises(ValueError):
            Task(
                task_id = 1,
                task_name = "",
                completion_status = True,
                priority = "High",
                category = "Grocery",
                due_date = datetime(2000,1,1)
            )

    def test_task_creation_invalid_completion_status(self):
        with self.assertRaises(TypeError):
            Task(
                task_id = 1,
                task_name = "Call Mom",
                completion_status = "True",
                priority = "High",
                category = "Personal",
                due_date = datetime(2000,1,1)
            )

    def test_task_creation_invalid_priority(self):
        with self.assertRaises(ValueError):
           Task(
                task_id = 1,
                task_name = "Defeat Malenia",
                completion_status = False,
                priority = "Urgent",
                category = "Gaming",
                due_date = datetime(2000,1,1)
            )

    def test_task_creation_invalid_due_date(self):
        with self.assertRaises(TypeError):
           Task(
                task_id = 1,
                task_name = "Defeat Malenia",
                completion_status = False,
                priority = "Low",
                category = "Gaming",
                due_date = "2000/01/01"
            )

    def test_update_task_field(self):
        task = Task(
                task_id = 1,
                task_name = "Exercise",
                completion_status = False,
                priority = "Low",
                category = "Fitness",
                due_date = datetime(2000,1,1)
            )
        task.update_task_field("1", "Go To The Gym")
        self.assertEqual(task.task_name, "Go To The Gym")

    def test_update_field_invalid_value(self):
        task = Task(
                task_id = 1,
                task_name = "Exercise",
                completion_status = False,
                priority = "Low",
                category = "Fitness",
                due_date = datetime(2000,1,1)
            )
        with self.assertRaises(ValueError):
            task.update_task_field("1", "")
        self.assertEqual(task.task_name, "Exercise")

if __name__ == "__main__":
    unittest.main()