class FourCal:
    def setdata(self, a,b):#setdata로 값을 받음
        self.a = a
        self.b = b
    def sum(self):
        return self.a+self.b#함수 안에서 쓰이는 변수는 self.변수명
    def mul(self):
        return self.a*self.b
    def sub(self):
        return self.a-self.b
    def div(self):
        return self.a/self.b
x = FourCal()
x.setdata(10,2)
print(x.a)
print(x.b)
print(x.sum())