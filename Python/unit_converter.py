print("Unit converter")
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