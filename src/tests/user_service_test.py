import unittest
from services.user_service import UserService
from errors import UsernameExistsError, InvalidCredentialError

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()

    def test_create_user(self):
        self.user_service.create_user("user3", "passw1")
        for user in self.user_service.list_all_users():
            self.assertEqual(user.get_username(), "user3")
            self.assertEqual(user.get_password(), "passw1")

    def test_create_user_but_username_exists(self):
        self.user_service.create_user("user4", "passw1")
        self.assertRaises(UsernameExistsError, self.user_service.create_user, "user4", "passw1")

    def test_login(self):
        self.user_service.login("user3", "passw1")

    def test_login_invalid_username(self):
        self.assertRaises(InvalidCredentialError, self.user_service.login, "user5", "passw1")

    def test_login_invalid_password(self):
        self.assertRaises(InvalidCredentialError, self.user_service.login, "user4", "passw5")
