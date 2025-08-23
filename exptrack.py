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
        
import matplotlib.pyplot as plt

def visualize_expenses():
    categories = {}
    for expense in expenses:
        categories[expense["category"]] = categories.get(expense["category"], 0) + expense["amount"]
    plt.bar(categories.keys(), categories.values())
    plt.title("Expense Breakdown")
    plt.show() 

def filter_expenses_by_category(category):
    filtered = [expense for expense in expenses if expense["category"] == category]
    if not filtered:
        print(f"No expenses found for category: {category}")
    else:
        print(f"Expenses for category '{category}':")
        for expense in filtered:
            print(f"- {expense['amount']} ({expense['category']})")
 from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_to_pdf(expenses, filename="expenses.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Expense Report")
    y = 700
    for expense in expenses:
        c.drawString(100, y, f"{expense['category']}: ${expense['amount']}")
        y -= 20
    c.save()
    print(f"Expense report saved to {filename}")

# Example usage
expenses = [{"category": "Food", "amount": 100}, {"category": "Transport", "amount": 50}]
export_to_pdf(expenses)           

# Example usage
filter_expenses_by_category("Food")

# Example usage
add_expense(100, "Food")
add_expense(50, "Transport")
generate_report()
