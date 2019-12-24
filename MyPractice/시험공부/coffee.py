class Machine:
    def __init__(self,coffee,water,sugar):
        self.coffee= coffee
        self.water = water
        self.sugar = sugar
    def esspresso(self):
        if (self.coffee>0 and self.water>0):
            print('에스프레소 나왔습니다')
            self.coffee = self.coffee-1
            self.water = self.water-1
            return self.coffee, self.water
        else:
            print('원료 부족')
    def americano(self):
        if(self.coffee>0 and self.water>1):
            print('아메리카노 나왔습니다')
            self.coffee = self.coffee-1
            self.water = self.water-2
            return self.coffee, self.water
        else:
            print('원료 부족')
    def sugarcoffee(self):
        if(self.coffee>0 and self.water>1 and self.sugar>0):
            print('설탕커피 나왔습니다')
            self.coffee = self.coffee-1
            self.water = self.water-2
            self.sugar = self.sugar-1
            return self.coffee, self.water, self.sugar
        else:
            print('원료 부족')
    def info(self):
        print('커피 {}, 물 {}, 설탕 {}' .format(self.coffee, self.water, self.sugar))

print('*****커피자판기*****')
machine = Machine(10,10,10)
while True:
    menu = input('1.에스프레소 2.아메리카노 3.설탕커피 4.잔량보기 5.원료 채우기')
    if menu == '1':
        machine.esspresso()
    elif menu == '2':
        machine.americano()
    elif menu =='3':
        machine.sugarcoffee()
    elif menu == '4':
        machine.info()
    elif menu == '5':
        machine = Machine(10,10,10)
