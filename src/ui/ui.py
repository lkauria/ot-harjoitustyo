from ui.create_user_view import CreateUserView
from ui.login_view import LoginView
from services.user_service import user_service


class UI:
    def __init__(self, root):
        self._root = root
        # This view changes by the use and first it is set to None
        self._current_view = None
        
    # FIRST PAGE IS CREATE USER VIEW ATM
    def start(self):
        self._show_login_view()

    # DESTROY CURRENT VIEW BEFORE CREATING A NEW VIEW
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    # CREATE USER VIEW -> VIEW HAS A HANDLER FOR CREATING NEW USER
    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateUserView(
            self._root,
            self._handle_create_user
        )
        self._current_view.pack()

    # IF USER PUSHES THE BUTTON CREATE USER ON UI, _CREATE_USER METHOD IN CREATE USER VIEW SENDS HANDLING TO HERE
    def _handle_create_user(self, username, password): 
        user_service.create_user(username, password)

    # LOGIN VIEW
    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._handle_login,
            self._show_create_user_view
        )
        self._current_view.pack()

    # HANDLE LOGIN USER, NOT READY
    def _handle_login(self, username, password):
        user_service.login(username, password)
        print("login handler")