print("Welcome to the roller coaster")
height = int(input("What is your height in cm? : "))
bill = 0

if height > 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age? : "))
    if age < 12:
        bill = 5
        print("ticket for children is $5")
    elif age <= 18:
        bill = 7
        print("ticket for teens is $7")
    else:
        bill = 12
        print("ticket for adult is $12")
    want_photo = input("Do you want photo (Y/N): ")
    if want_photo == "Y":
        bill += 3
    print(f"Your final bill is: ${bill}")
else:
    print("sorry you can not ride the rollercoster!")
