import unittest
from datetime import datetime
import storage
import json

from task import Task

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.task_list = [
            Task(
                task_id=1,
                task_name="Buy Milk",
                completion_status=True,
                priority="Low",
                category="Test",
                due_date=datetime(2000,1,1)
            )
        ]

    def test_convert_to_dict(self):
        expected_result = {
            "task_id": 1, 
            "task_name": "Buy Milk", 
            "completion_status": True, 
            "priority": "Low", 
            "category": "Test", 
            "due_date": "2000/01/01"
        }
        result = storage.convert_to_dict(self.task_list[0])

        self.assertEqual(result, expected_result)

    def test_convert_from_dict(self):
        dict_to_convert = [{"task_id": 1, "task_name": "Buy Milk", "completion_status": True, "priority": "Low", "category": "Test", "due_date": "2000/01/01"}]
        result = storage.convert_from_dict(dict_to_convert)

        self.assertEqual(result[0], self.task_list[0])
        self.assertIsInstance(result[0], Task)
        
