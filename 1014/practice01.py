#사람 정보를 간단하게 표현하는 클래스
class Person: #Person클래스 생성
    def __init__(self, name, age): #나이와 이름을 받는 생성자
        self.name = name
        self.age = age
    def inputName(self,name): #이름을 입력하는 inputName 메소드
        self.name = name #입력한 name값을 객체에 저장
    def inputAge(self,age):
        self.age = age #입력한 age값을 객체에  저장
    def introduce(self):#이름과 나이를 출력하는 introduce메소드
        print("이름은 %s 이고 나이는 %d 살 입니다" %(self.name, self.age))

mike = Person("Mike", 26)#miks객체 생성 이때 name은 Mike, age는 26임
mike.inputAge(28)#mike객체에 inputAge메소드실행 매개변수는 28
mike.introduce()#mike객체에 introduce메소드 실행
