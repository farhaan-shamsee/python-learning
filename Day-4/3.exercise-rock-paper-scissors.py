# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# # Write your code below this line 👇
#
# user_choice = int(input("Enter your choice: 0 for Rock, 1 for Paper and 2 for Scissors\n"))
#
# computer_choice = random.randint(0, 2)
#
# if user_choice == 0:
#     print(rock)
# if user_choice == 1:
#     print(paper)
# if user_choice == 2:
#     print(scissors)
#
# print("\nComputer chose:\n")
# print(computer_choice)
# if computer_choice == 0:
#     print(rock)
# if computer_choice == 1:
#     print(paper)
# if computer_choice == 2:
#     print(scissors)
#
#
# if user_choice == computer_choice:
#     print("\nDraw")
# elif user_choice > computer_choice:
#     if user_choice == 2 and computer_choice == 0:
#         print("\nyou loose")
#     else:
#         print("\nYou won")
# else:
#     if user_choice == 0 and computer_choice == 2:
#         print("\nYou win")
#     else:
#         print("\nYou loose")

# The above code was written by me. The below code is the solution:
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
