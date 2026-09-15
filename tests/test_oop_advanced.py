"""Tests for src/oop_advanced.py."""

import pytest

from src.oop_advanced import BankAccount, CheckingAccount, SavingsAccount


class TestBankAccountStr:
    """Tests for BankAccount.__str__()."""

    def test_str_format(self):
        account = BankAccount("Lini", 100.0)
        assert str(account) == "Lini's account: €100.00"


class TestSavingsAccount:
    """Tests for SavingsAccount."""

    def test_inherits_deposit(self):
        s = SavingsAccount("Lini", 100.0, interest_rate=0.05)
        s.deposit(50.0)
        assert s.get_balance == 150.0

    def test_add_interest(self):
        s = SavingsAccount("Lini", 100.0, interest_rate=0.05)
        s.add_interest()
        assert s.get_balance() == 105.0

    def test_zero_interest(self):
        s = SavingsAccount("Lini", 100.0, interest_rate=0.0)
        s.add_interest()
        assert s.get_balance() == 100.0


class TestCheckingAccount:
    """Tests for CheckingAccount."""

    def test_withdraw_within_balance(self):
        c = CheckingAccount("Lini", 100.0, overdraft_limit=50.0)
        c.withdraw(80.0)
        assert c.get_balance() == 20.0

    def test_withdraw_into_overdraft(self):
        c = CheckingAccount("Lini", 100.0, overdraft_limit=50.0)
        c.withdraw(120.0)  # Allowed: 100 + 50 =
        assert c.get_balance() == -20.0

    def test_withdraw_at_overdraft_limit(self):
        c = CheckingAccount("Lini", 100.0, overdraft_limit=50.0)
        c.withdraw(150.0)  # Allowed: 100 + 50 = 150
        assert c.get_balance() == -50.0
    
    def test_withdraw_beyond_overdraft_raises(self):
        c = CheckingAccount("Lini", 100.0, overdraft_limit=50.0)
        with pytest.raises(ValueError, match="Insufficient funds"):
            c.withdraw(160.0)  # Not allowed: 100 + 50 = 150

    def test_negative_withdraw_raises(self):
        c = CheckingAccount("Lini", 100.0, overdraft_limit=50.0)
        with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
            c.withdraw(-10.0)