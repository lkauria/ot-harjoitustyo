from database_connection import get_database_connection
from entities.user import User

class TransactionRepository():

    def __init__(self, connection):
        self._connection = connection

    # logic for saving transaction to database