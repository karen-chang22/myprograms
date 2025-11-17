def mergeSort(a_ilst):
    # consider as a splitter
    # Base Case
    if len(a_list) <= 1:
        return a_list
    
    # Work towards the base case
    mid = len(a_list) // 2
    first_half = a_list[:mid]
    second_half = a_list[mid:]

    first_half = mergeSort() # RESURSIVE CALL :O!
    second_half = mergeSort() # AGAIN!!

    return combine(first_half, second_half)


def combine(left, right):
    # assume left and right are sorted
    if len(left) == 0 and len(right) == 0:
        return []
    elif len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    else:
        # both left and right has values
        i = 0 # for left
        j = 0 # for right
        answer = [] # shove the sorted stuff here
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                answer.append(left[i])
                i += 1
            else:
                answer.append(right[j])
                j += 1
        # What happens to the leftover values?
        # when we've left the while loop above, and reaches here, 
        # it means that either LEFT or RIGHT is empty, so we add the remaining items
        while i < len(left): 
            answer.append(left[i])
            i += 1
        while j < len(right):
            answer.append(right[j])
            j += 1

        return answer
