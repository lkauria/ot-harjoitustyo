from tkinter import Button, Entry, Label, StringVar, ttk


class CreateUserView:

    def __init__(self, root, handle_create_user):
        self._root = root
        self._handle_create_user = handle_create_user
        self.username = StringVar()
        self.password = StringVar()

        self._show()

    
    def pack(self):
        print("CreateUserView pack")

    def destroy(self):
        print("CreateUserView destroy")

    def _show(self):

        label_create_user = Label(
            self._root, 
            text="Luo käyttäjätunnus"
        )

        label_username = Label(
            self._root, 
            text="käyttäjätunnus"
        )

        label_password = Label(
            self._root, 
            text="salasana"
        )

        self.entry_username = Entry(
            self._root, 
            width=25
        )

        self.entry_password = Entry(
            self._root, 
            width=25
        )

        button_create_user = Button(
            self._root, 
            text="Luo tunnus", 
            padx=50,
            pady=20, 
            command=self._create_user, 
            bg="#66CDAA"
        )

        label_create_user.grid(row=0, column=1)
        label_username.grid(row=2, column=0)
        label_password.grid(row=3, column=0)

        self.entry_username.grid(row=2, column=1)
        self.entry_password.grid(row=3, column=1)

        button_create_user.grid(row=5, column=1)

    def _create_user(self):
        self._handle_create_user(self.entry_username.get(), self.entry_password.get())
        