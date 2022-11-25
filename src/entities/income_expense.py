from csv import unregister_dialect


class Income_expense:
    def __init__(self, subject, sum, date_of_transaction, user_id):

        self.subject = subject
        self.sum = sum
        self.date_of_transaction = date_of_transaction 
        self.user_id = user_id
    
 