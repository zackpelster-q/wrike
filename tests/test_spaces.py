from unittest import TestCase
from unittest.mock import MagicMock
from wrike.api import Wrike
from wrike.models import Space, Result


class TestSpace(TestCase):
    def setUp(self) -> None:
        self.wrike = Wrike(page_size=3)
        self.wrike._rest_adapter = MagicMock()

    def test_get_space_returns_one_space(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "spaces",
                "data": [
                    {
                        "id": "test",
                        "title": "test",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                ],
            },
        )
        space = self.wrike.get_space()
        self.assertIsInstance(space, Space)

    def test_get_space_by_id_returns_one_space(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "spaces",
                "data": [
                    {
                        "id": "test",
                        "title": "test",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                ],
            },
        )
        space = self.wrike.get_space_by_id("test")
        self.assertIsInstance(space, Space)

    def test_get_spaces_returns_list_of_space(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "spaces",
                "data": [
                    {
                        "id": "test",
                        "title": "test",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "test",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "test",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                ],
            },
        )
        space_list = self.wrike.get_spaces()
        self.assertIsInstance(space_list, list)
        self.assertTrue(len(space_list), 3)
        self.assertIsInstance(space_list[0], Space)

    def test_get_space_and_filter_returns_one_space(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "spaces",
                "data": [
                    {
                        "id": "test",
                        "title": "test",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                ],
            },
        )
        space = self.wrike.get_space_and_filter("test")
        self.assertIsInstance(space[0], Space)

    def test_get_space_and_filter_with_one_filter(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "spaces",
                "data": [
                    {
                        "id": "test",
                        "title": "test",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "test1",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "test2",
                        "avatarUrl": "test",
                        "accessType": "test",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                ],
            },
        )
        space = self.wrike.get_space_and_filter(title="test")
        self.assertIsInstance(space[0], Space)
        self.assertEqual(space[0].title, "test")

    def test_get_space_and_filter_with_multiple_filters(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "spaces",
                "data": [
                    {
                        "id": "test",
                        "title": "a",
                        "avatarUrl": "c",
                        "accessType": "b",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "a",
                        "avatarUrl": "b",
                        "accessType": "c",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "b",
                        "avatarUrl": "a",
                        "accessType": "c",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "b",
                        "avatarUrl": "c",
                        "accessType": "a",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "c",
                        "avatarUrl": "a",
                        "accessType": "b",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                    {
                        "id": "test",
                        "title": "c",
                        "avatarUrl": "b",
                        "accessType": "a",
                        "archived": False,
                        "guestRoleId": "test",
                        "defaultProjectWorkflowId": "test",
                        "defaultTaskWorkflowId": "test",
                    },
                ],
            },
        )
        space = self.wrike.get_space_and_filter(
            title="a", avatar_url="b", access_type="c"
        )
        self.assertIsInstance(space[0], Space)
        self.assertEqual(space[0].title, "a")
        self.assertEqual(space[0].avatar_url, "b")
        self.assertEqual(space[0].access_type, "c")

    def test_get_space_and_filter_raises_value_error(self):
        with self.assertRaises(ValueError):
            space = self.wrike.get_space_and_filter()
