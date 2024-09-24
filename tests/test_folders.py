from unittest import TestCase
from unittest.mock import MagicMock
from wrike.api import Wrike
from wrike.models import Folder, Result


class TestFolder(TestCase):
    def setUp(self) -> None:
        self.wrike = Wrike(page_size=3)
        self.wrike._rest_adapter = MagicMock()

    def test_get_folder_returns_one_folder(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "folders",
                "data": [
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    }
                ],
            },
        )
        folder = self.wrike.get_folder()
        self.assertIsInstance(folder, Folder)

    def test_get_folder_by_id_returns_one_folder(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "folders",
                "data": [
                    {
                        "id": "test",
                        "accountId": "",
                        "title": "test",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    }
                ],
            },
        )
        folder = self.wrike.get_folder_by_id("test")
        self.assertIsInstance(folder, Folder)

    def test_get_folders_returns_list_of_folder(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "folders",
                "data": [
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                ],
            },
        )
        folder_list = self.wrike.get_folders()
        self.assertIsInstance(folder_list, list)
        self.assertTrue(len(folder_list), 3)
        self.assertIsInstance(folder_list[0], Folder)

    def test_get_folder_and_filter_returns_one_folder(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "folders",
                "data": [
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test1",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test1",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                ],
            },
        )
        folder = self.wrike.get_folder_and_filter_to_one("test")
        self.assertIsInstance(folder, Folder)

    def test_get_folder_and_filter_with_one_filter(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "folders",
                "data": [
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test1",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                    {
                        "id": "",
                        "accountId": "",
                        "title": "test1",
                        "createdDate": "",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                ],
            },
        )
        folder = self.wrike.get_folder_and_filter(title="test")
        self.assertIsInstance(folder[0], Folder)
        self.assertEqual(folder[0].title, "test")

    def test_get_folder_and_filter_with_multiple_filters(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "folders",
                "data": [
                    {
                        "id": "",
                        "accountId": "a",
                        "title": "b",
                        "createdDate": "c",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                    {
                        "id": "",
                        "accountId": "b",
                        "title": "a",
                        "createdDate": "c",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                    {
                        "id": "",
                        "accountId": "c",
                        "title": "b",
                        "createdDate": "a",
                        "updatedDate": "",
                        "description": "",
                        "sharedIds": ["test"],
                        "parentIds": ["test"],
                        "childIds": [],
                        "superParentIds": [],
                        "scope": "test",
                        "hasAttachments": False,
                        "permalink": "test",
                        "workflowId": "test",
                        "metadata": [],
                        "customFields": [],
                    },
                ],
            },
        )
        folder = self.wrike.get_folder_and_filter(
            account_id="a", title="b", created_date="c"
        )
        self.assertIsInstance(folder[0], Folder)
        self.assertEqual(folder[0].account_id, "a")
        self.assertEqual(folder[0].title, "b")
        self.assertEqual(folder[0].created_date, "c")

    def test_get_folder_and_filter_raises_value_error(self):
        with self.assertRaises(ValueError):
            folder = self.wrike.get_folder_and_filter()
