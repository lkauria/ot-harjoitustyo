#from database_connection import get_database_connection
from entities.user import User


class UserRepository:

    def __init__(self):
        # testataan, että saadaan käyttäjä tähän tallennettua
        self._users = []

    def find_all(self):
        return self._users

    def create_user(self, user):
        # lisätään uusi käyttäjä listaan
        self._users.append(user)



#user_repository = UserRepository(get_database_connection())