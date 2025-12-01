# Frequency of a letter/character in a word
# write a function that takes a string arg and return a dic that should have the alphabetical characters as keys in sorted order and assigned 
# with its frequency; case should be ignored

def freq(word):
    clean_word = sorted(word.lower()) # first make the word lowercased, then sort it (becomes a list)

    ans_dic = {}
    for char in clean_word:
        if char not in ans_dic: # means the char isn't a key yet
            ans_dic[char] = 1
        else:
            ans_dic[char] += 1 # increase it frequency since it has already been found

    return ans_dic


print(f"char freq of hello: {freq('hello')}")
