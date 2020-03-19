from random import *
from sys import *   # used for the function 'exit()' to end the program
def play():   # play() function
    choice = input("What's your choice?")
    choices = {1 : 'rock', 2 : 'paper', 3 : 'scissors'}
    c_choice = choices[randint(1,3)]    # randomly generaed choice
    if choice == c_choice:   # choice- player's choice, c_choice- computer's choice
        return print('Tie!')
    if compare(choice,c_choice):
        return print('You Win!')
    else:
        return print('You Lose!')
def compare(pChoice,compChoice):    # compare() function
    results = {('paper','rock') : True,
                    ('paper','scissors') : False,
                    ('rock','paper') : False,
                    ('rock','scissors') : True,
                    ('scissors','paper') : True,
                    ('scissors','rock') : False}
    return results[(pChoice,compChoice)]

def game_play():   # game_play() function
    begin = input("Let’s play Rock, Paper, Scissors? (yes/no) ")
    while begin != "yes":
        if begin == "no":
            print("Game Over")
            sys.exit()
        else:
            print("Please try again")
            begin = input("Let’s play Rock, Paper, Scissors? (yes/no)")
    play()   # play() function called 
    while True:
        begin = input('Play again?')
        while begin != "yes":
                if begin == "no":
                    print("Game Over")
                    exit()
                else:
                    print("Please try again")
                    begin = input("Play again? ")
        play()   # play() function called 
game_play()    # game_play() function called
