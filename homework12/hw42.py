# Possible Sum in an Array
# array is in ascending order

def find_target(a_list, target):
    i = 0
    j = len(a_list)-1
    while i != j:
        sum = a_list[i] + a_list[j]
        if sum == target:
            return True
        elif sum > target:
            j -= 1
        elif sum < target:
            i += 1

    return False

a_list = [
    1, 2, 4, 7, 8, 10
]
target = 19
print(find_target(a_list, target))