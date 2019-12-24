class Address:
    def __init__(self):
        self.address={}
    def setName(self, name):
        self.address[name] = []
    def setPhone(self,name, phone):
        self.address[name].append(phone)

add1 = Address()
while True:
    name = input('이름 : ')
    if name =='q':
        print('종료')
        break
    phone = input('전화 : ')
    add1.setName(name)
    add1.setPhone(name,phone)
print('검색 모드')
while True:
    findname = input('검색할 이름 : ')
    if findname in add1.address.keys():
        print(add1.address[findname])
