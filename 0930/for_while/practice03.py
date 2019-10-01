#0을 입력하면 입력은 종료가 되고 앞서 입력한 숫자를 더하여 출력
#while문 이용
#음수 포함
sum = 0 #총 합
print("종료하려면 0 입력")
while True:#무한루프 생성
    num = int(input(""))#사용자로부터 값 받음
    sum +=num#총합 구함
    if num == 0:#사용자에게 받은 값이 0일때 출
        print("총합은 ",sum,"입니다")
        break
