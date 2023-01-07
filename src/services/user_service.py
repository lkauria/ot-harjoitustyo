from entities.user import User
from repositories.user_repository import user_repository
import errors

class UserService:

    def __init__(self):

        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password):

        user_exists = self._user_repository.find_user(username)
        if user_exists != [None]:
            raise errors.UsernameExistsError(f"Käyttäjätunnus {username} on jo käytössä.")
        self._user_repository.create_user(User(username, password))
        user = User(username, password)
        self._user = user

        return user

    def login(self, username, password):

        user_exists = self._user_repository.find_user(username)
        if user_exists == [None] or user_exists[0].password != password:
            raise errors.InvalidCredentialError(f"Käyttäjätunnusta {username} ei ole ja/tai salasana on väärä.")
        
        user = User(username, password)
        self._user = user

        return user

    def list_all_users(self):
        return self._user_repository.find_all()



user_service = UserService()
