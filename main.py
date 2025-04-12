from data_handler import create_expense, save_expense
from analysis import total_by_category, monthly_summary

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("==== Expense Tracker ====")
    while True:
        print("\n1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Total")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = get_float_input("Amount spent: ₹")
            category = input("Category (food, travel, entertainment, etc.): ").strip()
            description = input("Description: ").strip()
            expense = create_expense(amount, category, description)
            save_expense(expense)
            print("Expense added successfully.")

        elif choice == "2":
            total = monthly_summary()
            print(f"Total spent this month: ₹{total:.2f}")

        elif choice == "3":
            category_totals = total_by_category()
            print("Expenses by Category:")
            for cat, amt in category_totals.items():
                print(f"  {cat.capitalize()}: ₹{amt:.2f}")

        elif choice == "4":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
