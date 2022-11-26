#from entities.user import User
#from entities.transaction import Transaction

class TransactionService:
    def __init__(self, transaction_repository, user_repository):
        self._user = None
        self._transction_repository = transaction_repository
        self._user_repository = user_repository

#    def create_transaction(self, content):
#        transaction = Transaction(content=content, user=self._user)
#        return self._transction_repository.create(transaction)
