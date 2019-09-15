#포도를 3송이 이상 구매 할 경우 총 결제금액에 10%할인
applePrice = 1000#과일의 값은 사용자가 수정 할 수 있도록 변수로 선언함
grapePrice = 3000
baePrice = 2000
gyeulPrice = 500

grapeNum = int(input("포도 몇개? : "))
appleNum = int(input("사과 몇개? : "))
baeNum = int(input("배 몇개? : "))
gyeulNum = int(input("귤 몇개? : "))

totalPrice = appleNum*applePrice + grapeNum*grapePrice + baeNum*baePrice + gyeulNum*gyeulPrice
#총가격을 계산

if grapeNum>=3 :#포도 3개 이상 샀을 경우
    totalPrice = totalPrice*0.9#10프로 할인 한 값을 총가격에 대입
    print("%d 원 입니다" %totalPrice)
else:
    print("%d 원 입니다" %totalPrice)
