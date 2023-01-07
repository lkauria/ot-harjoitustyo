from tkinter import Button, Entry, Label, StringVar, Frame
import errors


class CreateUserView:
    """View for creating a new user account
    
    Attributes: Tkinter window (root), create user handler that redirects back to UI 
    and then service class and repository class. Those classes handle creating the new user."""


    def __init__(self, root, handle_create_user, handle_show_create_user_view, handle_show_transaction_view):
        """Constructor for creating a view for creating a new user account
        
        Args: Tkinter window (root), handler for creating a new user"""

        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_show_transaction_view = handle_show_transaction_view

        self._frame = None
        self.username = StringVar()
        self.password = StringVar()

        self._error_variable = None
        self._error_label = None

        self._show()

    
    def pack(self):
        """A method for packing/rendering Tkinter window widgets on a frame"""

        if self._frame:
            self._frame.pack()

    def destroy(self):
        """A method for destroying frame and its widgets before creating a new view."""

        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()

    def _show(self):
        """Show method defines all the widgets inside the view"""

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

        label_create_user = Label(
            master=self._frame,
            text="Luo käyttäjätunnus"
        )

        label_username = Label(
            master=self._frame,
            text="käyttäjätunnus"
        )

        label_password = Label(
            master=self._frame,
            text="salasana"
        )

        self.entry_username = Entry(
            master=self._frame,
            width=25
        )

        self.entry_password = Entry(
            master=self._frame,
            width=25
        )

        button_create_user = Button(
            master=self._frame,
            text="Luo tunnus", 
            padx=50,
            pady=20, 
            command=self._create_user, 
            bg="#66CDAA"
        )

        button_login = Button(
            master=self._frame,
            text="Minulla on jo tunnus", 
            padx=50,
            pady=20, 
            command=self._handle_show_create_user_view, 
            bg="#66CDAA"
        )

        self._error_label.grid(row=0, column=1, padx=5, pady=5)

        label_create_user.grid(row=1, column=1)
        label_username.grid(row=3, column=0)
        label_password.grid(row=4, column=0)

        self.entry_username.grid(row=3, column=1)
        self.entry_password.grid(row=4, column=1)

        button_create_user.grid(row=6, column=1)
        button_login.grid(row=7,column=1)

        self._hide_error()

    def _create_user(self):
        """When pushing a button create new user, it triggers the handler. First this redirects back 
        to UI class and after to service and repository classes."""
        try:
            self._handle_create_user(self.entry_username.get(), self.entry_password.get())
            self._handle_show_transaction_view()
        except errors.UsernameExistsError:
            self._show_error("Käyttäjätunnus on jo käytössä")
