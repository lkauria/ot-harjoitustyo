from entities.user import User
from repositories.user_repository import user_repository
import errors

class UserService:
    
    def __init__(self):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password, login=True):

        user_exists = self._user_repository.find_user(username)
        if user_exists != [None]:
            raise errors.UsernameExistsError(f"Käyttäjätunnus {username} on jo käytössä.")
        user = self._user_repository.create_user(User(username, password))
        if login:
            self._user = user
        return user

    def login(self, username, password):
        user = User(username, password)
        self._user_repository.login(user)
        if not user or user.password != password:
            raise errors.InvalidCredentialsError("Käyttäjätunnusta ei ole tai salasana oli väärä.")
        self._user = user
        
        return user

    def list_all_users(self):
        return self._user_repository.find_all()

    


user_service = UserService()
