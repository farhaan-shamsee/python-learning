import game_data
import art
import os
import random




def print_data(option_a, option_b):
    '''this prints the data in the format, taking input the options'''
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

def choose_players():
    '''randomly chooses a data set from the list of accounts'''
    return random.choice(game_data.data)

def check_count(option_a, option_b):
    '''checks the follower count of the supplied accounts'''
    if option_a['follower_count'] > option_b['follower_count']:
        return "A"
    else:
        return "B"
    

def game():
    score = 0
    print(art.logo)
    game_should_continue = True
    option_a = choose_players()
    option_b = choose_players()

    while game_should_continue:
        # replacing the options as option b always should go to option 1 after every round
        option_a = option_b
        option_b = choose_players()
        while option_a == option_b:
            option_b = random.choice(game_data.data)
        print_data(option_a, option_b)
        
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        actual_answer = check_count(option_a, option_b)

        os.system('clear')
        print(art.logo)
        if actual_answer == user_answer:
            score += 1
            print(f"You're right! Current score: {score}")
            # return score
            # game()
        else:
            game_should_continue = False
            # return is_answer_correct
            print(f"Sorry that was wrong. Final score {score}")


game()
