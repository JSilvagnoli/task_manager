import unittest

from task import create_task


class TestCreateTask(unittest.TestCase):

    def test_create_task(self):

        task = create_task(
            "Buy Milk",
            False,
            "High",
            "Groceries",
            "2026/07/30"
        )

        self.assertEqual(task["task"], "Buy Milk")
        self.assertFalse(task["completed"])
        self.assertEqual(task["priority"], "High")
        self.assertEqual(task["category"], "Groceries")
        self.assertEqual(task["due_date"], "2026/07/30")


if __name__ == "__main__":
    unittest.main()