#한개 정수 입력 받고 적절한 것 출력
num = int(input("정수를 입력하세요 : "))#숫자 받음 int형으로 변환
if num>=20 and num<30 :#범위 지정
    print("입력한 값은 20이상 30 미만입니다.")
elif num>=10 and num <20 :
    print("입력한 값은 10이상 20 미만입니다.")
elif num >= 0 and num<10 :
    print("입력한 값은 0이상 10 미만입니다.")
elif num < 0 :#음수일때 조건
    print("입력한 값은 0보다 작습니다.")
elif num >=30:#30보다 큰 수 일때
    print("입력한 값은 30이상입니다.")
