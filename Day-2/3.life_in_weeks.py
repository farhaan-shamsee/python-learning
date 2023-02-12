"""
Problem statement:
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90
years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
"""
current_age = int(input("What is your current age: "))

max_age = 90

age_left = max_age - current_age

age_left_in_weeks = age_left * 52
age_left_in_days = age_left * 365
age_left_in_months = age_left * 12

print(f"You have {age_left_in_days} days, {age_left_in_weeks} weeks, and {age_left_in_months} months left.")
