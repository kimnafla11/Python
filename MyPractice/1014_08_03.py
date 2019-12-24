class Car:
    def __init__(self,color,speed,kia):
        self.color = color
        
    def setKia(self,kia):
        self.kia = kia
    def setSpeed(self,speed):
        self.speed = speed
   # def getSpeed(self):
    #    return self.speed
    #def getKia(self):
     #   return self.kia

    def __str__(self):
        return "(%s,%d,%d)" %(self.color,self.speed,self.kia)
    
car1 = Car("white",100,3)
car1.setKia(4)
car1.setSpeed(120)
print(car1)
