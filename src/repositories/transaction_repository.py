from database_connection import get_database_connection
from entities.user import User

class TransactionRepository():

    def __init__(self, connection):
        self._connection = connection

    def save_transaction(self, username, amount, subject):
        print("Transaction Repository, start saving")
        pass

transaction_repository = TransactionRepository(get_database_connection())