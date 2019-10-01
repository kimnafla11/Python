#for문과 while문의 중첩을 사용하여 별 1개씩 증가하며 5개까지 찍기
num = 0 #초기화
while num <5:#줄바꿈을 위한 while문 5줄
    num+=1
    print()#줄바꿈
    for x in range(num):#for문을 사용하여 별 num개씩 찍으며 반
        print("*",end = " ")
