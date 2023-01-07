from tkinter import Button, Entry, Label, StringVar, Frame
import errors


class LoginView:
    """View for login to a personal user account
    
    Attributes: Tkinter window (root), login handler that redirects back to UI 
    and then service class and repository class. Those classes handle login for the user."""

    def __init__(self, root, handle_login, handle_show_create_user_view, handle_show_transaction_view):
        """Constructor for creating a view for login to user account, also a first page
        
        Args: Tkinter window (root), handler login user"""
        
        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_show_transaction_view = handle_show_transaction_view
        self._frame = None
        self.username = StringVar()
        self.password = StringVar()
        self._error_variable = None
        self._error_label = None

        self._show()

    def pack(self):
        if self._frame:
            self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()

    def _show(self):

        self._frame = Frame(
            master=self._root,
            padx=100,
            pady=100
        )

        self._error_variable = StringVar(self._frame)

        self._error_label = Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )



        label_login = Label(
            master=self._frame,
            text="Tervetuloa budjetointisovellukseen!"
        )

        button_login = Button(
            master=self._frame,
            text="Kirjaudu", 
            padx=50,
            pady=20, 
            command=self._login, 
            bg="#66CDAA"
        )

        button_create_user = Button(
            master=self._frame,
            text="Luo uusi tunnus", 
            padx=50,
            pady=20, 
            command=self._handle_show_create_user_view, 
            bg="#66CDAA"
        )

        label_username = Label(
            master=self._frame,
            text="käyttäjätunnus"
        )

        label_password = Label(
            master=self._frame,
            text="salasana"
        )

        label_new_account = Label(
            master=self._frame,
            text="Oletko uusi käyttäjä?"
        )

        self.entry_username = Entry(
            master=self._frame,
            width=25
        )

        self.entry_password = Entry(
            master=self._frame,
            width=25
        )


        self._error_label.grid(row=0, column=1, padx=5, pady=5)

        label_login.grid(row=1, column=1)
        label_username.grid(row=3, column=0)
        label_password.grid(row=4, column=0)

        self.entry_username.grid(row=3, column=1)
        self.entry_password.grid(row=4, column=1)

        button_login.grid(row=8, column=1)

        label_new_account.grid(row=9, column=1)
        button_create_user.grid(row=10, column=1)

        self._hide_error()


    def _login(self):
        try: 
            self._handle_login(self.entry_username.get(), self.entry_password.get())
            self._handle_show_transaction_view()
        except errors.InvalidCredentialError:
            self._show_error("Käyttäjätunnusta ei ole ja/tai salasana on väärä.")