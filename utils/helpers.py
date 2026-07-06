def display_menu():
    print("""
========== Expense Tracker ==========
1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expense
5. Monthly Total
6. Exit
""")
    
def get_valid_amount():    
    while True:
        amount = input("Enter the amount : ")
        try:
            amount = float(amount)
            if(amount > 0):
                return amount
        except ValueError:
            print("Please Enter valid Amount : ")


def get_valid_category():
    categories = ("food", "shopping", "travel", "bills", "other")

    while True:
        category = input("Enter Category: ").strip().lower()
        if category in categories:
            return category
        print("Please enter a valid category: food, shopping, travel, bills, other")
    
def get_valid_month():
    while True:
        month = input("Enter the Month : ")
        try:
            month = int(month)
            if(month > 0 and month < 13):
                return month
        except ValueError:
            print("Please Enter valid Month : ")

def pause():
    input("Press Enter to continue...")