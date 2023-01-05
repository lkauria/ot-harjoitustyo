from entities.user import User
from repositories.transaction_repository import transaction_repository
import errors

class TransactionService:
    
    def __init__(self):

        self._user = None
        self._transaction_repository = transaction_repository

    def save_transaction(self, username, amount, subject):
        print("username ", username, ", amount ", amount, ", subject ", subject)
        if amount == "" or subject == "":
            raise errors.EmptyFieldError("Kenttä tyhjänä")
        self._transaction_repository.save_transaction(username, amount, subject)

transaction_service = TransactionService()