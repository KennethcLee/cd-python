class User:
    def __init__(self, fname, lname, amount=0):
        self.fname = fname
        self.lname = lname
        self.amount = amount

    def displayUserBalance(self):
        print(f"{self.fname} {self.lname} has ${self.amount}")
        return self

    def verify_input(self, amount):
        if amount >= 0:
            return True
        else:
            print("incorrect amount")
            return False

    def verify_amount(self, amount, sAccount):
        if sAccount.amount >= amount:
            return True
        else:
            print("insufficent fund")
            return False

    def make_withdrawal(self, amount=0):
        if self.verify_input(amount):
            self.amount -= amount
        return self

    def make_deposit(self, amount=0):
        if self.verify_input(amount):
            self.amount += amount
        return self

    def transfer_money(self, amount, sAccount, dAccount):
        if self.verify_input(amount) and self.verify_amount(amount, sAccount):
            sAccount.amount -= amount
            dAccount.amount += amount
        return self

peter = User("Peter", "Hong", 30)
mary = User("Mary", "Lin", 100)
joe = User("Joe", "Chang")

peter.displayUserBalance()
mary.displayUserBalance()
joe.displayUserBalance()
mary.make_withdrawal(-50)

peter.displayUserBalance()
mary.displayUserBalance()
joe.displayUserBalance()
peter.make_deposit(40).make_deposit(10).make_deposit(33).make_withdrawal(50)

peter.displayUserBalance()
mary.displayUserBalance()
joe.displayUserBalance()
mary.make_deposit(32).make_deposit(49).make_withdrawal(11).make_withdrawal(28)

peter.displayUserBalance()
mary.displayUserBalance()
joe.displayUserBalance()
joe.make_deposit(145).make_withdrawal(31).make_withdrawal(59).make_withdrawal(12)

peter.displayUserBalance()
mary.displayUserBalance()
joe.displayUserBalance()
mary.transfer_money(10, mary, peter)

peter.displayUserBalance()
mary.displayUserBalance()
joe.displayUserBalance()
mary.transfer_money(1000, mary, peter)

peter.displayUserBalance()
mary.displayUserBalance()
joe.displayUserBalance()