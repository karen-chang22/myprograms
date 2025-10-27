# Bubble Sort
b_list = [
    # 1, 3, 4, 1, 5, 2, 9
    6, 5, 3, 1, 8, 7, 2, 4
]
def bubble(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        count_swap = 1
        # or could do: swapped = True
        # while swapped == True:
        while count_swap > 0: #count the number of swapping, if it didn't swap, meaning it's in order
            i = 0
            # swapped = False
            count_swap = 0
            while i < (len(a_list)-1): #doesn't get to the very last item, because i+1 will be outOfBounds
                smallest = a_list[i]
                if a_list[i+1] < a_list[i]: #if the second value of the bubble is smaller, it needs to swap
                    temp = a_list[i] #make a copy of the bigger value to be assigned to the second spot later
                    a_list[i] = a_list[i+1] #swapping mechanism: assigning the smaller value (i+1) to the first spot
                    a_list[i+1] = temp #swapping mechanism: assigning the bigger value (i) to the second spot
                    smallest = a_list[i+1] 
                    # python way of swapping:
                    # if a_list[i] > a_list[i+1]
                            # a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

                    count_swap += 1 #it means: swapping occurred!! It must loop again to check whether everything is in place
                    # swapped = True
                i += 1
        return a_list

print(f'the list ordered from smallest to greatest: {bubble(b_list)}')
# expected output: [1, 1, 2, 3, 4, 5, 9]
