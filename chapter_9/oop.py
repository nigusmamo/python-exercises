class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("\n\nperson name is: ",self.name ,"and age :",self.age)
c1 = Person("mehari",30)
c2 = Person("nigus",20)
c1.display()
c2.display()
