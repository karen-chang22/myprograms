# how to do 2 to the power of n using a recursive function
def exponent(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * exponent(base, exp-1)

print(exponent(2, 4))

def missing(array):
    limit = len(array)
    freq_table = {}
    for x in array:
        freq_table[x] = 1

    for i in range(0, limit+1):
        if i not in freq_table:
            return i 
    return -1

def scrabble_score(word):
    word.upper()
    score = 0
    for n in word:
        if n in "AEIOULNSTR":
            score += 1
        elif n in "DG":
            score += 2
        elif n in "BCMP":
            score += 3
        elif n in "FHVWY":
            score += 4
        elif n == "K":
            score += 5
        elif n in "JX":
            


def table(a_list):


