#3개의 숫자를 받아 평균 계산 결과 출력
firstNum = int(input("첫번째 숫자를 입력하시오 : "))#input으로 문자형 받아서 int형변환
secondNum = int(input("두번째 숫자를 입력하시오 : "))
thirdNum = int(input("세번째 숫자를 입력하시오 : "))
average = (firstNum+secondNum+thirdNum)//3#정수로만 출력될 수 있게 //사용
print("%d %d %d 의 평균은 %d 입니다" %(firstNum, secondNum, thirdNum, average))
#문자열의 출력

