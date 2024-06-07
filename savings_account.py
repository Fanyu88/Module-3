# savings_account.py
from Account import Account  # Import the Account class

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance."""
    # Create an instance of the Account class
    savings_account = Account(balance, 0)  # Initial interest is 0

    # Calculate interest earned (annual interest divided by 12, multiplied by balance and months)
    interest_earned = (interest_rate / 100 / 12) * balance * months

    # Update the balance
    updated_balance = balance + interest_earned

    # Set the updated balance and interest earned in the account
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)

    return savings_account.get_balance(), savings_account.get_interest()  
