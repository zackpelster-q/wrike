from unittest import TestCase
from unittest.mock import MagicMock
from wrike.api import Wrike
from wrike.models import Task, Result


class TestWrike(TestCase):
    def setUp(self) -> None:
        self.wrike = Wrike(page_size=3)
        self.wrike._rest_adapter = MagicMock()

    def test_get_task_returns_one_task(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "tasks",
                "data": [
                    {
                        "id": 1,
                        "title": "test",
                        "status": "test",
                        "importance": "test",
                        "dates": "test",
                        "scope": "test",
                        "permalink": "test",
                        "priority": "test",
                    }
                ],
            },
        )
        task = self.wrike.get_task()
        self.assertIsInstance(task, Task)

    def test_get_tasks_returns_list_of_task(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "tasks",
                "data": [
                    {
                        "id": 1,
                        "title": "test",
                        "status": "test",
                        "importance": "test",
                        "dates": "test",
                        "scope": "test",
                        "permalink": "test",
                        "priority": "test",
                    },
                    {
                        "id": 2,
                        "title": "test",
                        "status": "test",
                        "importance": "test",
                        "dates": "test",
                        "scope": "test",
                        "permalink": "test",
                        "priority": "test",
                    },
                    {
                        "id": 3,
                        "title": "test",
                        "status": "test",
                        "importance": "test",
                        "dates": "test",
                        "scope": "test",
                        "permalink": "test",
                        "priority": "test",
                    },
                ],
            },
        )
        task_list = self.wrike.get_tasks()
        self.assertIsInstance(task_list, list)
        self.assertTrue(len(task_list), 3)
        self.assertIsInstance(task_list[0], Task)

    # TODO: What happens when you get to the last page of a paged Wrike call?
    def test_get_tasks_paged_returns_iterator_of_task(self):
        self.wrike._rest_adapter.get.side_effect = [
            Result(
                200,
                headers={},
                data={
                    "kind": "tasks",
                    "nextPageToken": "test",
                    "responseSize": 1,
                    "data": [
                        {
                            "id": 1,
                            "title": "test",
                            "status": "test",
                            "importance": "test",
                            "dates": "test",
                            "scope": "test",
                            "permalink": "test",
                            "priority": "test",
                        },
                        {
                            "id": 2,
                            "title": "test",
                            "status": "test",
                            "importance": "test",
                            "dates": "test",
                            "scope": "test",
                            "permalink": "test",
                            "priority": "test",
                        },
                        {
                            "id": 3,
                            "title": "test",
                            "status": "test",
                            "importance": "test",
                            "dates": "test",
                            "scope": "test",
                            "permalink": "test",
                            "priority": "test",
                        },
                    ],
                },
            ),
            Result(
                200,
                headers={},
                data={
                    "kind": "tasks",
                    "nextPageToken": "test",
                    "data": [],
                },
            ),
        ]
        task_iterator = self.wrike.get_tasks_paged()
        task1 = next(task_iterator)
        task2 = next(task_iterator)
        task3 = next(task_iterator)
        self.assertIsInstance(task3, Task)
        with self.assertRaises(StopIteration):
            task4 = next(task_iterator)
