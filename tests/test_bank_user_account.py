import pytest
from bank_user_account.main import BankAccount, User


def test_user_instance():
    user1 = User('test-name', 'test-surname', 1234)
    assert isinstance(user1, User)
    assert user1._passport_nr is not None
    assert isinstance(user1._name, str)


def test_balance():
    bank = BankAccount('n', 's', 1)
    assert isinstance(bank, BankAccount)


def test_id():
    bank = BankAccount('n', 's', 1)
    assert isinstance(bank._id, str)


def test_deposit():
    bank = BankAccount('n', 's', 1)
    bank.make_deposit(200)
    bank.make_deposit(200)
    assert bank._bank_balance == 400


def test_withdraw():
    bank = BankAccount('n', 's', 1)
    bank.make_deposit(200)
    bank.withdraw(100)
    assert bank._bank_balance == 100


def test_delete_account():
    bank = BankAccount('n', 's', 1)
    bank.delete_account()
    assert bank._name is not set

