# Comma Separated Values & Random Numbers List 
def convert(text):
    removed = text.split(",")
    a_list = []
    for val in removed:
        a_list.append(int(val))

    return a_list


# list of random 
# create a function that takes three arguments: (start, end, frequency), and eturn a list of random [frequency] many integers within the range

from random import randrange
def randList(start, end, frequency):
    if start < end and frequency > 0:
        a_list = []
        for _ in range(frequency):
            new_val = randrange(start, end+1)
            a_list.append(new_val)
        return a_list
    else:
        return []

print(randList(0, 50, 10))