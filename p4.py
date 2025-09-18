# Heads or Tails 
from random import choice

play = True
while play:
    print("Welcome to our heads or tails game!")
    print("please choose either heads or tails. Enter X if you want to exit.")
    while play: # infinite loop
        userInput = input("user's choice: ")
        userInput = userInput.lower() # makes everything lowercased

        if userInput in {"heads", "tails", "head", "tail"}:
            # userInput was valid, we can exit the infinite loop
            break # trigger this to exit
        elif userInput in {"x"}: 
            play = False
            break
        else:
            print("invalid input, please type in 'heads' or 'tails' or x to exit")

    # end of while

    # now randomly generate HEADS OR TAILS
    if play == True:
        flipResult = choice(["heads", "tails"]) # [] bc its a list NOT NEED FOR "."
        print(f"The computer flipped: {flipResult}.")
        if userInput in {"heads", "head"} and flipResult == "heads":
            print("The user guessed greatly!")
        elif userInput in {"tails", "head"} and flipResult == "tails":
            print("The user guessed greatly!")
        else:
            print("Sorry, wrong guess!")

print("Thanks for playing~")
