"""
Sum of two numbers

def calc_sum(a,b):
    return a+b

sum = calc_sum(2,7)
print("The sum is: ",sum)

------------------------------------------------------------"""

"""Average


a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
def average(a,b,c):
    sum = a+b+c
    ans = sum/3
    return ans

output = average(a,b,c)
print("The average of the entered values is ",output)

------------------------------------------------------------"""

"""Length of List

values = [1,2,3,6,5,7]
family = ["Rut","Vis"]
def list_length():
    return len(values)
output = list_length()
print(output)
print(type(values))
print(type(output))

def print_list(list):
    print(len(list))
    for el in list:
        print(el , end = " ")

print_list(values)
print_list(family)

------------------------------------------------------------"""

"""Factorial

def factorial(n):
    fact = 1
    i = 1
    while(n >= i):
        fact = fact * i
        i = i+1
    return print("The Factorial of",str(n), "is: ",fact)

n = int(input("Enter the value: "))
output = factorial(n)

------------------------------------------------------------"""

"""Unit converter"""
print("MENU\n1. Celsius → Fahrenheit\n2. Fahrenheit → Celsius\n")
choice = int(input("Enter your choice: "))

if(choice == 1):
    def unit_converter(value):
        print("Converting temperature to Farenheit...")
        farenheit = (value * 1.8) +32
        return farenheit
    value = int(input("Enter temperature in celsius: "))
    farenheit = unit_converter(value)
    print(farenheit)

elif(choice == 2):
    def unit_converter(value):
        print("Converting temperature to Celsius...")
        celsius = (value - 32) * (5/9)
        return celsius
    value = int(input("Enter temperature in farenheit: "))
    celsius = unit_converter(value)
    print(celsius)


else:
    print("Invalid Choice")
