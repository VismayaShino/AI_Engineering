weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight/(height**2)
print("BMI = ",bmi)
if(bmi < 18.5 ):
    print("Category: Underweight")
elif(bmi >= 18.5 or bmi <= 24.9):
    print("Category: Normal")
elif(bmi >= 25 or bmi <= 29.9):
    print("Category: Overweight")
elif(bmi > 30):
    print("Category: Obese")
