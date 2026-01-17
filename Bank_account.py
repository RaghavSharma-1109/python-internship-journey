class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Current balance: {self.balance}")

acc = BankAccount("Raghav", 5000)
acc.deposit(2000)
acc.withdraw(10000)
acc.display_balance()

        