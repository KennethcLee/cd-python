class BankAccount:
    all_accounts = []

    def __init__(self, int_rate = 0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (BankAccount.can_withdraw(self.balance, amount)):
            self.balance -= amount
        return self

    def display_account_info(self):
        return self.balance

    def display_rate_info(self):
        print(f"{self.int_rate}")
        return self

    def yield_interest(self):
        if (BankAccount.account_positive(self.balance)):
            self.balance = round((self.balance * (1+self.int_rate)), 2)
        return self

    @classmethod
    def all_balance(cls):
        sum = 0
        for j in cls.all_accounts:
            sum += j.balance
        return sum

    def display_all_accounts():
        print(f"${BankAccount.all_accounts}")

    def display_all_balance():
        print(f"${round(BankAccount.all_balance(), 2)}")

    @staticmethod
    def account_positive(balance):
        if (balance >=0):
            return True
        else:
            return False

    def can_withdraw(balance, amount):
        if(balance >= amount):
            return True
        else:
            print("insufficent fund")
            return False

class User:
    all_accounts = {}
    def __init__(self, fname, lname, acctname="SAVING", init_rate=0.01, amount=0):
        self.fname = fname
        self.lname = lname
        if ''.join([fname, lname]) in User.all_accounts.keys():
            # print("YES")
            User.all_accounts[fname + lname][acctname] = BankAccount(init_rate, amount)
        else:
            User.all_accounts[fname + lname] = {acctname : BankAccount(init_rate, amount)}

    def displayUserBalance(self, acctname="SAVING"):
        if self.account_exist(acctname):
            print(f"{self.fname} {self.lname} {acctname} account has ${User.all_accounts[self.fname + self.lname][acctname].display_account_info()}")
        return self

    def make_withdrawal(self, acctname="SAVING", amount=0):
        if self.account_exist(acctname):
            User.all_accounts[self.fname + self.lname][acctname].withdraw(amount)
        return self

    def make_deposit(self, acctname="SAVING", amount=0):
        if self.account_exist(acctname):
            User.all_accounts[self.fname + self.lname][acctname].deposit(amount)
        return self

    def yield_interest(self, acctname="SAVING", amount=0):
        if self.account_exist(acctname):
            User.all_accounts[self.fname + self.lname][acctname].yield_interest()
        return self

    def transfer_money(self, amount, sAccount, dAccount):
        sAccount.account.withdraw(amount)
        dAccount.account.deposit(amount)
        return self

    def account_exist(self, acctname):
        if acctname in User.all_accounts[self.fname + self.lname].keys():
            return True
        else:
            print("Account does not exist")
            return False


peter = User("Peter", "Hong", "SAVING", 0.02, 50)
mary = User("Mary", "Lin", "SAVING", 0.03, 100)
joe = User("Joe", "Chang", "SAVING", 0.01, 1)
joe = User("Joe", "Chang", "IRA", 0.01, 100)
joe = User("Joe", "Chang", "CHECKING", 0.01, 10)

peter.make_deposit("SAVING",40).make_deposit("SAVING",100).make_deposit("SAVING",2000).make_withdrawal("SAVING",1).yield_interest().displayUserBalance()
mary.make_deposit("SAVING",30000).make_deposit("SAVING", 300).make_withdrawal("SAVING", 1).make_withdrawal("SAVING", 10).make_withdrawal("SAVING", 100).make_withdrawal("SAVING", 1000).yield_interest().displayUserBalance()
joe.make_deposit("SAVING",30000).make_deposit("CHECKING", 3000).make_deposit("IRA",2000).make_withdrawal("IRA", 1).make_withdrawal("IRA", 10).make_withdrawal("SAVING", 100).make_withdrawal("CHECKING", 1000).yield_interest("IRA").displayUserBalance().displayUserBalance("IRA").displayUserBalance("CHECKING")

BankAccount.display_all_balance()
BankAccount.display_all_accounts()
