from unittest import TestCase
from unittest.mock import MagicMock
from wrike.api import Wrike
from wrike.models import Contact, Result


class TestContacts(TestCase):
    def setUp(self) -> None:
        self.wrike = Wrike(page_size=3)
        self.wrike._rest_adapter = MagicMock()

    def test_get_contact_returns_one_contact(self):
        self.wrike._rest_adapter.get.return_value = Result(
            200,
            headers={},
            data={
                "kind": "contacts",
                "data": [
                    {
                        "id": "test",
                        "firstName": "test",
                        "lastName": "test",
                        "type": "test",
                        "profiles": [
                            {
                                "accountId": "test",
                                "email": "test",
                                "role": "test",
                                "external": False,
                                "admin": False,
                                "owner": False,
                            }
                        ],
                        "avatarUrl": "test",
                        "timezone": "test",
                        "locale": "test",
                        "deleted": False,
                        "me": True,
                        "title": "test",
                        "companyName": "test",
                        "phone": "test",
                        "location": "test",
                        "primaryEmail": "test",
                    }
                ],
            },
        )
        contact = self.wrike.get_me()
        self.assertIsInstance(contact, Contact)
