import datetime

expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    description = input("Enter description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    
    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            if 'date' in expense and 'category' in expense and 'amount' in expense and 'description' in expense:
                print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
            else:
                print("Incomplete expense entry.")


budget = 0  # Initialize budget globally

def set_budget():
    global budget
    try:
        budget = float(input("Enter your monthly budget: "))
        print(f"Budget set to: {budget}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def track_budget():
    if budget == 0:  # Check if the budget is still 0
        print("You haven't set a budget yet. Please set one first.")
        return

    total_expenses = sum(expense['amount'] for expense in expenses)
    if total_expenses > budget:
        print(f"You have exceeded your budget! You are over by {total_expenses - budget}.")
    else:
        print(f"You have {budget - total_expenses} left for the month.")


        
import csv

def save_expenses():
    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print("Expenses saved successfully.")

def load_expenses():
    global expenses
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.DictReader(file)
            expenses = []
            for row in reader:
                # Convert 'amount' to float
                row['amount'] = float(row['amount'])
                expenses.append(row)
        print("Expenses loaded successfully.")
    except FileNotFoundError:
        print("No previous expenses found.")
    except ValueError:
        print("Error in loading data: Amount field contains invalid values.")

def show_menu():
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Budget")
    print("4. Track Budget")
    print("5. Save Expenses")
    print("6. Exit")
    
    choice = int(input("Choose an option: "))
    return choice


def main():
    load_expenses()  # Load existing expenses if any

    while True:
        choice = show_menu()

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            set_budget()
        elif choice == 4:
            track_budget()
        elif choice == 5:
            save_expenses()
        elif choice == 6:
            save_expenses()  # Save expenses before exiting
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
