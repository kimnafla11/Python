#소유하는 돈과 사탕의 가격을 받아 연산하도록
myMoney = int(input("현재 소지하고 있는 금액 : "))
#input은 문자형을 가지고 오기때매 int형변환을 해주어야한다.
price = int(input("구매하려는 물건의 가격 : "))
print("물건의 최대 구매 가능 개수 : ", myMoney//price)
print("구입하고 남은 금액 : ", myMoney%price)
