from entities.user import User
from repositories.transaction_repository import transaction_repository
import errors

class TransactionService:
    
    def __init__(self):

        self._user = None
        self._transaction_repository = transaction_repository

    def save_transaction(self, username, amount, subject):
        print("Check, if empty or amount not integer, to do")
        if amount == "" or subject == "":
            raise errors.EmptyFieldError("Kenttä tyhjänä")
        self._transaction_repository.save_transaction(username, amount, subject)

    def get_transactions(self, username):
        transactions = self._transaction_repository.find_all_transactions_of_user(username)
        return transactions

transaction_service = TransactionService()