# Rock Paper Scissors vs AI

from random import choice

# input
invalid = True
player = ''

while invalid:
    player = input("Enter (rock, paper, or scissors): ") 

    if player in {'rock', 'paper', 'scissors'}:
        invalid = False
        # we use in opeartor in python often with sets because it's faster execution speed
# end of while loop

# processing
ai = choice(['rock', 'paper', 'scissors'])  #randomly chooses one of these
print(f"AI has chosen {ai}")
# game logic
if player == ai: #it's better to put this condition first because then if this is true we don't need to check the rest
    print("tie game")
else:
    #guaranteeed that one side has won
    if player == 'rock':
        if ai == 'paper':
            print("AI has won the game")
        else:
            print("player has won the game")
    elif player == 'paper':
        if ai == 'scissors':
            print("AI has won the game")
        else:
            print("player has won the game")
    else:
        if ai == 'rock':
            print("AI has won the game")
        else:
            print("player has won the game")

# end of game logic conditions



