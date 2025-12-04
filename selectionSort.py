# Non-Destructive Selection Sort with Lists
def select(a_list): #a_list is a placeholder variable, rep the input the function would get (bc we don't know the value)
    if len(a_list) <= 1: # this argument (list) has only single or no values, no need to sort, so just return the list back
        return a_list
    else: #when the list has more than 1 items
        i = 0
        while i < len(a_list): 
            smallest = a_list[i] # to prove it is or it is not, assuming it is
            # go hunting
            j = i + 1 # searches from i + 1 onwards
            new_location = i # initialize to i since it was initially assumed to be i
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest: # smallest value is no longer is smallest
                    smallest = new_value
                    new_location = j # the index/location of new smallest item
                j += 1
            # end of hunting
            # swap the smallest into the proper location
            temporary = a_list[i]
            a_list[i] = smallest
            a_list[new_location] = temporary
            # Python way
            # a_list[i], a_list[new_location] = a_list[new_location], a_list[i]
            i += 1    
    return a_list

