class Account:
    """Creating an Account class with methods"""

    def __init__(self, balance=0, interest=0):
        """Initializes the account with a balance and interest rate"""
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance

    def get_balance(self):
        """Returns the current balance of the account"""
        return self.balance

    def set_interest(self, interest):
        """Sets the interest rate for the account"""
        self.interest = interest

    def get_interest(self):
        """Returns the interest rate of the account"""
        return self.interest

    def deposit(self, amount):
        """Deposits a specified amount into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account if sufficient balance exists"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def apply_interest(self):
        """Applies the interest to the current balance"""
        interest_amount = self.balance * (self.interest / 100)
        self.balance += interest_amount
        print(f"Applied interest of {self.interest}%. New balance is {self.balance}.")

# Example usage:
account = Account(1000, 5)

# Deposit 500
account.deposit(500)
# Balance after deposit should be 1500

# Withdraw 200
account.withdraw(200)
# Balance after withdrawal should be 1300

# Apply interest
account.apply_interest()
# Balance after applying 5% interest should be 1365.0
