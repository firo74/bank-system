from dataclasses import dataclass
from decimal import Decimal

from models import Account, Bank, Customer

class AccountManager:
    def __init__(self, bank: Bank):
        self.accounts : dict[str, Account] = {}
        self.customers : dict[str, Customer] = {}
        self.bank = bank

    def create_account(self, info: 'InitialInfo') -> tuple[str, Decimal]:
        # filtered_customers = list(filter(lambda c: c.nid == info.nid, self.customers))
        # if len(filtered_customers) > 0:
        #     customer = filtered_customers[0]
        # else:
        #     customer = Customer(info.nid, info.name)

        customer = self.customers.get(info.nid, Customer(nid=info.nid, name=info.name))
        new_account = Account(self.bank, customer)

        self.accounts[new_account.account_number] = new_account
        if customer.nid not in self.customers:
            self.customers[customer.nid] = customer

        self.deposit(new_account.account_number, info.initial_amount)

        return (new_account.account_number, new_account.balance)

    def delete_account(self, account_number: str) -> Decimal:
        self._validate_account_number(account_number)
        
        account_balance = self.accounts[account_number].balance
        del self.accounts[account_number]
        # TODO: Remove account from customer account list
        return account_balance

    def deposit(self, account_number: str, amount: Decimal) -> Decimal:
        self._validate_account_number(account_number)

        account = self.accounts[account_number]
        account.deposit(amount)

        return account.balance

    def withdraw(self, account_number: str, amount: Decimal) -> Decimal:
        self._validate_account_number(account_number)
        account = self.accounts[account_number]
        did_happen = account.withdraw(amount)

        if not did_happen:
            raise Exception(
                f'Balance is low: {account.balance}, Valid withdraw amount: {account.withdraw_balance}',
                )
        
        return account.balance
    
    def get_balance(self, account_number: str) -> Decimal:
        self._validate_account_number(account_number)
        return self.accounts[account_number].balance

    
    def _validate_account_number(self, account_number) -> None:
        if account_number not in self.accounts:
            raise Exception('There is no account with this account number')
            


@dataclass
class InitialInfo:
    name: str
    nid: str
    initial_amount: Decimal
