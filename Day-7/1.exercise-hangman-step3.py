"""
#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
            letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

guess = input("Guess a letter: ").lower()

#Check guessed letter
for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

print(display)
"""
import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# guess = (input("Guess a letter:\n")).lower()

print(f'Pssst, the solution is {chosen_word}.')
display = []
for letters in chosen_word:
    display.append("_")

# added the while loop here as part of step 3
while '_' in display:
    guess = (input("Guess a letter:\n")).lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    print(display)

print("You won")
