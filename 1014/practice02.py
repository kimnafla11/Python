#커피자판기 제어
#커피, 물, 설탕 중 잔량이 부족하면 "원료가 부족합니다" 출력

class Coffee : #커피라는 클래스 생성
    esspreso = 10
    water = 10
    sugar = 10#클래스 변수 선언
    def __init__(self,esspreso,water,sugar): #원료들을 매개변수로 받음
        self.esspreso = esspreso
        self.water = water
        self.sugar = sugar
        
    def ep(self):#에스프레소 만드는 메소드
        if(Coffee.esspreso>=1 and Coffee.water>=1): #원료가 남았을때 실행
            Coffee.esspreso -=1#클래수변수 -1
            Coffee.water -=1
            self.esspreso=Coffee.esspreso#객체의 변수에 클래스변수 저장
            self.water = Coffee.water
            print('에스프레소 나옴')
        else:
            print("원료 부족")
        return self.esspreso, self.water
    
    def am(self):
        if(Coffee.esspreso>=1 and Coffee.water>=2):
            Coffee.esspreso -=1
            Coffee.water -=2
            self.esspreso = Coffee.esspreso
            self.water = Coffee.water
            print('아메리카노 나옴')
        else:
            print("원료 부족")
        return self.esspreso, self.water
    
    def su(self):
        if(Coffee.esspreso>=1 and Coffee.water>=2 and Coffee.sugar>=1):
            Coffee.esspreso -=1
            Coffee.water -=1
            Coffee.sugar -=1
            self.esspreso=Coffee.esspreso
            self.water = Coffee.water
            self.sugar = Coffee.sugar
            print('설탕커피 나옴')
        else:
            print("원료 부족")
        return self.esspreso, self.water, self.sugar

    def show(self):
        print("커피%d, 물%d, 설탕%d" %(Coffee.esspreso, Coffee.water, Coffee.sugar))#클래스변수 출력

    def full(self):
        Coffee.sugar =10#클래스변수의 값을 full로 채움
        Coffee.esspreso =10
        Coffee.water =10
        self.esspreso = Coffee.esspreso
        self.water = Coffee.water
        self.sugar = Coffee.sugar
        return self.esspreso, self.water, self.sugar



print('***** 커피자판기가 동작합니다*****')
while(True): #반복문
    num = int(input("메뉴를 눌러주세요(1:에스프레소, 2:아메리카노, 3: 설탕커피, 4: 잔량보기, 5: 채우기)"))
    cof = Coffee(10,10,10) #Coffee클래스에 cof객체 변수 10,10,10으로 생성
    if(num == 1): #if문에 따라 메소드 실행
        cof.ep()
    elif(num == 2):
        cof.am()
    elif(num == 3):
        cof.su()
    elif(num ==4):
        cof.show()
    elif(num ==5):
        cof.full()
