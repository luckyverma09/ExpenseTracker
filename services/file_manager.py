import json
from models.expense import Expense


class FileManager:
    def save_to_file(self, expenses):
        data = []

        for expense in expenses:
            data.append(expense.to_dict())

        with open("data/expenses.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self):
        try:
            with open("data/expenses.json", "r") as file:
                data = json.load(file)

                expenses = []

                for item in data:
                    expense = Expense.from_dict(item)
                    expenses.append(expense)

                return expenses
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
            