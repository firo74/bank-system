from decimal import Decimal

from services import AccountManager, InitialInfo, SMSSender, EmailSender
from models import Bank


def main():
    melli = Bank('Melli', Decimal('1'))
    saman = Bank('Saman', Decimal('100000'))

    am_melli = AccountManager(melli, [SMSSender('KaveNegar')])
    am_saman = AccountManager(saman, [SMSSender('SMS.ir'), EmailSender('saman_emails.txt')])

    print('Creating Accounts')
    my_account_number_1, _ = am_melli.create_account(InitialInfo('mohamamdali', '123', Decimal('5000000')))
    my_account_number_2, _ = am_melli.create_account(InitialInfo('mohamamdali', '123', Decimal('6000000')))
    my_account_number_3, _ = am_saman.create_account(InitialInfo('mohamamdali', '123', Decimal('200000')))

    print('Delete one of accounts')
    try:
        am_melli.delete_account(my_account_number_3)
    except Exception as e:
        print(e)

    my_balance_1 = am_melli.delete_account(my_account_number_1)
    print(f'Delete Successfully, balance = {my_balance_1}')
    am_melli.deposit(my_account_number_2, Decimal('1000'))
    
    print('Balance Exercise')
    print(am_saman.get_balance(my_account_number_3))
    am_saman.deposit(my_account_number_3, Decimal('200000'))
    print(am_saman.get_balance(my_account_number_3))
    am_saman.withdraw(my_account_number_3, Decimal('100000'))
    print(am_saman.get_balance(my_account_number_3))
    try:
        am_saman.withdraw(my_account_number_3, Decimal('1000000'))
    except Exception as e:
        print(e)
    print(am_saman.get_balance(my_account_number_3))
    try:
        am_saman.withdraw(my_account_number_3, Decimal('300000'))
    except Exception as e:
        print(e)
    print(am_saman.get_balance(my_account_number_3))


if __name__ == '__main__':
    main()