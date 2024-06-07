# customer_banking.py

from cd_account import create_cd_account
from savings_account import create_savings_account  # Ensure this is correctly implemented

def main():
    """Prompts for savings and CD account details, calculates interest, and displays results."""

    # Savings Account
    print("\nSavings Account:")
    while True:
        try:
            savings_balance = float(input("Enter the initial balance: $"))
            if savings_balance >= 0:  
                break
            else:
                print("Invalid input. Please enter a positive number or zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            savings_interest = float(input("Enter the APR interest rate (%): "))
            if savings_interest >= 0:
                break
            else:
                print("Invalid input. Please enter a positive number or zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            savings_maturity = int(input("Enter the maturity period (months): "))
            if savings_maturity > 0:
                break
            else:
                print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    updated_savings_balance, interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity
    )
    print("\nSavings Account Results:")
    print(f"Interest earned: ${interest_earned:.2f}")
    print(f"Updated balance: ${updated_savings_balance:.2f}")

    # CD Account
    print("\nCD Account:")
    while True:
        try:
            cd_balance = float(input("Enter the initial balance: $"))
            if cd_balance >= 0:  
                break
            else:
                print("Invalid input. Please enter a positive number or zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            cd_interest = float(input("Enter the APR interest rate (%): "))
            if cd_interest >= 0:
                break
            else:
                print("Invalid input. Please enter a positive number or zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            cd_maturity = int(input("Enter the maturity period (months): "))
            if cd_maturity > 0:
                break
            else:
                print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    updated_cd_balance, interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity
    )
    print("\nCD Account Results:")
    print(f"Interest earned: ${interest_earned:.2f}")
    print(f"Updated balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
     main()
