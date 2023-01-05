class Transaction:
    """ Transaction class includes the budget incomes and expenses.
    """
    def __init__(self, subject, amount, username):
        # user_id must come automatically from the user logged in -> to do
        self.subject = subject
        self.amount = amount
        self.username = username
