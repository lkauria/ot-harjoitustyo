import unittest
from services.user_service import UserService
from entities.user import User

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        user = User("user1", "passw1")



