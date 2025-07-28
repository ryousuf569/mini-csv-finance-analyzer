import csv

class Expense:
    all_list = []
    all_dict = {}
    next_transaction = 0

    def __init__(self, date, amount, category, vendor):
        assert amount >= 0, "You can't spend negative amount of money"

        self.transaction = Expense.next_transaction
        self.date = date
        self.amount = amount
        self.category = category
        self.vendor = vendor

        Expense.all_list.append(self)
        Expense.all_dict[self.transaction] = self

        Expense.next_transaction += 1

    @classmethod
    def get_transactions(cls):
        with open('data/sample_expenses.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Expense(
                date=item.get('date'),
                amount=float(item.get('amount')),
                category=item.get('category'),
                vendor=item.get('vendor')
            )

    def __repr__(self):
        return f"Date: {self.date} | Amount: {self.amount} | Category: {self.category} | Vendor: {self.vendor}"
    
Expense.get_transactions()
transaction_list = [Expense.amount for Expense in Expense.all_dict.values()]
category_list = [Category.category for Category in Expense.all_dict.values()]
category_list.sort()
