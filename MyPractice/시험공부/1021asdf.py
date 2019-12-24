class Bank:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self,money1):
        self.money1 = money1
    def withdraw(self,money2):
        self.money2 = money2
    def __str__(self):
        return str(self.balance+self.money1-self.money2)
balance = int(input('통장 잔액 ? '))
money1 = int(input('입금 금액 ? '))
money2 = int(input('출금 금액 ? '))
bank = Bank(balance)
bank.deposit(money1)
print(money1,'입금')
bank.withdraw(money2)
print(money2,'출금')
print('잔액 ',bank)
