from ui.create_user_view import CreateUserView
from services.user_service import user_service
# from ui.login_view import LoginView
# from ui.transaction_view import TransactionView


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None
        
    # FIRST PAGE IS LOGIN
    def start(self):
        self._show_create_user_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None


    # CREATE USER
    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateUserView(
            self._root,
            self._handle_create_user,
        )
        self._current_view.pack()

    def _handle_create_user(self, username, password):
        user_service.create_user(username, password)
        print(user_service.list_all_users())


    '''
    # LOGIN
    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root, 
            self.
            self._show_login_view
        )
        self._current_view.pack()


    # TRANSACTIONS
    def _show_transaction_view(self):
        self._hide_current_view()
        self._current_view = TransactionView(
            self._root,
            self._show_transaction_view
        )
        self._current_view.pack()
    '''