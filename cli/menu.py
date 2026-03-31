from storage.filehandler import load_data, save_data
from core.classifier import classify_category
from core.predictor import predict_spending
from utils.validator import validate_amount
from datetime import date

def run_menu():
    data = load_data()

    while True:
        print("\n=== Smart Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Predict Spending")
        print("4. Help")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                add_expense(data)
            elif choice == "2":
                view_expenses(data)
            elif choice == "3":
                predict_spending(data)
            elif choice == "4":
                show_help()
            elif choice == "5":
                save_data(data)
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except Exception as e:
            print(f"\n[Error] An unexpected error occurred: {e}")
            print("Please try again or select another option.\n")
            
        if choice != "5":
            input("\nPress Enter to continue...")

def add_expense(data):
    """Prompt the user for an expense and append it to the in-memory list."""
    try:
        amount = float(input("Enter amount (Rs): "))
        if not validate_amount(amount):
            print("Invalid amount! Amount must be greater than 0.")
            return

        desc = input("Enter description: ").strip()
        if not desc:
            print("Description cannot be empty.")
            return
        category = classify_category(desc)

        data.append({
            "amount": amount,
            "description": desc,
            "category": category,
            "date": str(date.today()),
        })

        save_data(data)  # persist immediately so no data is lost on crash
        print(f"[Success] Added Rs. {amount:.2f} under '{category}'.")

    except ValueError:
        print("Invalid input! Please enter a numeric amount.")

def view_expenses(data):
    if not data:
        print("No expenses found.")
        return

    print(f"{'#':<4} {'Amount (Rs)':>11}  {'Date':<12}  {'Category':<15}  Description")
    print("-" * 62)
    for i, exp in enumerate(data, 1):
        date_str = exp.get('date', 'N/A')
        amount_val = float(exp['amount'])
        print(f"{i:<4} {amount_val:>11.2f}  {date_str:<12}  {exp['category']:<15}  {exp['description']}")

def show_help():
    """Display a brief description of each menu option."""
    print("\n--- Help ---")
    print("1 → Add Expense    : Record a new spend with amount & description")
    print("2 → View Expenses  : List all recorded expenses in a table")
    print("3 → Predict Spending: Estimate the next expense using linear regression")
    print("4 → Help           : Show this help text")
    print("5 → Exit           : Save all data and quit")