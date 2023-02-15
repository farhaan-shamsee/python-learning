"""
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2-digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
"""
name1 = input("Enter name 1: ").lower()
name2 = input("Enter name 2: ").lower()

name = name1 + name2


count_true_name = name.count("t") + name.count("r") + name.count("u") + name.count("e")
count_false_name = name.count("v") + name.count("o") + name.count("l") + name.count("e")

total_score = int(f"{count_true_name}"f"{count_false_name}")

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 < total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
