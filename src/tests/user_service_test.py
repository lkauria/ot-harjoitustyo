import unittest
from services.user_service import UserService
from repositories.user_repository import UserRepository
from entities.user import User

class TestUserService(unittest.TestCase):

    def test_create_user(self):
        user_service = UserService()
        user_service.create_user("usern3", "passw1")
        for user in user_service.list_all_users():
            if user.get_username() == "user3":
                pass

    
