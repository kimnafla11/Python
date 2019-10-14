#사용자에게 5개의 정수 입력 받고 최대값 최소값 출력
#사용자 입력값은 리스트 저장
#max(), min()함수 사용
numList = list() #리스트 선언
for n in range(1,6): # 1부터 5까지 반복
    print(n,end = "")
    num = int(input("번째 숫자 : "))
    numList.append(num)#받은 값을 리스트에 저장
print("최대값 : ", max(numList))#max()함수를 활용해 최대값 구함
print("최소값 : ",min(numList))#min()함수를 활용해 최소값 구함
