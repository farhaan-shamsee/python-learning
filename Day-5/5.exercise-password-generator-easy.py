"""
Password Generator
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
"""
========================================================================================
My Answer:
========================================================================================

letters_req = input("How many letters would you like in your password?")
symbols_req = input("How many symbols would you like?")

numbers_req = input("How many numbers would you like?")

letters_pwd = ''
symbols_pwd = ''
numbers_pwd = ''

for n in range(0, int(letters_req)):
    letters_pwd = letters_pwd + letters[(random.randint(0, (len(letters)-1)))]


for n in range(0, int(symbols_req)):
    symbols_pwd = symbols_pwd + symbols[(random.randint(0, (len(symbols)-1)))]
for n in range(0, int(numbers_req)):
    numbers_pwd = numbers_pwd + numbers[(random.randint(0, (len(numbers)-1)))]

print(letters_pwd + symbols_pwd + numbers_pwd)
"""

"""
========================================================================================
Simpler Answer
========================================================================================
"""
password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)