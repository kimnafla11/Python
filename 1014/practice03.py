#전화번호부 프로그램
#사용자가 q를 입력할때까지 이름과 전화번호를 입력받아 저장하고 이름으로 전화번호 검색

class Book:#클래스 생성
    def __init__(self):
        self.address ={}#address라는 딕셔너리 만듦
    def setName(self,name):
        self.address[name] = []#name을 받아 address의 키값으로 설정
    def setPhone(self,name,phone):
        self.address[name].append(phone)#phone을 받아 name이 키인 address의 value로 설정
        
print('이름과 전화번호를 입력하시오')
b1 = Book()#인스턴스 생성
while(True):
    name = input("이름 : ")
    if(name !='q'):#q가 아니면 if문 실행
        phone = input("전화 : ")
        b1.setName(name)#b1인스턴스에 setName실행
        b1.setPhone(name,phone)#b1인스턴스 setPhone실행
    else:
        break#q이면 반복문 종료

print('전화번호 입력종료')

while(True):
    inputName = input("검색 할 이름 : ")
    if(inputName in b1.address): #inputName이 b1인스턴스 address에 있따면..
        print(b1.address[inputName])#value출력
    else:
        print("이름이 없습니다.")
