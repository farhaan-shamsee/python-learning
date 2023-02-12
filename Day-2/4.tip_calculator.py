print("Welcome to  the tip calculator")

total_bill = float(input("What was the total bill?: $"))

tip_percentage = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))

total_bill_with_tip = total_bill + (total_bill * (tip_percentage/100))

number_of_persons = int(input("How many people to split the bill? "))

final_bill = round((total_bill_with_tip/number_of_persons), 2)

print(f"Each person should pay: ${final_bill}")
