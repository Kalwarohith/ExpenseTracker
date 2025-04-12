from collections import defaultdict
from datetime import datetime
from data_handler import load_expenses

def total_by_category():
    expenses = load_expenses()
    summary = defaultdict(float)
    for expense in expenses:
        summary[expense["category"]] += expense["amount"]
    return summary

def monthly_summary():
    expenses = load_expenses()
    this_month = datetime.now().strftime("%Y-%m")
    total = 0
    for expense in expenses:
        if expense["date"].startswith(this_month):
            total += expense["amount"]
    return total
