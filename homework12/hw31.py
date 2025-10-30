# anagram checker

def anagram(word1, word2):
    if len(word1) != len(word2):
        return "They are not anagrams"
    else:
        is_anagram = True
        for n in word1:
            if word1.count(n) != word2.count(n):
                is_anagram = False
                break

    return is_anagram

x = input("enter the first word: ")
y = input("enter the second word: ")
print(f"anagram? {anagram(x, y)}")