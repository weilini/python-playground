"""Tests for src/oop_basics.py."""

import pytest

from src.oop_basics import BankAccount


class TestBankAccountInit:
    """Tests for BankAccount.__init__()."""

    def test_default_balance(self):
        account = BankAccount("Lini")
        assert account.get_balance() == 0.0

    def test_with_initial_balance(self):
        account = BankAccount("Lini", 100.0)
        assert account.get_balance() == 100.0

    def test_stores_owner(self):
        account = BankAccount("Lini")
        assert account.owner == "Lini"


class TestDeposit:
    """Tests for BankAccount.deposit()."""

    def test_deposit_adds_to_balance(self):
        account = BankAccount("Lini")
        account.deposit(50.0)
        assert account.get_balance() == 50.0

    def test_multiple_deposits(self):
        account = BankAccount("Lini")
        account.deposit(50.0)
        account.deposit(30.0)
        assert account.get_balance() == 80.0

    def test_deposit_zero_raises(self):
        account = BankAccount("Lini")
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            account.deposit(0)

    def test_deposit_negative_raises(self):
        account = BankAccount("Lini")
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            account.deposit(-10)


class TestWithdraw:
    """Tests for BankAccount.withdraw()."""

    def test_withdraw_reduces_balance(self):
        account = BankAccount("Lini", 100.0)
        account.withdraw(30.0)
        assert account.get_balance() == 70.0

    def test_withdraw_exact_balance(self):
        account = BankAccount("Lini", 100.0)
        account.withdraw(100.0)
        assert account.get_balance() == 0.0

    def test_withdraw_zero_raises(self):
        account = BankAccount("Lini", 100.0)
        with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
            account.withdraw(0)

    def test_withdraw_negative_raises(self):
        account = BankAccount("Lini", 100.0)
        with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
            account.withdraw(-10)

    def test_withdraw_more_than_balance_raises(self):
        account = BankAccount("Lini", 100.0)
        with pytest.raises(ValueError, match="Insufficient funds"):
            account.withdraw(150.0)


class TestGetBalance:
    """Tests for BankAccount.get_balance()."""

    def test_returns_current_balance(self):
        account = BankAccount("Lini", 42.0)
        assert account.get_balance() == 42.0

    def test_reflects_deposits_and_withdrawals(self):
        account = BankAccount("Lini", 100.0)
        account.deposit(50.0)
        account.withdraw(30.0)
        assert account.get_balance() == 120.0