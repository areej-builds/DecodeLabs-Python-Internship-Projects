def add_expense(new_expense: float, total_spent: float) -> float:
    """
    Function to add the new expense to the total tracker.
    """
    # Dynamic calculation unit that handles data accumulation
    total_spent = total_spent + new_expense
    print("\n[SUCCESS] Expense added successfully!")
    return total_spent

def main():
    # Application state memory initialization to track calculations
    total_spent = 0.0

    print("\n" + "=" * 35)
    print("     WELCOME TO EXPENSE TRACKER!     ")
    print("=" * 35)

    # Continuous operational loop for processing menu actions
    while True:
        print("\n--- Main Menu ---")
        print("1. Add New Expense")
        print("2. View Total Expenses")
        print("3. Exit Program")
        print("-" * 18)

        choice = None  
        
        try:
            # Capturing and validating the numerical action input
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("\n[ERROR] Invalid input! Please enter a number (1, 2, or 3).")
            continue

        # Processing system operations based on user selection
        if choice == 1:
            try:
                new_expense = float(input("\nEnter expense amount: "))
                
                # Input validation barrier to reject negative data entries
                if new_expense < 0:
                    print("[WARNING] Expense amount cannot be negative!")
                else:
                    total_spent = add_expense(new_expense, total_spent)
            except ValueError:
                print("\n[ERROR] Invalid data! Please enter a valid number for amount.")

        elif choice == 2:
            print(f"\n[STATUS] Current Total Expense: ${total_spent:.2f}")

        elif choice == 3:
            # Kill-switch activation: Graceful shutdown and final state logging
            print("\n" + "=" * 35)
            print("          FINAL REPORT             ")
            print(f"  Total Amount Spent: ${total_spent:.2f}")
            print("=" * 35)
            print("Thank you for using Expense Tracker. Goodbye!")
            break

        else:
            print("\n[ERROR] Invalid option! Please choose between 1 and 3.")

if __name__ == "__main__":
    main()
 
