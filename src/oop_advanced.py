"""Advanced OOP exercises for Stage 2, Day 6.

This module demonstrates:
- Inheritance
- super()
- Method overriding
- Polymorphism
- @property
- __str__ and __repr__
"""


class BankAccount:
    """A basic bank account (parent class)."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def __str__(self) -> str:
        return f"{self.owner}'s account: €{self.balance:.2f}"


class SavingsAccount(BankAccount):
    """A savings account that earns interest."""

    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        

    def add_interest(self) -> None:
        """Add interest to the balance.

        Formula: balance *= (1 + interest_rate)
        """
        self.balance *= (1 + self.interest_rate)


class CheckingAccount(BankAccount):
    """A checking account with overdraft protection."""

    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 100.0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        """Withdraw, allowing overdraft up to the limit.

        Raises:
            ValueError: If amount is not positive.
            ValueError: If amount exceeds balance + overdraft_limit.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


if __name__ == "__main__":
    # Test BankAccount
    a = BankAccount("Lini", 100.0)
    print(a)                          # Lini's account: €100.00

    # Test SavingsAccount
    s = SavingsAccount("Lini", 100.0, 0.05)
    s.add_interest()
    print(s.balance)                  # 105.0

    # Test CheckingAccount
    c = CheckingAccount("Lini", 50.0, 100.0)
    c.withdraw(120.0)                 # Allowed: 50 + 100 = 150
    print(c.balance)                  # -70.0