from entities.user import User
from repositories.transaction_repository import transaction_repository
import errors

class TransactionService:
    
    def __init__(self):

        self._user = None
        self._transaction_repository = transaction_repository

    def save_transaction(self, username, amount, subject):
        pass

transaction_service = TransactionService()