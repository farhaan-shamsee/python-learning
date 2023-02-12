# Operators in Python

## Floor Division
The floor division operator (//) is used to perform division where the result is rounded 
down to the nearest whole number. This is also known as integer division or division that
returns an integer, since the result will always be an **integer** even if the division would
normally result in a fraction.

## Round Function
The `round` function in Python is used to round a floating-point number to a specified number of 
decimal places.

```python
round(number, ndigits)
```

where `number` is the floating-point number that you want to round and `ndigits` is an optional argument 
that specifies the number of decimal places to which you want to round the number. 
If `ndigits` is not specified, round will round the number to the nearest whole number.

## F-String
Used to convert the datatypes to string. It provides a convenient way to embed 
expressions inside string literals, using {} brackets to evaluate expressions. 
The letter "f" before the string indicates that the string is an f-string.

## Life in weeks problem:

### Problem statement:
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 
90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input:
56

Output: You have 12410 days, 1768 weeks, and 408 months left.

Solution is [here](./3.life_in_weeks.py)

## Tip Calculator

### Problem Statement:
Ask for total bill and percentage of tip to be given, later split the bill among total persons and 
show the amount to be paid by each person

### Sample Run:

```
    Welcome to  the tip calculator
    What was the total bill?: $124.56
    What percentage of tip would you like to give? 10, 12, or 15? 12
    How many people to split the bill? 7
    Each person should pay: $19.93
```
