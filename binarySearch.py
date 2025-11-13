# $5000 question - Binary Search
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