from entities.user import User
from entities.transaction import Transaction

class UserService:
    def __init__(self, transaction_repository, user_repository):
        self._user = None
        self._transction_repository = transaction_repository
        self._user_repository = user_repository

    
