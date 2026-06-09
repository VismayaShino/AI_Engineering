#print numbers from 1 to 10
"""
count = 1
while count<= 100:
    print(count)
    count= count+1"""

#print numbers 100 to 1
"""
reverse_count = 100
while reverse_count >= 1:
    print(reverse_count)
    reverse_count = reverse_count-1
"""

#print multiplication table of n
"""
value = int(input("Enter the value: "))
i = 1
while i <= 10:
    answer = value * i
    print(answer)
    i = i+1
"""

#print elements using a loop
"""
values = [1,4,9,16,25,36,49,64,81,100]
i=0
while (i < len(values)):
    print(values[i])
    i = i+1
"""

#search the element
"""
search = (1,4,16,25,36,49.64,81,100)
x = int(input("Enter the value to be searched: "))
i =0
while(i < len(search)):
    if(search[i] == x):
        print("Found at index", i)
    i = i+1
"""
#continue
"""
i = 1
while i <= 10:
    if(i%2 == 0):
        i = i + 1
        continue
    print(i)
    i = i + 1"""

"""
#for loop
list = ["Vismaya","Meredith","Meow"]
for el in list:
    print(el)

tup = (1,3,12,27,16)
for values in tup:
    print(values)"""

"""
str = "Meredith"
for letter in str:
    if(letter =="t"):
        print("t found")
        break 
    print(letter)
else:
    print("end")"""

tup =(1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the value:"))
for val in tup:
    if (val == x):
        print("val found")
        break
else:
    print("end")

    




