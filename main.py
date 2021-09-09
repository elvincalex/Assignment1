import random
import sys
history = {0:''}
choices_dict = {"r": "Rock", "p": "Paper", "s": "Scissors"}
beats = {'r': 'p', 's': 'r', 'p': 's'}
choices = ["r", "p", "s"]
def play_again():
    while True:
        print("\n\nPlay another game?\nEnter y for Yes or n for No")
        print("\n--------------------------------")
        play_again_user_response = input("...")
        if (play_again_user_response == "y") or (play_again_user_response == "Y"):
            num_games_func()
            break
        if (play_again_user_response == "n") or (play_again_user_response == "N"):
            print("Are you sure you want to quit?\nEnter y to confirm")
            play_again_user_response_confirm = input("...")
            if (play_again_user_response_confirm == "y") or (play_again_user_response_confirm == "Y"):
                sys.exit()
            continue
        print("Error: Invalid input\nPlease enter y or n")

def result(initial_rounds_num, final_scores):
    print("\n--------------------------------")
    if final_scores[0] > final_scores[1]:
        print("Player Wins with score:"+ str(final_scores[0]) + "/"  + str(initial_rounds_num)+"\nComputer lost with a score of " + str(final_scores[1]) +"/"+str(initial_rounds_num) )
    elif (final_scores[0] < final_scores[1]):
        print("Computer Wins with a score of " + str(final_scores[1]) +"/"+str(initial_rounds_num)+"\nPlayer lost with score:"+ str(final_scores[0]) + "/"  + str(initial_rounds_num))
    else:
        print("Player and Computer have drawn at a score of " + str(final_scores[0]) + "/" + str( initial_rounds_num))
    while True:
        print("Enter the round which you need more information, to exit enter 99")
        round_check = input("..")
        if (round_check.isdecimal()):
            round_check = int(round_check)
            if(round_check==99):
                play_again()
            elif (round_check>0)or(round_check<=initial_rounds_num):
                uc = history[round_check]
                uc =list(uc)
                ucc=uc[0][1]
                cc=uc[0][0]
                outc=uc[0][2]
                print("Player choice:"+ucc+"\nComputer Choice:"+cc+"\n"+outc+" the round\n")

def game_run(rounds, scores):
    initial_rounds_num = rounds
    decrease_rounds = True
    i = 0
    while True:
        comp_choice = random.choice(choices)
        user_input = input("...")
        if (user_input not in choices):
            print("Enter a valid input")
            decrease_rounds = False
        else:
            decrease_rounds = True
            if (comp_choice == user_input):
                i = i + 1
                history[i] = {(choices_dict[comp_choice],choices_dict[user_input],'Tied')}
            elif comp_choice == beats[user_input]:
                i = i + 1
                scores[1] += 1
                history[i] = {(choices_dict[comp_choice], choices_dict[user_input],'Computer wins')}
            else:
                i = i + 1
                scores[0] += 1
                history[i] = {(choices_dict[comp_choice], choices_dict[user_input],"Player wins")}
        if (rounds == 1 and decrease_rounds):
            final_scores = scores
            result(initial_rounds_num, final_scores)
        if decrease_rounds:
            rounds -= 1
def start(rounds, scores):
    print( "\n-------------------\nBest of " + str(rounds) + ":\n-------------------\nEnter:\n\nr for Rock\np for Paper\ns for Scissors")
    game_run(rounds, scores)
def num_games_func():
    print("This is a new game :\n")
    scores = [0, 0]
    while True:
        num_games_input = input("...")
        if (num_games_input.isdecimal()):
            num_games_input = int(num_games_input)
            if (num_games_input == 10):
                rounds_remaining = num_games_input
                start(num_games_input, scores)
            elif (num_games_input<10) or (num_games_input>10):
                rounds_remaining = num_games_input
                start(num_games_input, scores)
            else:
                print("Error: Invalid input\nEnter a valid input")
        else:
            print("Error: Invalid input\nEnter a valid input")
print("\nEnter the number of rounds for Rock, Paper, Scissors\n")
num_games_func()
