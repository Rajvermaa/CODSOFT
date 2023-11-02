# ROCK PAPER SCIZZORS GAME USING IF ELSE AND RANDOM
import random

# here we create a tuple to give the choices to pick between Rock Paper Scizzor
picker = ("rock", "paper", "scizzors")
replay = True
while replay:
    player = None
    Comp = random.choice(picker)

    # Use of while loop so that a user can select only from the given choices(Rock , paper, scizzor) and
    #  this loop will run until user didnt select the right choice.
    while player not in picker:
        player = input("Choose between rock , paper , scizzors\n ")
    print(f"You Pick: {player}")
    print(f"Comp Pick: {Comp}")
    # here i put every condition of tie and winning in if or else-if condition
    if player == Comp:
        print("Its a TIE")
    elif player == "rock" and Comp == "scizzors":
        print("You Won :) ")
    elif player == "scizzors" and Comp == "paper":
        print("You Won :) ")
    elif player == "paper" and Comp == "rock":
        print("You Won :) ")
    else:
        print("You loose :(")

    replay_game = input("Play again? (y or n): ")
    if replay_game == "y":
        replay = True
    else:
        replay = False
a = input("Please give us feedback of your experiene: ")
print("We appriciate your feedback. Thank you for playing this game")
