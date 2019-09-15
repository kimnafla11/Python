buyPrice = int(input("구입금액을 입력하시오: "))
if buyPrice>=100000:
    print("최종금액")
    buyPrice = buyPrice*0.95
    #dcPrice = buyPrice*0.95
    #print("지불금액은 %f 입니다."%dcPrice)
print("최종금액 : %d" %buyPrice)
