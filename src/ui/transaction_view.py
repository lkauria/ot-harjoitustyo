class TransactionView:

    # create log of button, table and sum for transactions

    def __init__(self, root, user):
        self._root = root
        self._user = user
        print("Transaction view")

        # The user comes in as an attribute
        print("logged in as: ", self._user.username)
