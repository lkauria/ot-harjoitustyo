from repositories.transaction_repository import transaction_repository
import errors

class TransactionService:
    """This transaction service is resposible for application logic regarding Transaction class
    and methods for users transactions.
    """
    def __init__(self):
        """This constructor creates a new transaction service.
        """
        self._user = None
        self._transaction_repository = transaction_repository

    def save_transaction(self, username, amount, subject):
        """_summary_

        Args:
            username (str): username that is logged in while adding the transaction
            amount (int): the amount of the transaction
            subject (str): the subject of the transaction

        Raises:
            errors.EmptyFieldError: neither of the fields should not be empty or error message
        """
        if amount == "" or subject == "":
            raise errors.EmptyFieldError("Kenttä tyhjänä")
        self._transaction_repository.save_transaction(username, amount, subject)

    def get_transactions(self, username):
        """Fetch transactions from the database table transactions for one user.

        Args:
            username (str): This is needed to get transactions for a specific user.

        Returns:
            transactions (class Transaction): returns transactions of a one user
        """
        transactions = self._transaction_repository.find_all_transactions_of_user(username)
        return transactions

transaction_service = TransactionService()
