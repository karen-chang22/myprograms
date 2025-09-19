# Rolling a D20 Against a Set DC

# import statement
from random import randrange

# input
difficulty = int(input("Enter the DC: "))

# processing and output
playerRoll = randrange(1, 21) #randrange never include b; it goes up to b
print(f"the player has rolled {playerRoll} on their D20.")

if playerRoll >= difficulty:
    print(f"the player was successful as {playerRoll} is greater than {difficulty}")
else:
    print(f"the player was unsuccessful as {playerRoll} is less than {difficulty}")

