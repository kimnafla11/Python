#커피자판기
print('***** 커피 자판기가 동작합니다 *****')
machine = {'커피': 10, '물':10, '설탕': 10}
while True:
    menu = input('메뉴를 눌러주세요 1.에스프레소, 2.아메리카노, 3.설탕커피, 4.잔량보기 5.채우기')
    if menu == '1':
        if machine['커피']>0 and machine['물']>0:
            machine['커피'] = machine['커피']-1
            machine['물'] = machine['물']-1
            print('에스프레소 나왔습니다.')
        else:
            print('원료가 부족합니다.')
    elif menu == '2':
        if machine['커피']>0 and machine['물']>1:
            machine['커피'] = machine['커피']-1
            machine['물'] = machine['물']-2
            print('아메리카노 나왔습니다.')
        else:
            print('원료가 부족합니다.')
    elif menu == '3':
        if machine['커피']>0 and machine['물']>1 and machine['설탕']>0:
            machine['커피'] = machine['커피']-1
            machine['물'] = machine['물']-2
            machine['설탕'] = machine['설탕']-1
            print('설탕커피 나왔습니다.')
        else:
            print('원료가 부족합니다')
    elif menu == '4':
        for i in machine:
            print(i, machine[i],',',end = '')
        print()
    elif menu =='5':
        for i in machine:
            machine[i] = 10
    
