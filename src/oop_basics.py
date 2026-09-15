"""Object-Oriented Programming exercises for Stage 2, Day 5.

This module demonstrates:
- Classes and objects
- The __init__ method (constructor)
- The self keyword
- Instance attributes and methods
"""


class BankAccount:
    """A simple bank account class.

    Attributes:
        owner: The name of the account holder.
        balance: The current balance (default 0.0).
    """

    def __init__(self, owner: str, initial_balance: float = 0.0):
        """Create a new BankAccount.

        Args:
            owner: Name of the account holder.
            initial_balance: Starting balance (default 0.0).
        """
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """Add money to the account.

        Args:
            amount: Amount to deposit. Must be positive.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Remove money from the account.

        Args:
            amount: Amount to withdraw. Must be positive and <= balance.

        Raises:
            ValueError: If amount is not positive or exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance


if __name__ == "__main__":
    # Manual test
    account = BankAccount("Lini", 100.0)
    print(account.get_balance())  # 100.0

    account.deposit(50.0)
    print(account.get_balance())  # 150.0

    account.withdraw(30.0)
    print(account.get_balance())  # 120.0

    # Uncomment to test error paths:
    # account.deposit(-10)
    # account.withdraw(1000)
