from tkinter import Button, Entry, Label, StringVar, Frame, ttk

class TransactionView:
    """ Transaction view show the budget's incomes and expenses.
    """
    def __init__(self, root, user, handle_save_transaction, handle_show_transaction_view, handle_get_transactions):
        self._root = root
        self._user = user
        self._handle_save_transaction = handle_save_transaction
        self._handle_show_transaction_view = handle_show_transaction_view
        self._handle_get_transactions = handle_get_transactions
        self._frame = None
        self.amount = StringVar()
        self.subject = StringVar()
        self._total_amount = 0
        self.is_income = True
        self.my_tree = ttk.Treeview(master=self._root)

        self._show()
    
    def pack(self):
        """If the frame exists, this packs the widgets to the window.
        """
        if self._frame:
            self._frame.pack()

    def destroy(self):
        """This method destroys widgets that are in the window.
        """
        self._frame.destroy()

    def _show(self):
        """This sets the probable error message to the window as one widget.

        Args:
            message (str): Error message that is defined in the login method with try-except.
        """
        self._frame = Frame(
            master=self._root,
            padx=100,
            pady=100
        )

        transactions = self._handle_get_transactions(self._user)

        """Draw a table by ttk.Treeview(), this mixes .pack() and .grid() that is not solved yet"""
        self.my_tree['columns'] = ("one")

        self.my_tree.heading("#0", text="Aihe")
        self.my_tree.heading("one", text="Summa")
 
        for transaction in transactions:
            self.my_tree.insert("", "end", text=transaction[0], values=transaction[1:])
            self._total_amount = self._total_amount + transaction[1]

        label_transaction_view = Label(
            master=self._frame,
            pady=30,
            text="Lisää alla uusi meno tai tulo:"
        )

        label_amount = Label(
            master=self._frame,
            text="Summa"
        )

        label_total_amount = Label(
            master=self._frame,
            text=("Budjettisi kokonaisarvio on: ")
        )

        label_total_amount_value = Label(
            master=self._frame,
            anchor="w",
            text=self._total_amount
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

        label_transaction_view.grid(row=1, column=1)

        label_amount.grid(row=2, column=0)
        label_subject.grid(row=3, column=0)

        self.entry_amount.grid(row=2, column=1)
        self.entry_subject.grid(row=3, column=1)

        button_expense_submit.grid(row=5, column=1)
        button_income_submit.grid(row=5, column=2)

        button_expense_submit.grid(row=7, column=1)
        button_income_submit.grid(row=7, column=2)

        # This is not working with the treeview -> locating does not work. neither with sticky. Unsolved.
        self.my_tree.grid(row=25, column=1, sticky="s")

        label_total_amount.grid(row=0, column=1)
        label_total_amount_value.grid(row=0, column=2)

        self.my_tree.pack()


    def _handle_save_expense(self):
        """When saving the expense button (button_expense_submit) is pushed this method is called. Here a positive figure is changed to negative as it is an expense.
        The saving is happening through a _handle_save_income methood as the positive income.
        """
        self.is_income = False
        self.subject = self.entry_subject.get()
        self.amount = -1 * int(self.entry_amount.get())
        # to do: check inputs
        self._handle_save_income()

    def _handle_save_income(self):
        """This handles saving both income and expense through the transaction service class.
        """
        if self.is_income:
            self.subject = self.entry_subject.get()
            self.amount = int(self.entry_amount.get())
        self._handle_save_transaction(self._user, self.amount, self.subject)
        self.is_income = True

        self.my_tree.pack_forget()
        self._handle_show_transaction_view()
