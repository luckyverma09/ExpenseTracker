from datetime import datetime

class Expense:
    def __init__(self, amount, category, desc, date = None):
        self.amount = amount
        self.category = category
        self.desc = desc

        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%d")
        else:
            self.date = date


    def to_dict(self):
        return{
            "amount" : self.amount,
            "category" : self.category,
            "desc" : self.desc,
            "date" : self.date
        }           
    
    @classmethod
    def from_dict(cls, data):
        """Create a Expense object from dictionary."""
        return cls(
            amount = data["amount"],
            category = data["category"],
            desc = data["desc"],
            date = data["date"],
        )
    
    def __str__(self):
        return(
            f"Date: {self.date}\n"
            f"Category: {self.category}\n"
            f"Description: {self.desc}\n"
            f"Amount: {self.amount:.2f}\n"
        )