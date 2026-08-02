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

"""Recursion
def recursion(n):
    if(n==0 or n==1):
        return 1
    else:
        return recursion(n-1) * n
print(recursion(5))

------------------------------------------------------------"""

"""Sum of first n natural numbers
def summation(n):
    if(n==0):
        return 0
    else:
        return n + summation (n-1)
print(summation(10))

------------------------------------------------------------"""

"""Print all elememnts in a list"""
def print_list(list):
    if((len(list)) == 0):
        return 0
    else:
        return list
print(print_list([1,2,3,4,5]))

