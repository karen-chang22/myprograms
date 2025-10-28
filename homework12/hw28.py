# palindrome checker

def palindromeChecker(text):
    text_list = list(text)
    reverse_list = text_list[:]
    reverse_list.reverse() # instead of assignment, we can mutate variable reverse_list
    if text_list == reverse_list:
        return True
    else:
        return False

string = input('enter your text: ')
if palindromeChecker(string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome")

