# Tournament selection 

# input
# game1 = input("enter game 1 result: ")

wins = 0
for i in range(6): #range(6) --> 0,1,2,3,4,5 in computer memory
    currentResult = input(f"enter game {i+1} result: ")

    if currentResult == "w" or currentResult == "W":
        wins += 1

group = 0    
if wins > 4:
    group = 1
elif wins > 2:
    group = 2
elif wins > 0:
    group = 3

if group == 0:
    print("The player is eliminated")
else: 
    print(f"The player is in group {group}. ")


