secret_number = 7
string = input("Enter you name: ")
print("Hello "+ string + "!! Welcome to the number guessing game!")
value = int(input("Enter your guess: "))
count = 1
while (secret_number != value):
    if(value > secret_number):
        print("Uff!! Too high")
        value = int(input("Enter your guess: "))
        count = count+1
    elif(value < secret_number):
        print("Ooops!! Too low")
        value = int(input("Enter your guess: "))
        count = count +1
   
print("Congratulations "+ string)
print("Woohoo! You solved it in "+ str(count) +" attempts")

