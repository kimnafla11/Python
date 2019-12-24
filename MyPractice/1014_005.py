class HouseKim:
    b = "김"
    def setname(self,a):
        self.fullname = self.b+a
    def travel(self,c):
        print(self.fullname,", ",c,"여행감")
pey = HouseKim()
pey.setname("나은")
pey.travel("부산")

class HouseLim(HouseKim):
    b = "임"
    def travel(self,c,d):
        print(self.fullname,",",c,"에 ",d,"일 감")
pey1 = HouseLim()
pey1.setname("찬규")
pey1.travel("철원",600)