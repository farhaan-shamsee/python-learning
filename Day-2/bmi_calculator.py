# Taking values from user
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Calculating BMI
bmi = int(weight)/(float(height)*float(height))
bmi = int(bmi)
print("Your BMI is: " + str(bmi))
