import matplotlib.pyplot as plt

def visualize_expenses():
    categories = {}
    for expense in expenses:
        categories[expense["category"]] = categories.get(expense["category"], 0) + expense["amount"]
    plt.bar(categories.keys(), categories.values())
    plt.title("Expense Breakdown")
    plt.show()

# Example usage
visualize_expenses()
