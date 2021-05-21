class BankAccount:
    def __init__(self, balance=0, int_rate=0.05):
        self.account_balance = balance
        self.interest_rate = int_rate
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print("Done")
        else:
            print("There is no enogh balance")
        return self
    def display_account_info(self):
        print("Balance :", "$",self.account_balance, ",", "interest_rate",self.interest_rate)
        return self
    def yield_interest(self):
        self.account_balance = self.account_balance*(1+self.interest_rate)
        return self


class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.account = BankAccount(balance = balance)
    def make_deposit(self, amount):
        self.account.deposit(1000)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(500)
        return self
    def display_user_balance(self):
        print("user_name :", self.name, ":", "Balance :", self.account.account_balance)
        return self
    def  transfer_money(self, other_user, amount):
        self.account.account_balance -= amount
        other_user.account.account_balance += amount
        return self

Aws = User("Aws", "awsr.email")
Aws.account.deposit(1000).display_account_info()
Aws.account.deposit(500).display_account_info()
Aws.display_user_balance()