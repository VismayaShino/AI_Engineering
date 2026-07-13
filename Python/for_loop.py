"""#print elements using for
elements = [1,4,9,16,25,36,49,64,81,100]

for el in elements:
    print(el)

#search an element
values = (1,4,9,16,25,36,49,64,81,100)
value1 = int(input("Enter the value to be searched: "))

i=0
for val in values:
    if(value1 == values[i]):
        print("Value found at index "+ str(i+1))
        break
    else:
        i = i+1

#range function
for i in range(10):
    print(i) 

#print even numbers using range
for i in range(2,10,2):
    print(i)

for i in range(10,0,-1):
    print(i)"""

#multiplication table
val = int(input("Enter the value: "))

for i in range(1,11):
    ans = (val*i)
    print(ans)


