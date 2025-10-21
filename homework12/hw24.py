# longest name finder

name = ''
longest_length = 0
longest_name = ''
userInput = input("enter the names (enter 'x' to stop): ")
while userInput.lower() != 'x':
    userInput = input("enter the names (enter 'x' to stop): ")
    if len(userInput) >= longest_length:
        longest_name = userInput # if longer, update the longest name
        longest_length = len(userInput) # if greater, update the longest length

if longest_name:    
    print(f'the longst name is {longest_name}, with a length of {longest_length}')
else:
    print('not enough data')