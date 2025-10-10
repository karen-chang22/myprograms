# practice with strings functions and methods

word = 'hello'
word2 = 'world'
outputChoice = int(input("enter the number: "))


#concatenation ENTER 1
word_can = word + word2

#repetition ENTER 2
word_rep = word * 3

#indexing & slicing [start:end:step] ENTER 3
word_ind_slc = word[:-2]

#membership: in || not in ENTER 4
word_memI = 'h' in word
word_memN = "e" in word2

#max() and min() in strings ENTER 5
word3 = 'bye'
wordMin = min(word, word2, word3)
wordMax = max(word3)

#len() ENTER 6
wordLen = len(word2)

#basic type & type conversion related functions ENTER 7
num = 12345
num_s = "6789"
num_b = ""
typeValue = type(num)
conv_string = str(num)
conv_float = float(num)
conv_int = int(num_s)
conv_bolT = bool(num)
conv_bolF = bool(num_b)



if outputChoice == 1:
    print(f"{word_can}")
elif outputChoice == 2:
    print(f"{word_rep}")
elif outputChoice == 3:
    print(f"{word_ind_slc}")
elif outputChoice == 4:
    print(f"{word_memI}, {word_memN}")
elif outputChoice == 5:
    print(f"{wordMin}, {wordMax}")
elif outputChoice == 6:
    print(f"{wordLen}")
elif outputChoice == 7:
    print(f"{typeValue}, {conv_string}, {conv_float}, {conv_int + 1}, {conv_bolT}, {conv_bolF}")
elif outputChoice == 8:
    print(f"{typeValue}")





