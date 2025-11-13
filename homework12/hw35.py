# Remove duplicates in a list

def removeDup(a_list):
    result = []
    while len(a_list):
        i = 0
        if result.count(a_list[i]) == 0:
            result.append(a_list[i])

        a_list.remove(a_list[i])
    return result

text = [
    "a", "3", "3", "b", "e", "6", "a"
]
print(removeDup(text))