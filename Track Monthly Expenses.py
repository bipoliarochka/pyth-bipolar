# Repository: python-expense-tracker
# New Feature: Track monthly expenses

expenses = []

def add_expense(amount, category, date):
    """Add an expense with a specific date."""
    expenses.append({"amount": amount, "category": category, "date": date})

def monthly_summary(month):
    """Generate a summary of expenses for a specific month."""
    total = sum(expense["amount"] for expense in expenses if expense["date"].startswith(month))
    print(f"Total expenses for {month}: {total}")
    for expense in expenses:
        if expense["date"].startswith(month):
            print(f"- {expense['amount']} ({expense['category']})")

# Example usage
add_expense(100, "Food", "2023-10-01")
add_expense(50, "Transport", "2023-10-02")
monthly_summary("2023-10")
