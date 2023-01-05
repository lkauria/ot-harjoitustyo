from tkinter import Button, Entry, Label, StringVar, Frame, ttk

class TransactionView:
    """ Transaction view show the budget's incomes and expenses.
    """

    def __init__(self, root, user, handle_save_transaction, handle_show_transaction_view):
        self._root = root
        self._user = user
        self._handle_save_transaction = handle_save_transaction
        self._handle_show_transaction_view = handle_show_transaction_view
        self._frame = None
        self.amount = StringVar()
        self.subject = StringVar()
        self.is_income = True
        self._my_tree = ttk.Treeview(self._root)

        self._show()
    
    def pack(self):
        if self._frame:
            self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _show(self):

        self._frame = Frame(
            master=self._root,
            padx=100,
            pady=100
        )

        self._my_tree['columns'] = ("Tulo tai meno", "Summa")
        self._my_tree.column("#0", width=120, minwidth=25)
        self._my_tree.column("Tulo tai meno", anchor="w", width=120)
        self._my_tree.column("Summa", anchor="center", width=120)
        self._my_tree.heading("#0", text="Label", anchor="w")
        self._my_tree.heading("Tulo tai meno", text="Tulo tai meno", anchor="w")
        self._my_tree.heading("Summa", text="Summa", anchor="center")
        self._my_tree.insert("", "end", text="Item 1", values=("1a", "1b"))
        self._my_tree.insert("", "end", text="Item 2", values=("2a", "2b"))      

        self._my_tree.pack()

        label_transaction_view = Label(
            master=self._frame,
            text="Oma budjetointisi"
        )

        label_amount = Label(
            master=self._frame,
            text="Summa"
        )

        label_subject = Label(
            master=self._frame,
            text="Aihe"
        )

        self.entry_amount = Entry(
            master=self._frame,
            width=25
        )

        self.entry_subject = Entry(
            master=self._frame,
            width=25
        )

        button_expense_submit = Button(
            master=self._frame,
            text="Lisää uusi meno", 
            padx=50,
            pady=20, 
            command=self._handle_save_expense
        )

        button_income_submit = Button(
            master=self._frame,
            text="Lisää uusi tulo", 
            padx=50,
            pady=20, 
            command=self._handle_save_income
        ) 

        label_transaction_view.grid(row=0, column=1)
        label_amount.grid(row=2, column=0)
        label_subject.grid(row=3, column=0)

        self.entry_amount.grid(row=2, column=1)
        self.entry_subject.grid(row=3, column=1)

        button_expense_submit.grid(row=5, column=1)
        button_income_submit.grid(row=5, column=2)

        button_expense_submit.grid(row=7, column=1)
        button_income_submit.grid(row=7, column=2)

    def _handle_save_expense(self):
        self.is_income = False
        self.subject = self.entry_subject.get()
        self.amount = -1 * int(self.entry_amount.get())
        self._handle_save_income()

    def _handle_save_income(self):
        if self.is_income:
            self.subject = self.entry_subject.get()
            self.amount = int(self.entry_amount.get())
        self._handle_save_transaction(self._user, self.amount, self.subject)
        self.is_income = True
        self._handle_show_transaction_view()
