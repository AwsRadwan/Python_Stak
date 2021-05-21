class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("user_name :", self.name, ":", "Balance :", self.account_balance)
        return self
    def  transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Aws = User("Aws", "aws.g")
Ali = User("Ali", "ali.g")
# print(Aws.name)
Aws.make_deposit(1000).make_withdrawal(300)
Ali.make_deposit(1000).make_withdrawal(200)
# print(Ali.account_balance)
Aws.transfer_money(Ali, 200)
Ali.display_user_balance()
Aws.display_user_balance()



