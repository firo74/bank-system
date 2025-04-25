# DTO = Data Transfer Object

class Customer:
    def __init__(self, nid, name):
        self.__nid = nid
        self.name = name
        self.__accounts = {} # Navigator

    @property
    def nid(self):
        return self.__nid
    
    def add_account(self, account):
        self.__accounts[account.account_number] = account

    def get_account(self, account_number: str):
        return self.__accounts.get(account_number)


def main():
    c = Customer(name='ali', nid='1234')
    print(c.nid)

if __name__ == '__main__':
    main()