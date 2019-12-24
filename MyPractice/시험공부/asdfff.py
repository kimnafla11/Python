class bank:
    def __init__(self):
        self.money = 0
    def withdraw(self,x):
        return x
    def deposit(self,x):
        return x
balance = bank()
print(balance.withdraw(100))
print(balance.deposit(10))
