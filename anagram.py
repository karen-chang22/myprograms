# given two texts, determine if they are anagrams
# anagram: texts that are composed of the same set of characters/symbols

def alphaSorting(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    i = 0
    while i < len(abc): # getting through each letter in the alphabet from a ~ z
        # current_letter = abc[i]
        # text_lowered = text.lower()
        # if current_letter in text_lowered:
        #     occurence = text_lowered.count(current_letter)
        #     result = result + (current_letter * occurence)
        # --- slower way

        if abc[i] in text.lower():
            result += abc[i] * (text.lower().count(abc[i])) #starting from a, we count its occurence and add onto our result string variable
        i += 1
    return result

word1 = input("enter the first text: ")
word2 = input("enter the second text: ")
if alphaSorting(word1) == alphaSorting(word2):
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")