# test prep 3 - Scrable

def scrabble(text):
    score = 0
    text = text.lower()
    for n in text:
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

word = input("enter text: ")
print(scrable(word))

def listScrabble(a_list):
    scoreList = []
    for word in a_list:
        scoreList.append(scrabble(word))

    return listScrabble

def sortScores(b_list): #b_list considers of the words ex; CAT, DOG
    scoresList = listScrabble(b_list) #turns into a list of scores in the SAME ORDER WITHOUT BEING SORTED
    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < len(scoresList)-1:
            smallest = scoresList[i]
            if scoresList[i] > scoresList[i+1]:
                swapped = True
                scoresList[i], scoresList[i+1] = scoresList[i+1], scoresList[i]
                b_list[i], b_list[i+1] = b_list[i+1], b_list[i]

            i += 1

    return b_list

