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
        print(f"{self.balance}")
        return self

    def display_rate_info(self):
        print(f"{self.int_rate}")
        return self

    def yield_interest(self):
        if (BankAccount.account_positive(self.balance)):
            self.balance *= (1+self.int_rate)
        return self

    @classmethod
    def all_balance(cls):
        sum = 0
        for j in cls.all_accounts:
            sum += j.balance
        return sum

    def display_all_balance():
        print(BankAccount.all_balance())

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

peter = BankAccount(0.02, 100)
mary = BankAccount()

peter.display_account_info()
peter.display_rate_info()
mary.display_account_info()
mary.display_rate_info()

peter.deposit(100).deposit(50).deposit(1000).withdraw(3)
peter.display_account_info()

mary.deposit(20).deposit(2000).withdraw(5).withdraw(50).withdraw(500).withdraw(1)
mary.display_account_info()

mary.withdraw(10000)

BankAccount.display_all_balance()