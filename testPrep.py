# Test Prep - Mean Calculation

DATA = [1, 2, 3, 4, 5]

def mean(arg):
    sum = 0
    counter = 0
    for n in arg:
        sum += n
        counter += 1
    result_mean = sum / counter
    return result_mean

print(f"the mean is: {mean(DATA)}")

def sorted(arg):
    sorted_list = []
    while len(arg) > 0:
        smallest = min(arg)
        sorted_list.append(smallest)
        arg.remove(smallest)
    return sorted_list

def median(arg2):
    sorted_list = sorted(arg2)
    if len(sorted_list) % 2 == 0: #if the number of items is even number, it means there are two "middle values"
    #so we must find the mean of the two values
        middle_even = (int(len(sorted_list) // 2))
        median = (sorted_list[middle_even-1] + sorted_list[middle_even]) / 2
    else:
        middle_odd = (int(len(sorted_list) / 2))
        median = sorted_list[middle_odd]
     
    return median


print(f"the median is: {median(DATA)}")

    

