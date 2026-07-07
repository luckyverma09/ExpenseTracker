# 💰 Personal Expense Tracker (CLI)

A simple command-line based **Personal Expense Tracker** built using **Python**. This project helps users manage their daily expenses by adding, viewing, searching, deleting, and calculating monthly expenses. All data is stored locally in a JSON file, ensuring persistence between program runs.

---

## 📌 Features

* ➕ Add a new expense
* 📋 View all expenses
* 🗑️ Delete an expense
* 🔍 Search expenses by category or description
* 📅 Calculate total monthly expenses
* 💾 Automatically save data to a JSON file
* 📂 Load saved expenses when the application starts
* ✅ Input validation for amount, category, and month
* 🧩 Modular and object-oriented code structure

---

## 📁 Project Structure

```text
ExpenseTracker/
│
├── data/
│   └── expenses.json
│
├── models/
│   └── expense.py
│
├── services/
│   ├── expense_manager.py
│   └── file_manager.py
│
├── utils/
│   └── helpers.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

* Python 3
* JSON
* Object-Oriented Programming (OOP)

---

## 📚 Concepts Covered

This project demonstrates the following Python concepts:

* Variables & Data Types
* Conditional Statements
* Loops
* Functions
* Classes & Objects
* File Handling
* JSON Serialization
* Exception Handling
* Modular Programming
* Input Validation

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder

```bash
cd ExpenseTracker
```

### 3. Run the application

```bash
python main.py
```

---

## 📷 Sample Menu

```text
========== Expense Tracker ==========

1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expense
5. Monthly Total
6. Exit
```

---

## 💡 Sample Expense

```text
Date: 2026-07-08
Category: food
Description: Pizza
Amount: 250.00
```

---

## 🔄 How It Works

1. The application loads previously saved expenses from `expenses.json`.
2. Users interact with a menu-driven interface.
3. Expenses are stored as `Expense` objects.
4. `ExpenseManager` performs all business operations.
5. `FileManager` handles reading and writing JSON data.
6. Every change is immediately saved to the JSON file.

---

## 🧱 Project Architecture

```text
                main.py
                    │
     ┌──────────────┴──────────────┐
     │                             │
 Helpers                     ExpenseManager
                                     │
                                     ▼
                                Expense Model
                                     │
                                     ▼
                               FileManager
                                     │
                                     ▼
                              expenses.json
```

---

## 🚀 Future Improvements

* ✏️ Edit an existing expense
* 📊 Expense summary by category
* 📈 Monthly spending report
* 🏷️ Custom expense categories
* 📤 Export expenses to CSV
* 📉 Expense analytics and charts
* 🔍 Partial keyword search
* 🖥️ GUI version using Tkinter or PyQt

---

## 👨‍💻 Author

Developed as a learning project to strengthen Python fundamentals, Object-Oriented Programming, modular programming, and file handling.

---

## 📄 License

This project is open-source and available for educational and personal use.
