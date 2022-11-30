from ui.create_user_view import CreateUserView
from services.user_service import user_service


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        
    # FIRST PAGE IS LOGIN
    def start(self):
        self._show_create_user_view()

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
            self._handle_create_user,
        )
        self._current_view.pack()

    # IF USER PUSHES THE BUTTON CREATE USER ON UI, _CREATE_USER METHOD IN CREATE USER VIEW SENDS HANDLING TO HERE
    def _handle_create_user(self, username, password):
        user_service.create_user(username, password)
        print("INSIDE HANDLER ", user_service.list_all_users())
