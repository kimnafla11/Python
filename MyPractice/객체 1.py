class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def inputName(self,name):
        self.name=name
    def inputAge(self,age):
        self.age=age
    def introduce(self):
        print('이름은 {} 나이는 {}살 입니다' .format(self.name, self.age))
mike= Person('mike',26)
mike.inputName('mike')
mike.inputAge(28)
mike.introduce()
