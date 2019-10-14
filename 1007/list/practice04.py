#연습문제 2를 참고하여 max(), min()사용하지 않고 최대최소 구하기
#사용자가 입력한 데이터 리스트에 저장

numList = list()#사용자가 입력한 값을 저장할 배열
for n in range(1,6): # 1부터 5까지 반복
    print(n,end = " ") 
    num= int(input("번째 숫자 : "))#사용자로부터 숫자 받음
    numList.append(num) #받은 숫자를 배열에 저장
numList.sort()#오름차순으로 정렬
print("최대값 : ",numList[-1]) #인덱스번호로 최대값 호출
print("최소값 : ",numList[0]) #인덱스번호로 최소값 호출
