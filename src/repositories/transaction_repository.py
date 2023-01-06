from database_connection import get_database_connection
from entities.user import User

class TransactionRepository():

    def __init__(self, connection):
        self._connection = connection

    def save_transaction(self, user_id, amount, subject):

        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO transactions (user_id, amount, subject) VALUES (?, ?, ?)",
            (user_id, amount, subject)
        )
        self._connection.commit()
    

    def find_all_transactions_of_user(self, username):
        
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM transactions WHERE user_id = ?",
            (username,)
        )
        rows = cursor.fetchall()
        
        return rows

transaction_repository = TransactionRepository(get_database_connection())