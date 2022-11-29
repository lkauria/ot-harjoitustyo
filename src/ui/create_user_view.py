from tkinter import Button, Entry, Label, StringVar, ttk


class CreateUserView:

    def __init__(self, root, handle_create_user):
        self._root = root
        self._handle_create_user = handle_create_user
        self.username = StringVar()
        self.password = StringVar()

        self._show()

    def pack(self):
        pass

    def _show(self):

        login_label = Label(self._root, text="Logiikka kirjautumiselle alkaa")
        login_label.grid(row=4, column=1)

        label_welcome = Label(self._root, text="Tervetuloa budjetointisovellukseen!")
        button_login = Button(self._root, text="Kirjaudu", padx=50,
                        pady=20, command=self._create_user, bg="#66CDAA")

        self.entry_username = Entry(self._root, width=60)
        self.entry_password = Entry(self._root, width=60)

        label_welcome.grid(row=0, column=1)
        button_login.grid(row=3, column=1)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=2, column=1)

    def _create_user(self):

        self._handle_create_user(self.entry_username.get(), self.entry_password.get())
        