# Test Prep 2 - Binary Search

a_list = [1, 1, 2, 3, 4, 5, 6, 9]
target = 6

# def sum(a_list, target):
#     for i in range(len(a_list)-1): #i is index
#         j = i + 1 #j is also index
#         while j < len(a_list):
#             if a_list[i] + a_list[j] == target:
#                 return True
#                 break
#             j += 1

#      return False

# print(sum(a_list, target))


# Binary Search
def bin_search(a_list, target):
    low = 0
    high = len(a_list)
    while low < high:
        mid = (low+high) // 2 # index
        if a_list[mid] == target:
            return mid
        elif a_list[mid] > target:
            high = mid
        else: #a_list[mid] < target
            low = mid + 1

    return -1 # classic code saying that it doesn't exist
# Solve using Binary Search
def sum2(a_list, target):
    possibility = False
    for i in a_list:
        secondVal = target - i
        if bin_search(a_list, secondVal) != -1:
            possibility = True
            break

    return possibility
print(sum2(a_list, target))

# fastest method
def solve(a_list, target):
    i = 0
    j = len(a_list)-1
    while i != j:
        if a_list[i] + a_list[j] > target:
            j -= 1
        elif a_list[i] + a_list[j] < target:
            i += 1
        else:
            return True

    return False

