import random

attempts = 0

def set_difficulty():
    global attempts
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == 'easy':
        # attempts = 10
        return 10
    elif level == 'hard':
        # attempts = 5
        return 5

def check_answer(guess_number, chosen_number, attempts):
    if guess_number == chosen_number:
        print(f"You got it! The answer was {chosen_number}")
        # attempts = 0
    else:
        if guess_number > chosen_number:
            print("Too high\nGuess again")
        elif guess_number < chosen_number:
            print("Too low\nGuess again")
        return attempts - 1

def game():
    print("Welcome to the Number Guessing Game!\n")
    print("I am thinking of a number between 1 and 100.\n")
    chosen_number = random.randint(1, 100)
    attempts = set_difficulty()
    guess_number = 0
    while guess_number != chosen_number:
        print(f"You have {attempts} remaining to guess the number. \n")
        guess_number = int(input("make a guess: "))
        attempts = check_answer(guess_number, chosen_number, attempts)
        if attempts == 0:
            print("You have run out of attempts. You loose")
            return
    
game()


