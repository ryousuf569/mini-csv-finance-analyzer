from utlities.objects import *
from collections import *

total_expenses = 0 
top_catg_expenses = 0
category_counter = Counter(category_list)
avg_day_spend = sum(transaction_list) / len(transaction_list)
amount_of_transactions = len(transaction_list)

for e in transaction_list:
    total_expenses += e

most_cmn_catg_list = (list(category_counter.most_common(1)))
most_cmn_catg = most_cmn_catg_list[0][0]
mst_cmn_catg_amount = [expense.amount for expense in Expense.all_dict.values() if expense.category == most_cmn_catg]
for e in mst_cmn_catg_amount:
    top_catg_expenses += e

