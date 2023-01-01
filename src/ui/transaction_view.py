class TransactionView:

    """ Transaction view show the budget's incomes and expenses.
    """

    def __init__(self, root, user):
        self._root = root
        self._user = user
        print("Transaction view")

        print("logged in as: ", self._user.username)
