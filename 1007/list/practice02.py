#사용자가 정수 3개 입력하면 정수 합계 구하는 코드
#입력된 숫자는 리스트에 저장
#반복문은 for문 사용

numList = list()#사용자가 입력한 값을 저장할 배열
sum = 0#배열의 합을 저장할 변수 초깃값
for n in range(1,4): # 1부터 3까지 반복
    print(n,end = " ") 
    num= int(input("번째 숫자 : "))#사용자로부터 숫자 받음
    numList.append(num) #받은 숫자를 배열에 저장
for x in range(len(numList)): #배열 길이 만큼 반복
    sum +=numList[x] #sum변수에 배열 값 모두 더함
print("합계 : ",sum)
