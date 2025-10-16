# String stuff - Oct 08
# tacocat is a palindrome, so are doggod, 906609
def is_palindrome(word):
    # checks whether argument word is a palindrom
    return word == word[::-1]

text = input("enter a word: ")
if 'ab' <= 'abc':
    print("true")
else:
    print('false')
if is_palindrome(text):
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome (boo)")
