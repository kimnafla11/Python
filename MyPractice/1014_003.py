class Service:
    secret = "나는 고추가 작다"
    def __init__(self,age):#__init__함수를 사용했기때문에 인스턴스 생성할때 꼭 age써야됨
        self.age = age
    def setname(self, name):
        self.name = name
    def sum(self,a,b): #무조건self로 사용해야 인스턴스의 함수로 사용할 수 있음
        result = a+b
        print(self.name,"님",a,"+",b,"=",result, " 입니다")
pey = Service(25)#인스턴스생성할떄 __init__때문에 꼭 변수 써줘야됨
print(pey.secret)
my = input("이름 : ")
pey.setname(my)#setname에 변수 저장
pey.sum(1,2)