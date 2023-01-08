import unittest
from services.transaction_service import TransactionService
from errors import EmptyFieldError

class TestTransactionService(unittest.TestCase):

    def setUp(self):
        self.transaction_service = TransactionService()

    def test_save_transaction(self):
        self.transaction_service.save_transaction("user3", 300, "wood")

    def test_create_user_but_a_field_is_empty(self):
        self.assertRaises(EmptyFieldError, self.transaction_service.save_transaction, "user3", "", "tiles")

    def test_find_transactions_that_are_submit(self):
        self.transaction_service.save_transaction("user3", 300, "wood")
        self.transaction_service.save_transaction("user3", 400, "tiles")
        transactions = self.transaction_service.get_transactions("user3")
        self.assertEqual(len(transactions), 2)



        

