import json
import os
from utlities.moneycalcs import *
from utlities.algorithms.savings import *

budgetbuddy = {"Total Expenses": total_expenses, 
               "Top Expense": most_cmn_catg, 
               "Top Expense Amount": round(top_catg_expenses, 2),
               "Average Daily Spend: ": round(avg_day_spend, 2),
               "Number of Transactions: ": amount_of_transactions,
               "Savings Earned: ": round(calc_savings(), 2)}

def make_json(list):

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "budgetbuddy.json")

    with open(output_path, "w") as file:
        json.dump(list, file, indent=4)
    
    return json.dumps(list, indent=4)