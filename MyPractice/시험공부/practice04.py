#전화번호부 프로그램
#사용자가 q를 입력할때까지 이름과 전화번호를 입력받아 저장하고 이름으로 전화번호 검색

class Book:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def setName(self,name):
        self.name = name
    def setPhone(self,phone):
        self.phone = phone
    def getPhone(self,name):
        if(self.name == name):
            return self.phone
        
print('이름과 전화번호를 입력하시오')

while(True):
    name = input("이름 : ")
    if(name !='q'):
        phone = input("전화 : ")
        b1 = Book(name, phone)
    else:
        break

print('반복종료')
inputName = input("이름 : ")
print(b1.getPhone(inputName))
