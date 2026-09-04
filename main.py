"""
Personal Expense Tracker
Week 2 Final Project
"""

from expenses import (add_expense, view_expenses, view_total_spending, view_spending_by_category)


def display_menu():
    """
    Show the main menu to the user.
    """

    print("\n" + "=" * 40)
    print("Personal Expense Tracker")
    print("=" * 40)
    print("1. Add expense")
    print("2. View expenses")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("help - Show this menu")
    print("quit - Exit application")
    print()


def handle_choice(choice):
    """
    Process the user's choice and call appropriate functions.
    
    Args:
    choice (str): The user's menu choice.
     
    Returns:
    bool: True to continue the application, False to exit.
    """
     
    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total_spending()

    elif choice == "4":
        view_spending_by_category()

    elif choice == "help":
        display_menu()

    elif choice == "quit":
        print("Thanks for using the application. Goodbye!")
        return False

    else:
        print(f"'{choice}' is not a valid option. Type 'help' to see available commands.")

    return True


def main():
    """
    Main application loop.
    Displays menu, gets user input, and processes choices.
    """

    print("Welcome to the Personal Expense Tracker!")
    display_menu()

    running = True

    while running:
        choice = input("Enter your choice: ").strip().lower()
        running = handle_choice(choice)

if __name__ == "__main__":
    main()