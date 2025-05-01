from decimal import Decimal
from random import randint

try:
    from models.customer import Customer
    from models.bank import Bank
except ModuleNotFoundError:
    from customer import Customer
    from bank import Bank

class Account:
    def __init__(self, bank: Bank, customer: Customer, currency: str = 'IRR'):
        self.__bank = bank
        self.__customer = customer # Navigator
        self.__currency = currency
        self.__balance = Decimal('0')
        self.__account_number = str(randint(1000, 9999))

        self.__customer.add_account(self)


    @property
    def customer(self):
        return self.__customer
    
    @property
    def currency(self):
        return self.__currency
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def withdraw_balance(self):
        return self.__balance - self.__bank.withdraw_threshold

    @property
    def account_number(self):
        return self.__account_number

    def deposit(self, amount: Decimal):
        self.__balance += amount

    def withdraw(self, amount: Decimal) -> bool:
        """True if ok, False if amount is more than balance"""
        if amount > self.withdraw_balance:
            return False
        
        self.__balance -= amount
        return True

def main():
    c = Customer(name='ali', nid='1234')
    a = Account(c)
    a.deposit(10000)
    print(c.get_account(a.account_number).balance)

if __name__ == '__main__':
    main()