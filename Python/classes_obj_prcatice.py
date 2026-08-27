#------------------------------------------------------------------------------------------

"""class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        #marks1 = int(input("Enter marks of Maths: "))
        #marks2 = int(input("Enter marks of Chemistry: "))
        #marks3 = int(input("Enter marks of Physics: "))
        avg = (self.marks1 + self.marks2 + self.marks3)/3
        print("Hi",self.name,"The average of the marks are: ",avg)

s1 = Student("Vis",30,30,30)
s1.average()

s1.name = "Loki"
s1.average()"""
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
"""
class Account:
    def __init__(self,balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self):

        a = int(input("Enter amount to be debited: "))
        self.balance = self.balance - a
        print(self.balance)

    def credit(self):
        b = int(input("Enter amount to be credited: "))
        self.balance = self.balance + b
        print(self.balance)       

a1 = Account(10000,101)
a1.debit()
a1.credit()
"""
#------------------------------------------------------------------------------------------

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.answer = self.radius * self.radius * 3.14 
        print("The area of the circle is: ",self.answer,"m^2")

c1 = Circle(10)
c1.area()

class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("Your role is: ",self.role)
        print("Your department is: ",self.department)
        print("Your salary is: ",self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Your name is: ",self.name)
        print("Your age is: ",self.age)
        super().__init__("Cloud Engineer", "Cloud",50000)


e1 = Engineer("Vis",25)
e1.showdetails()





