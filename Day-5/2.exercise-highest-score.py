"""
You are going to write a program that calculates the highest score from a List of scores.
"""
student_score = input("Enter students scores: ").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])


highest_score = 0

for score in student_score:
    if score > highest_score:
        highest_score = score


print(highest_score)