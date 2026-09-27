import csv
import os

FILE_NAME = "expenses.csv"


def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "category", "amount", "description"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    try:
        amount = float(amount)

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("\nExpense added successfully!")

    except ValueError:
        print("\nInvalid amount! Please enter a number.")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n----- All Expenses -----")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']} | "
            f"{expense['description']}"
        )


def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += float(expense["amount"])

    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n----- Category Wise Expenses -----")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Wise Expenses")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_expenses(expenses)

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
