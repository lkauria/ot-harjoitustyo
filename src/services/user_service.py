from entities.user import User
from repositories.user_repository import user_repository
import errors

class UserService:
    """This user service is resposible for application logic regarding User class
    and methods for a user.
    """
    def __init__(self):
        """This constructor creates a new user service.
        """
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password):
        """A method that creates a new user with username and password given as arguments.

        Args:
            username (str): username given as entry on the create_user_view.py
            password (str): password given as entry on the create_user_view.py

        Raises:
            errors.UsernameExistsError: If username exists, it cannot be created
            again, error message sent

        Returns:
            user (class User): returns the user that has just been created.
        """

        user_exists = self._user_repository.find_user(username)
        if user_exists != [None]:
            raise errors.UsernameExistsError(f"Käyttäjätunnus {username} on jo käytössä.")
        self._user_repository.create_user(User(username, password))
        user = User(username, password)
        self._user = user

        return user

    def login(self, username, password):
        """A method that tries login with a username and a password given.

        Args:
            username (str): username given as entry on the login_view.py
            password (str): password given as entry on the login_view.py

        Raises:
            errors.InvalidCredentialError: username or/and password is not valid, error message

        Returns:
            user (class User): returns the user that just logged in.
        """

        user_exists = self._user_repository.find_user(username)
        if user_exists == [None] or user_exists[0].password != password:
            raise errors.InvalidCredentialError(f"Tunnusta {username} ei ole tai salasana on väärä")

        user = User(username, password)
        self._user = user

        return user

    def list_all_users(self):
        """A method that lists all the users in the database table "users".

        Returns:
            users (list with User objects): returns a list with User objects.
        """
        return self._user_repository.find_all()



user_service = UserService()
