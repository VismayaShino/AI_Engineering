#print elements using for
elements = [1,4,9,16,25,36,49,64,81,100]

for el in elements:
    print(el)

#search an element
values = [1,4,9,16,25,36,49,64,81,100]
value1 = int(input("Enter the value to be searched: "))

i=0
for val in values:
    if(value1 == values[i]):
        print("Value found at index "+ str(i+1))
        break
    else:
        i = i+1
