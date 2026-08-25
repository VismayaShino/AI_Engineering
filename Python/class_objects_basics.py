"""
#basic structure of a class nad object
class Student:
    name = "Vis"
#here python automatically calls the __init__ fucntion and runs it 
s1 = Student()
#this parenthisis is used to call the constructor
print(s1.name)

----------------------------------------------------------------------------------

class Cars:
    def __init__(self,fullname):
        self.name = fullname
        print(self)
#self is the parameter of init fucntion
#here self is c1 ..as it is the newly created object

c1 = Cars("Karan ")
print(c1.name)

-----------------------------------------------------------------------------------"""
"""class Student:
    college_name = "JSPM"
    #parameteriezed constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        #self.attribute = parameter

    def addition(self):
        val1 = int(input("Enter val1: "))
        val2 = int(input("Enter val2: "))
        print(val1 + val2)

    def hello(self):
        print("Hello",self.name)

s1 = Student("Vis",25)
#object.attribute
print(s1.name)
print(s1.marks)
s1.hello()

s2 = Student("Rut",21)
print(s2.name, s2.marks)
s2.addition()

-----------------------------------------------------------------------------------"""
"""
class Cars:
    def __init__(self, name , engine):
        self.name = name
        self.engine = engine
    
c1 = Cars("P1","V8")
print(c1.name)
-----------------------------------------------------------------------------------"""

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        #now because of __ acc_pass is a private attribute
        self.__acc_pass = acc_pass

    def display_details(self):
         print("Your account number is: ",self.__acc_pass)

a1 = Account("1234","rutvik")
print(a1.acc_no)
print(a1.display_details())


class Intro:
    __name = "anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = Intro()
p1.welcome()


    



