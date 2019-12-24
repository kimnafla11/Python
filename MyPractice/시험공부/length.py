#사용자 두 점의 좌표 (x1, y1)(x2,y2)받아 두점사이 거리 계산
#((x1-x2)**2+(y1-y2)**2)**(1/2)

x1 = int(input('x1 : '))
y1 = int(input('y1 : '))
x2 = int(input('x2 : '))
y2 = int(input('y2 : '))
length = ((x1-x2)**2+(y1-y2)**2)**(1/2)
print('두 점의 거리 : ',length)
