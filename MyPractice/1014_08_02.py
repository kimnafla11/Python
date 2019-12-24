#입출금 은행계좌 현재잔액(balance)만을 인스턴스 변수로 작성
#생성자와 인출메소드 withdraw(),입금 deposit()
class Bank:
    def __init__(self,money1,money2):#생성자
        self.money1 = money1
        self.money2 = money2

    def withdraw(self):
        print("통장에서",self.money1,"가 출금되었음")
    def deposit(self):
        print("통장에",self.money2,"가 입금되었음")


money1 = int(input("출금 얼마? "))
money2 = int(input("입금 얼마? "))
balance = Bank(money1,money2)
balance.withdraw()
balance.deposit()
