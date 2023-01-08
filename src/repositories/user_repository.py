from database_connection import get_database_connection
from entities.user import User


class UserRepository:
    """A class for managing database queries regarding users.
    """
    def __init__(self, connection):
        """A constructor for initializing a repository that controls database queries.

        Args:
            connection (class Connect): the repository class gets a database connection
            as an argument
        """
        self._connection = connection


    def find_all(self):
        """A method that fetch all the users from users database table.

        Returns:
            user (list of User objects): here all the users from users table are returned.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]


    def find_user(self, username):
        """A method for finding a particular user from a database table users

        Args:
            username (str): username of a user

        Returns:
            user (class User): if a user is found returns a user object. Otherwise returns None.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return [User(row["username"], row["password"]) if row else None]

    def create_user(self, user):
        """A method that inserts a new user to a database table users.

        Args:
            user (class User): a new user to be saved to table users.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()



user_repository = UserRepository(get_database_connection())
