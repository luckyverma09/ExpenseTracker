# main.py

from services.expense_manager import ExpenseManager
from services.file_manager import FileManager
from utils.helpers import (
    display_menu,
    get_valid_amount,
    get_valid_category,
    get_valid_month,
    pause,
)

# ----------------------------------------
# Setup
# ----------------------------------------

file_manager = FileManager()

# Load saved expenses
loaded_expenses = file_manager.load_from_file()

# Create ExpenseManager
manager = ExpenseManager(loaded_expenses)

# ----------------------------------------
# Main Loop
# ----------------------------------------

while True:

    display_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        amount = get_valid_amount()
        category = get_valid_category()
        description = input("Enter the description: ").strip()

        manager.add_expense(amount, category, description)
        file_manager.save_to_file(manager.expenses)

        print("Expense added successfully!")

        pause()

    elif choice == "2":

        manager.view_expenses()

        pause()

    elif choice == "3":

        if len(manager.expenses) == 0:
            print("No expenses to delete.")
            pause()
            continue
    
        print("\nExpenses:\n")
    
        for index, expense in enumerate(manager.expenses, start=1):
            print(f"{index}.")
            print(expense)
    
        try:
            expense_number = int(input("Enter expense number to delete: "))
    
            removed = manager.delete_expense(expense_number - 1)
    
            if removed:
                file_manager.save_to_file(manager.expenses)
    
                print("\nDeleted Expense:")
                print(removed)
    
        except ValueError:
            print("Please enter a valid number.")
    
        pause()
        
    elif choice == "4":

        # Search expenses by category or description (exact match)
        keyword = input("Enter category or description: ").strip()
        result = manager.search_expense(keyword)
        if result:
            print("Expense found:")
            print(result)
        else:
            print("No matching expense found.")

        pause()

    elif choice == "5":

        # Monthly total
        month = get_valid_month()
        total = manager.calculate_monthly_total(month)
        print(f"\nTotal Expense for Month {month}: ₹{total:.2f}")

        pause()

    elif choice == "6":

        print("Thank you for using Expense Tracker!")
        break

    else:

        print("Invalid Choice!")

        pause()