#Single Inheritance
"""class Car:                     #parent class
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")
#---------------------------------------------------------------------
class McLaren(Car):             #child class
    def __init__(self, brand):
        self.brand = brand

car1 = McLaren("Artura")
car1.start()"""

#______________________________________________________________________________

#Multi-level Inheritance
"""class Car:                     #parent class
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")
#---------------------------------------------------------------------
class McLaren(Car):             #child class
    def __init__(self, brand):
        self.brand = brand
#---------------------------------------------------------------------
class Artura(McLaren):                 #child class
    def __init__(self,type):
        self.type = type
#---------------------------------------------------------------------
car1 = Artura("Petrol")
car1.start()
car1.stop()"""

#______________________________________________________________________________

#Multiple Inheritance
"""
class CarModes:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def close():
        print("Car stopped...")

class Engine:
    def __init__(self,name):
        self.name = name

class Car(CarModes,Engine):
    def __init__(self, brand,name):
        self.brand = brand
        super().__init__(name)  #super class

c1 = Car("McLaren","V8")
print(c1.name)
c1.start()"""
#______________________________________________________________________________
#class method
"""class Person:
    name = "anonymous"

    @classmethod          #decorator
    def change(cls,name):
        cls.name = name
    
p1 = Person()
p1.change("ansh")
print(p1.name)"""
#______________________________________________________________________________

#percentage

""""class Student:
    def __init__(self,math,chem,phy):
        self.math = math
        self.chem = chem
        self.phy = phy 

    @property
    def percentage(self):
        return str((self.math+self.chem+self.phy)/3) + '%'

s1 = Student(98,99,96)
print(s1.percentage) 

s1.phy = 86
print(s1.percentage)"""
#______________________________________________________________________________



