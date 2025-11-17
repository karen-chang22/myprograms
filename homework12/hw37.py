# string compression
# example: aaabbbbbcc --> a3b5c2

def zip(text):
    counter = 1
    result = ''
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            counter += 1
        else:
            result = result + text[i-1] + str(counter)
            counter = 1
    result += text[-1] + str(counter)

    if len(result) < len(text):
        return result
    else:
        return text

word = input("enter the word: ")
print(f"compressed version: {zip(word)}")
