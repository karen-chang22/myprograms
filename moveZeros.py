# goal: to move all the zeros to the very end while maintaining the order of the other numbers

def move(a_list):
    counter = 0
    result = []
    for item in a_list:
        if item != 0:
            result.append(item)
        else:
            counter += 1
    for times in range(0, counter):
        result.append(0)

    return result


def move2(a_list):
    i = 0
    while i < len(a_list):
        if a_list[i] == 0:
            a_list.append(0)
            a_list.remove(a_list[i])
        i += 1
    return a_list

def move3(a_list):
    temp = [0] * len(a_list) #starts off with all zeros: 00000
    i = 0
    for item in a_list: 
        if item != 0: #once runs into a number (not zero), replaces 0 with the number
            temp[i] = item
            i += 1
    temp = a_list
    return a_list
    #sometimes we want a list filled w placeholder

def move4(a_list):
    zero_i = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_i] = nums[zero_i], nums[i]
            zero_i += 1

    return a_list
    #we can have two pointers moving at different speeds and swap when a number is encountered

# Testing
nums = [0, 1, 0, 0, 3, 12]
print(move4(nums))