import unittest
from services.user_service import UserService
from errors import UsernameExistsError

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        user_service = UserService()
        user_service.create_user("user3", "passw1")
        for user in user_service.list_all_users():
            self.assertEqual(user.get_username(), "user3")

    def test_create_user_but_exists_already(self):
        user_service = UserService()
        user_service.create_user("user4", "passw1")
        self.assertRaises(UsernameExistsError, user_service.create_user, "user4", "passw1")

