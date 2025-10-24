# a string clean function
# that removes all non-alphabetical characters and return lowercased letters only

def clean(arg):
    '''
    Functionality: to clean the string so it's left with only lowercased alphabets and free of any special characters or numbers

    Args: 1 string argument from input to analyze/clean

    Return: a string that consists of only lowercased alphabets
    '''
    cleaned = ''
    for n in arg:
        if n.isalpha():
            cleaned += n.lower()
    return cleaned

string = input('enter string: ')
print(f'the cleaned version of the string is: {clean(string)}')



