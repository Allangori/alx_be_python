class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if sufficient funds are available.
        Returns True if the withdrawal was successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print( f"Current Balance: {self.account_balance}")