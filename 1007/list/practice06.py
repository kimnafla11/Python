#1차부터 4차까지 치뤄지는 시험
#차수가 늘어날수록 반영비중이 10% 20% 30% 40% 늘어남
#합계

sList = list()#사용자가 입력한 값을 저장할 배열
sum = 0 #총 합을 저장할 변수 선언
for n in range(1,5): # 1부터 4까지 반복
    print(n,end = " ") 
    score = int(input("차 시험 : "))#사용자로부터 숫자 받음
    sList.append(score) #받은 점수를 배열에 저장
sum = int(sList[0]*0.1+sList[1]*0.2+sList[2]*0.3+sList[3]*0.4)  #가중치를 곱해서 sum에 저장
print("합계 : ",sum)
