#사용자에게 5개의 정수를 입력받고 역으로 출력
#사용자가 입력한 데이터 리스트에 저장
numList = list()#사용자가 입력한 값을 저장할 배열
for n in range(1,6): # 1부터 5까지 반복
    print(n,end = " ") 
    num= int(input("번째 숫자 : "))#사용자로부터 숫자 받음
    numList.insert(-n,num) #받은 숫자를 배열에 저장

print(numList)
