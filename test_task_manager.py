import unittest
from datetime import datetime

from task import Task
import task_manager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_list = [
            Task(
                task_id=1,
                task_name="Buy Milk",
                completion_status=True,
                priority="Low",
                category="Test",
                due_date=datetime(2000,3,9)
            ),
            Task(
                task_id=2,
                task_name="Study Python",
                completion_status=False,
                priority="High",
                category="Test",
                due_date=datetime.min
            ),
            Task(
                task_id=3,
                task_name="Clean House",
                completion_status=False,
                priority="",
                category="Test",
                due_date=datetime(2593,11,23)
            ),
            Task(
                task_id=4,
                task_name="Exercise",
                completion_status=False,
                priority="Medium",
                category="Test",
                due_date=datetime(1992,2,10)
            )
        ]
    
    def test_add_task(self):
        task_data = {
            "task_name": "Test 5",
            "completion_status": False,
            "priority": "Low",
            "category": "Test",
            "due_date": datetime(2000,1,1)
        }

        task_manager.add_task(task_data, self.task_list)
        added_task = self.task_list[-1]

        self.assertEqual(added_task.task_id, 5)
        self.assertEqual(added_task.task_name, "Test 5")
        self.assertFalse(added_task.completion_status)
        self.assertEqual(added_task.priority, "Low")
        self.assertEqual(added_task.category, "Test")
        self.assertEqual(added_task.due_date, datetime(2000,1,1))

    def test_next_available_id_empty_list(self):
        task_list = []
        next_available_id = task_manager.next_available_id(task_list)

        self.assertEqual(next_available_id, 1)
    
    def test_next_available_id(self):
        next_available_id = task_manager.next_available_id(self.task_list)

        self.assertEqual(next_available_id, 5)

    def test_delete_task(self):
        task_to_delete = self.task_list[2]
        task_manager.delete_task(self.task_list, task_to_delete)

        self.assertEqual(len(self.task_list), 3)
        self.assertNotIn(task_to_delete, self.task_list)

    def test_delete_task_not_found(self):
        task_to_delete = Task(
                task_id=10000,
                task_name="Test 10000",
                completion_status=False,
                priority="Low",
                category="Test",
                due_date=datetime(2000,1,1)
            )

        with self.assertRaises(ValueError):
            task_manager.delete_task(self.task_list, task_to_delete)
        self.assertEqual(len(self.task_list), 4)
    
    def test_find_task_by_exact_name(self):
        task_to_find = Task(
                task_id=2,
                task_name="Study Python",
                completion_status=False,
                priority="High",
                category="Test",
                due_date=datetime.min
            )
        found_task = task_manager.find_task_by_exact_name(self.task_list, "Study Python")
        self.assertEqual(found_task, task_to_find)

    def test_find_task_by_exact_name_not_found(self):
        found_task = task_manager.find_task_by_exact_name(
            self.task_list,
            "Does Not Exist"
        )

        self.assertIsNone(found_task)

    def test_find_tasks_by_partial_name(self):
        tasks_to_find = "o"
        found_tasks = task_manager.find_tasks_by_partial_name(self.task_list, tasks_to_find)
        found_names = [task.task_name for task in found_tasks]

        self.assertEqual(found_names, ["Study Python", "Clean House"])

    def test_find_tasks_by_partial_name_case_insensitive(self):
        tasks_to_find = "PYTHON"
        found_tasks = task_manager.find_tasks_by_partial_name(self.task_list, tasks_to_find)
        found_names = [task.task_name for task in found_tasks]

        self.assertEqual(found_names, ["Study Python"])

    def test_find_tasks_by_partial_name_no_results(self):
        tasks_to_find = "Nonsense"
        found_tasks = task_manager.find_tasks_by_partial_name(self.task_list, tasks_to_find)
        found_names = [task.task_name for task in found_tasks]

        self.assertEqual(found_names, [])

    def test_stats(self):
        stats = task_manager.stats(self.task_list)

        self.assertEqual(stats["total"], 4)
        self.assertEqual(stats["complete"], 1)
        self.assertEqual(stats["incomplete"], 3)
        self.assertAlmostEqual(stats["percentage"], 25.00, places=2)

    def test_stats_empty_list(self):
        stats = task_manager.stats([])

        self.assertEqual(stats["total"], 0)
        self.assertEqual(stats["complete"], 0)
        self.assertEqual(stats["incomplete"], 0)
        self.assertEqual(stats["percentage"], 0)

    def test_sort_alphabetically(self):
        sorted_list = task_manager.sort_alphabetical(self.task_list)
        sorted_names = [task.task_name for task in sorted_list]

        self.assertEqual(
            sorted_names,
            [
                "Buy Milk",
                "Clean House",
                "Exercise",
                "Study Python",
            ]
        )

    def test_sort_by_priority(self):
        sorted_list = task_manager.sort_priority(self.task_list)
        sorted_priorities = [task.priority for task in sorted_list]

        self.assertEqual(
            sorted_priorities,
            [
                "High",
                "Medium",
                "Low",
                ""
            ]
        )

    def test_sort_by_due_date(self):
        sorted_list = task_manager.sort_date(self.task_list)
        sorted_due_dates = [task.due_date for task in sorted_list]

        self.assertEqual(
            sorted_due_dates,
            [
                datetime(2593,11,23),
                datetime(2000,3,9),
                datetime(1992,2,10),
                datetime.min
            ]
        )