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

        transactions = self._handle_get_transactions(self._user)

        """Draw a table by ttk.Treeview()"""
        self._my_tree['columns'] = ("one")

        self._my_tree.heading("#0", text="Aihe")
        self._my_tree.heading("one", text="Summa")
 
       
        # must be replaces with actual data
        for transaction in transactions:
            self._my_tree.insert("", "end", text=transaction[0], values=transaction[1:])
            self._total_amount = self._total_amount + transaction[1]

        label_transaction_view = Label(
            master=self._frame,
            text="Oma budjetointisi"
        )

        label_amount = Label(
            master=self._frame,
            text="Summa"
        )

        label_total_amount = Label(
            master=self._frame,
            text=("Budjettisi kokonaisarvio on: ", str(self._total_amount))
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

        # This is not working with the treeview -> locating does not work.
        self._my_tree.grid(row=9, column=1)

        label_total_amount.grid(row=0, column=1)
        # Is this pack allowed to use here? Does not work without.
        self._my_tree.pack()


    def _handle_save_expense(self):
        self.is_income = False
        self.subject = self.entry_subject.get()
        self.amount = self.entry_amount.get()
        # create logic for checking input
        if self.amount:
            print(self.amount)
        else:
            print('empty input')
        self._handle_save_income()

    def _handle_save_income(self):
        if self.is_income:
            self.subject = self.entry_subject.get()
            self.amount = int(self.entry_amount.get())
        self._handle_save_transaction(self._user, self.amount, self.subject)
        self.is_income = True
        self._handle_show_transaction_view()
