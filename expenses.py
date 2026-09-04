def add_expense():
    """
    Ask the user for expense information.
    """
    print("\n--- Add Expense ---")

    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    amount = input("Enter expense amount: $")

    with open("expenses.txt", "a") as file:
        file.write(f"{description}, {category}, {amount}\n")  

    print("\nExpense entered:")
    print(f"Description: {description}")
    print(f"Category: {category}")
    print(f"Amount: ${amount}")

def view_expenses():
    """
    Display all saved expenses.
    """
    print("\n--- Saved Expenses ---")
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
        if not expenses:
            print("No expenses found.")
            return
        for expense in expenses:
            description, category, amount = expense.strip().split(", ")
            print(f"Description: {description}, Category: {category}, Amount: ${amount}")  





            