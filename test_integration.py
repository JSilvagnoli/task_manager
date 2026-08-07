import os
import unittest
import json
from datetime import datetime

from task import Task
import storage
import task_manager

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.task_list = [
            Task(
                task_id=1,
                task_name="Buy Milk",
                completion_status=True,
                priority="High",
                category="Grocery",
                due_date=datetime(2000,1,1)
            ),
            Task(
                task_id=2,
                task_name="Wash Car",
                completion_status=False,
                priority="Medium",
                category="Personal",
                due_date=datetime(2050,5,15)
            )
        ]

    # Create → Update → Save → Load → Verify
    def test_task_add_update_save_load_flow_from_scratch(self):
        task_list = []
        task_data = {
            "task_name": "Study",
            "completion_status": True,
            "priority": "",
            "category": "",
            "due_date": None
        }

        field_to_update = "1"
        value_to_update = "Study Python"
        file_name = "test_data.json"

        expected_result = [
            Task(
                task_id=1,
                task_name="Study Python",
                completion_status=True,
                priority="",
                category="",
                due_date=None
            )
        ]

        try:
            task_manager.add_task(task_data, task_list)
            Task.update_task_field(task_list[0], field_to_update, value_to_update)

            storage.save_json(task_list, file_name)
            reverted_data = storage.load_json(file_name)

            self.assertEqual(reverted_data, expected_result)

        finally:
            if os.path.exists(file_name):
                os.remove(file_name)

    # Load → Delete → Save → Load → Verify
    def test_task_load_delete_save_load_flow_from_file(self):
        file_name = "test_data.json"

        expected_result = [
            Task(
                task_id=2,
                task_name="Wash Car",
                completion_status=False,
                priority="Medium",
                category="Personal",
                due_date=datetime(2050,5,15)
            )
        ]

        try:
            storage.save_json(self.task_list, file_name)
            reverted_data = storage.load_json(file_name)

            task_manager.delete_task(self.task_list, self.task_list[0])
            storage.save_json(self.task_list, file_name)
            reverted_data = storage.load_json(file_name)

            self.assertEqual(reverted_data, expected_result)
        finally:
            if os.path.exists(file_name):
                os.remove(file_name)
