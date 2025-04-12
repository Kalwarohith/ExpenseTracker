import json
from datetime import datetime

FILENAME = "expenses.json"

def load_expenses():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expense(expense):
    data = load_expenses()
    data.append(expense)
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def create_expense(amount, category, description):
    return {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
