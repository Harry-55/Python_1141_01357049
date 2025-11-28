class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
    def get_balance(self):
        print(f"{self.balance:.0f}")

accounts = {}

while True:
    x = input().strip().split()
    cmd = x[0]
    if cmd == "create":
        name = x[1]
        amount = float(x[2])
        accounts[name] = BankAccount(name, amount)
    elif cmd == "deposit":
        name = x[1]
        amount = float(x[2])
        if name not in accounts:
            print("Account not found")
            continue
        accounts[name].deposit(amount)
    elif cmd == "withdraw":
        name = x[1]
        amount = float(x[2])
        if name not in accounts:
            print("Account not found")
            continue
        accounts[name].withdraw(amount)
    elif cmd == "balance":
        name = x[1]
        if name not in accounts:
            print("Account not found")
            continue
        accounts[name].get_balance()
    elif cmd == "stop":
        break
    else:
        print("Invalid command")
