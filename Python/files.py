"""Create a new file and add data

with open("sample.txt", 'w') as f:
    f.write("Hi everyone.\nWe are learning file I/O\n")
    f.write("Using java.\nI like programming in java.")
    f.close()

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
    f.close()

---------------------------------------------------------"""

"""Replace all occurances of java with python

with open("sample.txt", "r") as f:
    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)

with open("practice.txt" , "w") as f:
    f.write(new_data)

---------------------------------------------------------"""

"""Search if the word "learning" exists in the file

with open("sample.txt", "r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("word found")
    else:
        print("word not found")
        f.close()
---------------------------------------------------------"""

"""Search when the word "learning" occurs first in the file
word = "vis"
data = True
count = 1
with open("sample.txt", "r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(count)
        count = count + 1
    else:
        print("-1")
---------------------------------------------------------"""

"""from a file containing numbers separated by comma, print the count of the even numbers

with open("numbers.txt", "r") as f:
    data = f.read()
    # print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            if int(num) % 2 == 0:
                print(num)
            num = ""
        else:
            num += data[i]
    if int(num) % 2 == 0:
        print(num)

---------------------------------------------------------"""
