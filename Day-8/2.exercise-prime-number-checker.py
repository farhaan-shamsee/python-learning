# Write your code below this line 👇
import math


def prime_checker(number: int):
    is_prime = True
    if n <= 1:
        is_prime = False
    elif n == 2 or n == 3:
        is_prime = True
    elif n % 2 == 0 or n % 3 == 0:
        is_prime = False
    else:
        for i in range(5, int(math.sqrt(number)+1), 6):
            if n % i == 0 or n % (i+2) == 0:
                is_prime = False

    if is_prime is True:
        print("It's a prime number")
    else:
        print("It's not a prime number")
# Write your code above this line 👆

# Do NOT change any of the code below👇


n = int(input("Check this number: "))
prime_checker(number=n)
