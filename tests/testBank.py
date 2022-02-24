import unittest
from src.bank_user_account.main import BankAccount, User


class TestUser(unittest.TestCase):

    def test_user_instance(self):
        user1 = User('test-name', 'test-surname', 1234)
        assert isinstance(user1, User)
        assert user1.passport_nr is not None
        assert isinstance(user1.name, str)


class TestAccount(unittest.TestCase):

    def test_balance(self):
        bank = BankAccount('n', 's', 1)
        assert isinstance(bank, BankAccount)

    def test_id(self):
        bank = BankAccount('n', 's', 1)
        assert isinstance(bank.id, str)

    def test_deposit(self):
        bank = BankAccount('n', 's', 1)
        bank.make_deposit(200)
        bank.make_deposit(200)
        assert bank.bank_balance == 400

    def test_withdraw(self):
        bank = BankAccount('n', 's', 1)
        bank.make_deposit(200)
        bank.withdraw(100)
        assert bank.bank_balance == 100

    def test_delete_account(self):
        bank = BankAccount('n', 's', 1)
        bank.delete_account()
        assert bank.name is not set


if __name__ == '__main__':
    unittest.main()
