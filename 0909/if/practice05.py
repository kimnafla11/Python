#3개의 양수중 가장 큰 값 출력
num1 = int(input("1. 양의 정수 입력 : "))#값을 받아서 int형변환
num2 = int(input("2. 양의 정수 입력 : "))
num3 = int(input("3. 양의 정수 입력 : "))

if num1>0 and num2>0 and num3>0:#양수 조건
    if num1>num2:#num1이 num2보다 클 때
        if num1>=num3:#num1이 num3보다 크거나 같을때
            print(num1)#num1출력
        else:#num1이 num3보다 작을때
            print(num3)#num3출력
    elif num2>=num3:#num2가 num3보다 크거나 같을 때
        print(num2)#num2출력
    else:#num2가 num3보다 작을때
        print(num3)#num3출력
else:#음수가 하나라도 있을때
    print("양의 정수를 입력하세요.")

