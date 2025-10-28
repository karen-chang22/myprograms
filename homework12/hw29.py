# Consonant Counting
# count the number of consonants in a given string argument, 'aeiou' are the only vowels

def consonant_count(arg, vowel=False):
    counter_c = 0
    for n in arg:
        if n not in 'a' 'e' 'i' 'o' 'u':
            counter_c += 1
    if not vowel:
        return counter_c
    else:
        counter_v = len(arg) - counter_c
        return counter_v
    
    
print(f"vowels: {consonant_count('aeiou', False)}")

# string = input('enter the argument: ')
# print(consonant(string))