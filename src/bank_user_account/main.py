import shortuuid


class User:

    def __init__(self, name, surname, passport_nr, id=shortuuid.uuid()):
        self._name = name
        self._surname = surname
        self._passport_nr = passport_nr
        self._id = id

    @property
    def user(self):
        print(f'userdata id:{self._id} name:{self._name} surname: {self._surname} passport: {self._passport_nr}')


class BankAccount(User):

    def __init__(self, name, surname, passport_nr, bank_balance=0):
        super().__init__(name, surname, passport_nr)
        self._bank_balance = bank_balance

    def __del__(self):
        print(f'{self} deleted')

    def make_deposit(self, deposit: float):
        self._bank_balance = self._bank_balance + deposit
        # return self._bank_balance #zmiana

    def withdraw(self, withdraw: float):
        if self._bank_balance >= withdraw > 0:
            self._bank_balance = self._bank_balance - withdraw
        else:
            raise Exception('no money to withdraw such sum')

    def show_account_balance(self):
        print(f'account balance user: {self._name}, balance: {self._bank_balance}')

    def delete_account(self):
        self.__del__()
        print(f'{self} account deleted')


b1 = BankAccount('bart', 'd', 556)
print(b1.__dict__)

b1.user
print('kdsdkslk')
b1.make_deposit(100)
print(b1.__dict__)

b1.withdraw(100)
print(b1.__dict__)
