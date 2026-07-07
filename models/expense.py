from datetime import datetime

class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description

        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"],
        )

    def __str__(self):
        return (
            f"Date: {self.date}\n"
            f"Category: {self.category}\n"
            f"Description: {self.description}\n"
            f"Amount: {self.amount:.2f}\n"
        )