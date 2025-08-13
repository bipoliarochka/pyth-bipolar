### **Repository 10: Expense Tracker**
```python
# Repository: python-expense-tracker
# Description: Track expenses and generate reports.

expenses = []

def add_expense(amount, category):
    """Add an expense."""
    expenses.append({"amount": amount, "category": category})
    print(f"Expense added: {amount} ({category})")

def generate_report():
    """Generate a report of expenses."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: {total}")
    for expense in expenses:
        print(f"- {expense['amount']} ({expense['category']})")

# Example usage
add_expense(100, "Food")
add_expense(50, "Transport")
generate_report()
