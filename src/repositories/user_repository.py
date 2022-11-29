from database_connection import get_database_connection
from entities.user import User


class UserRepository:

    def __init__(self, connection):

        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def create_user(self, user):
        # add new user to database
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )
        self._connection.commit()
        
user_repository = UserRepository(get_database_connection())