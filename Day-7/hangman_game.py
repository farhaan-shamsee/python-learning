import random
import hangman_words
import hangman_arts

print(hangman_arts.logo)
word_list = hangman_words.word_list

chosen_word = random.choice(word_list)  # choosing a random word from word_list
word_length = len(chosen_word)


lives = 6
end_of_game = False
previous_guess = []

print(f'Pssst, the solution is {chosen_word}.')
display = []
for letters in chosen_word:  # adding number of blanks equal to length of chosen word
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in previous_guess:
        print("You have already guessed: " + guess)
        print(f"{' '.join(display)}")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            print("You guessed " + guess + ", that's not in the word. Yoy loose a life")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You win.")
    previous_guess += guess

    print(hangman_arts.stages[lives])
