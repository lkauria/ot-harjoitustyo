from tkinter import Button, Entry, Label, StringVar, Frame

class TransactionView:
    """ Transaction view show the budget's incomes and expenses.
    """

    def __init__(self, root, user, handle_save_transaction):
        self._root = root
        self._user = user
        self._handle_save_transaction = handle_save_transaction
        self._frame = None
        self.amount = StringVar()
        self.subject = StringVar()

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

        self.amount = Entry(
            master=self._frame,
            width=25
        )

        self.subject = Entry(
            master=self._frame,
            width=25
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

        self.amount.grid(row=2, column=1)
        self.subject.grid(row=3, column=1)

        button_expense_submit.grid(row=5, column=1)
        button_income_submit.grid(row=5, column=2)

        button_expense_submit.grid(row=7, column=1)
        button_income_submit.grid(row=7, column=2)

    def _handle_save_expense(self):
        self.entry_amount = -1 * self.entry_amount.get()
        self._handle_save_income

    def _handle_save_income(self):
        self.amount = self.entry_amount.get()
        self.subject = self.entry_subject.get()
        self._handle_save_transaction(self.amount, self.subject)
