from database_connection import get_database_connection

class TransactionRepository():
    """A class for managing database queries regarding transactions.
    """
    def __init__(self, connection):
        """A constructor for initializing a repository that controls database queries.

        Args:
            connection (class Connect): the repository class gets a database connection
            as an argument
        """
        self._connection = connection

    def save_transaction(self, user_id, amount, subject):
        """A method that saves a new transaction to the table for a particular user.

        Args:
            user_id (str): unique username
            amount (int): transaction's amount
            subject (str): transaction's subject
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO transactions (user_id, amount, subject) VALUES (?, ?, ?)",
            (user_id, amount, subject)
        )
        self._connection.commit()

    def find_all_transactions_of_user(self, username):
        """A method for finding all transactins for a specific user.

        Args:
            username (str): A username that transactions are listed for

        Returns:
            transactions (list of Transaction objects): A list for transaction objects for a
            specific user.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM transactions WHERE user_id = ?",
            (username,)
        )
        rows = cursor.fetchall()
        return rows

transaction_repository = TransactionRepository(get_database_connection())
