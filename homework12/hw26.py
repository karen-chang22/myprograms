# Intro to Functions - creating a function

# Problem: determine the number of factors for each number from 1 to N
# Let N be a user input

def factor_count(number):
    ''' determine the number of factors the number has 

    Args: 
        number: an integer needed to determine the number of its factors

    Returns:
        an integer, which is the total amount of factors the arguement has
    '''
    # above is a doc string, documenting a function: 
        # a single line of explanation of what the function does
        # list out the arguments, the data type and what it's supposed to do
        # what will be returned by the function 

    counter = 0
    for divider in range(1, number+1):
        if number % divider == 0:
            counter += 1

    return counter
# end of factor_count()

userInput = int(input('enter N: '))
for num in range(1, userInput+1):
    factor_size = factor_count(num)
    print(f'{num} has {factor_size} factors')

