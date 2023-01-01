class Transaction:
    """ Transaction class includes the budget incomes and expenses.
    """
    def __init__(self, subject, amount, user_id):
        self.subject = subject
        self.amount = amount
        self.user_id = user_id
