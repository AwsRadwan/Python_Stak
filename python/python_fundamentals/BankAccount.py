class BankAccount:
    def __init__(self, balance=0, int_rate=0.05):
        self.account_balance = balance
        self.interest_rate = int_rate
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print("Balance :", "$",self.account_balance, ",", "interest_rate",self.interest_rate)
        return self
    def yield_interest(self):
        self.account_balance = self.account_balance*(1+self.interest_rate)
        return self

account1 = BankAccount()
account2 = BankAccount()
account1.deposit(100).deposit(600).deposit(300).withdraw(300).yield_interest().display_account_info()
account2.deposit(400).deposit(600).withdraw(50).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()



