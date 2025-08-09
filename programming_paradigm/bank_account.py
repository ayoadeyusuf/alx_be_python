class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self,amount):
        account_balance = self.account_balance + amount
        return account_balance

    def withdraw(self,amount):
        account_balance = self.account_balance - amount
        return account_balance

    def display_balance(self):
        print(f"Account Balance: ${self.account_balance}")
