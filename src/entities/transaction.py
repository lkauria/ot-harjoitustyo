class Transaction:
    """ Transaction class includes the budget incomes and expenses.
    """
    def __init__(self, subject, amount, username):
        self.subject = subject
        self.amount = amount
        self.username = username


    def get_amount(self):
        return self.amount