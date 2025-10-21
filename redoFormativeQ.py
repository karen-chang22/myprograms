# write a FUNCTION that when given an argument: string, return based on the following:
# if number of uppercase > lowercase --> 1
# if equal amount --> 0
# if lowercase > uppercase --> -1

arguement = input()
def compare(arg):
    upper_count = 0
    lower_count = 0
    for n in arguement:
        if n.isalpha() and n.isupper():
            upper_count += 1
        elif n.isalpha() and n.islower():
            lower_count += 1
    if upper_count == lower_count:
        return 0
    elif upper_count > lower_count:
        return 1
    else:
        return -1

print(compare(arguement))