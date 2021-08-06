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
    def __init__(self, fname, lname, init_rate=0.01, amount=0):
        self.fname = fname
        self.lname = lname
        self.account = BankAccount(init_rate, amount)

    def displayUserBalance(self):
        print(f"{self.fname} {self.lname} has ${self.account.display_account_info()}")
        return self

    def make_withdrawal(self, amount=0):
        self.account.withdraw(amount)
        return self

    def make_deposit(self, amount=0):
        self.account.deposit(amount)
        return self

    def yield_interest(self, amount=0):
        self.account.yield_interest()
        return self

    def transfer_money(self, amount, sAccount, dAccount):
        sAccount.account.withdraw(amount)
        dAccount.account.deposit(amount)
        return self

peter = User("Peter", "Hong", 0.02, 50)
mary = User("Mary", "Lin", 0.03, 100)
joe = User("Joe", "Chang", 0.01, 1)
joe = User("Joe", "Chang", 0.03, 100)

peter.displayUserBalance()
joe.displayUserBalance()
joe.displayUserBalance()

peter.make_deposit(40).make_deposit(100).make_deposit(2000).make_withdrawal(1).yield_interest().displayUserBalance()
mary.make_deposit(30000).make_deposit(300).make_withdrawal(1).make_withdrawal(10).make_withdrawal(100).make_withdrawal(1000).yield_interest().displayUserBalance()
joe.displayUserBalance()

BankAccount.display_all_balance()
BankAccount.display_all_accounts()

