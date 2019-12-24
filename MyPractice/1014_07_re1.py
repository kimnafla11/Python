#1과 100사이의 3과 5의 공배수
#리스트에 저장 후 개수도 출력
cm_list = list()
for n in range(1,101):
    if(n%3 ==0)and(n%5==0):
        cm_list.append(n)
print("3과 5의 공배수 ",cm_list)
print("개수 ",len(cm_list))