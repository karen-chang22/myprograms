# Best Scrabble Score
# function takes a list of strings and returns a list with: 1. highest scoring string 2. highest score

def scrabble(word):
    score = 0
    for n in word:
        if n in {'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'}:
            score += 1
        elif n in {'d', 'g'}:
            score += 2
        elif n in {'b', 'c', 'm', 'p'}:
            score += 3
        elif n in {'f', 'h', 'v', 'w', 'y'}:
            score += 4
        elif n in {'k'}:          # elif n == "k"
            score += 5
        elif n in {'j', 'x'}:
            score += 8
        elif n in {'q', 'z'}:      # elif n in "qz":
            score += 10
    return score

def best(the_list):
    best_score = 0
    longest_string = ''
    result = []
    for string in the_list:
        if scrabble(string) > best_score:
            best_score = scrabble(string)
            longest_string = string
    result.append(longest_string)
    result.append(best_score)
    return result

a_list = [
    'graphic',
    'despair',
    'notice',
    'kite',
    'quiz',
    'or',
    'prediction'
]
print(best(a_list))

