from database_connection import get_database_connection
from entities.user import User

class TransactionRepository():

    def __init__(self, connection):
        self._connection = connection

    def save_transaction(self, user_id, amount, subject):
        print("Transaction Repository, start saving")

        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO transactions (user_id, amount, subject) VALUES (?, ?, ?)",
            (user_id, amount, subject)
        )
        self._connection.commit()
        print("repository: saving transaction ok!")
    
    

transaction_repository = TransactionRepository(get_database_connection())