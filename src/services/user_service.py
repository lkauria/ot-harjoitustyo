from entities.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self._user = None
        # luodaan user repository -olio
        self._user_repository = UserRepository()

    def create_user(self, username, password):
        user = User(username, password)
        self._user_repository.create_user(user)

    def list_all_users(self):
        return self._user_repository.find_all()

user_service = UserService()