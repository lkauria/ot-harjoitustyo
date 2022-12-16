from ui.create_user_view import CreateUserView
from ui.login_view import LoginView
from services.user_service import user_service


class UI:
    """Class that has initiative to create views
    
    Attribute: empty Tkinter window"""


    def __init__(self, root):
        """Constructor for a view
        
        Args: Tkinter window"""

        self._root = root
        self._current_view = None
        

    def start(self):
        """Start redirects Tkinter window to render login view on it"""

        self._show_login_view()



    def _hide_current_view(self):
        """Before creating a new view the old view must be destroyd"""

        if self._current_view:
            self._current_view.destroy()
        self._current_view = None



    def _show_create_user_view(self):
        """This redirects to create an object of a class Create user view where new user 
        creates an account.
        
        Result: A create user view is shown"""

        self._hide_current_view()
        self._current_view = CreateUserView(
            self._root,
            self._handle_create_user
        )
        self._current_view.pack()


    def _show_login_view(self):
        """This redirects to create an object of a class Login view where user can login 
        and new user can decide to create an account.
        
        Result: A login view is shown"""
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._handle_login,
            self._show_create_user_view
        )
        self._current_view.pack()



    def _handle_create_user(self, username, password):
        """If user pushes the button to create a new user account, this method redirects the 
        creation the user to User service class
        
        Args: username and password to create an account""" 

        user_service.create_user(username, password)


    def _handle_login(self, username, password):
        """If user pushes the button to login to user account, this method redirects to 
        checking if the user account exists with given arguments and logs in if so.
        
        Args: username and password to create an account""" 
       
        print("_handle_login ui.py: ", )
        user_service.login(username, password)
