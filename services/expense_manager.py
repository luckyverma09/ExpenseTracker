from datetime import datetime
from expense import Expense

class ExpenseManager():
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
    
    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found.")
            return
        for expense in self.expenses:
            print(expense)
    
    def delete_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            print("Please enter a valid expense index.")
            return
        
        removed = self.expenses.pop(index)
        return removed
    
    def search_expense(self, keyword):
        for expense in self.expenses:
            if(expense.category == keyword or expense.description == keyword):
                return expense

        return None

    def calculate_monthly_total(self,target_month):
        total = 0
        for expense in self.expenses:
            month = datetime.strptime(expense.date, "%Y-%m-%d").month
            if(target_month == month):
                total += expense.amount
        
        return total       