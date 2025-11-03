# shared characters in two strings
# create a function that takes two string inputs, return a single sorted list of characters that are found in each string

def duplicates(arg1, arg2):
    if not arg1 or not arg2: #if one of them is empty
        return []
    else: 
        arg1.lower()
        arg2.lower()
        result = []
        for n in arg1:
            if arg2.find(n) != -1:
                result.append(n)

        return sorted(result)

text1 = input('enter the text: ')
text2 = input('enter the second text: ')
print(f'the duplicate characters are: {duplicates(text1, text2)}')