import unittest
from services.user_service import UserService
from errors import UsernameExistsError, InvalidUsernameError, InvalidPasswordError

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        user_service = UserService()
        user_service.create_user("user3", "passw1")
        for user in user_service.list_all_users():
            self.assertEqual(user.get_username(), "user3")

    def test_create_user_but_username_exists(self):
        user_service = UserService()
        user_service.create_user("user4", "passw1")
        self.assertRaises(UsernameExistsError, user_service.create_user, "user4", "passw1")

    def test_login(self):
        user_service = UserService()
        user_service.login("user4", "passw1")

    def test_login_invalid_username(self):
        user_service = UserService()
        self.assertRaises(InvalidUsernameError, user_service.login, "user5", "passw1")

    def test_login_invalid_password(self):
        user_service = UserService()
        self.assertRaises(InvalidPasswordError, user_service.login, "user4", "passw5")

