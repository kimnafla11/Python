#수를 입력받아 그 수가 짝수인지 홀수인지 판별
#while문 무한루프 사용
#0을 입력하면 exit출력 break로 무한루프로 탈출
#5,2,3 숫자를 각각 입력해 테스트
while True:#무한루프
    num = int(input("Enter the number : "))#값 받음
    if num%2!=0 :#짝수일때
                print(num,"is odd number")
    elif num==0 :#0을받았을때 무한루프 나감
        print("EXIT")
        break
    else:
        print(num,"is even number")
