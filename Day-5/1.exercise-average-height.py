"""
Problem statement:
Calculate average height without using len() and sum() functions.
"""

student_height = input("Enter heights: ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])


sumOfHeight = 0
count = 0
for i in student_height:
    sumOfHeight = sumOfHeight + i
    count += 1

average_height = round(sumOfHeight/count)

print(average_height)


