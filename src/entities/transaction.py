class Transaction:
    """ Transaction class includes the budget incomes and expenses.
    """
    def __init__(self, subject, amount, user_id):
        # user_id must come automatically from the user logged in -> to do
        self.subject = subject
        self.amount = amount
        self.user_id = user_id
