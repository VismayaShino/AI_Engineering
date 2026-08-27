import random 
secret_number = random.randint(1,100)
string = input("Enter your name: ")
print("Hello " + string + " Welcome to the game!")

value = int(input("Enter your guess: "))
count = 0
while(secret_number != value):
    if(value > secret_number):
        print("Uh-Oh! Too high...Go down a bit..")

    elif(value < secret_number):
        print("Mann! Too low...")
    value = int(input("Enter your guess: "))
    count = count + 1

print("Congratulations "+ string)
print("Woohoo! You solved it in "+ str(count) +" attempts")