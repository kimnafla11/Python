r = int(input("원의 반지름 = ",))
class circle:
    def __init__(self):
        self.nul = 0
        self.dul = 0
    def nulbi(self, r):
        return r*r*3.14
    def dulle(self, r):
        return 2*r*3.14
cir1 = circle()
cir2 = circle()
print("원의 넓이 = ",cir1.nulbi(r))
print("원의 둘레 = ", cir2.dulle(r))