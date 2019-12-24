class Car:
    def __init__(self, speed,color, model):
        self.speed = speed
        self.color = color
        self.model= model

    def faster(self,speed):
        return speed+10
    def gia(self, gia):
        return gia+1
    def __str__(self):
        msg = "속도 :"+str(self.speed)+" 색상 : "+self.color+" 모델 : "+self.model
        return msg

myCar = Car(10,'white','소렌토')
print(myCar)
print(myCar.faster(10))
