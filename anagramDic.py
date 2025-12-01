# a program to check anagrams using dictionaries
# all uppercase, no special char, no numbers
# technique: frequency table
# letter : count
def anagram(word1, word2):
    freq_table = {} # empty dict
    for c in word1: 
        if c in freq_table:
            freq_table[c] += 1
        else:
            freq_table[c] = 1
    # from an empty loop, we keep track of each letter and its frequency into the freq_table

    for c in word2:
        if c != freq_table:
            return False
        else:
            freq_table[c] -= 1
            if freq_table[c] < 0:
                return False

    for key, value in freq_table.items(): #prove again (when the first word is longer than the second)
        if value != 0:
            return False
    return True
