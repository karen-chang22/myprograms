a_list = [6, 5, 3, 1, 8, 7, 2, 4]
b_list = ['f', 'e', 'c', 'a', 'h', 'g', 'b', 'd']



def inserty(a_list):
    i = 1 # we start at one so we can do i-1
    while i < len(a_list):
        j = i
        while j > 0:
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j],  = a_list[j], a_list[j-1]
                b_list[j-1], b_list[j] = b_list[j], b_list[j-1]
            else:
                break
            
            j -= 1
        
        i += 1


        1, 3, 4, 1, 5, 2, 9
    return a_list, b_list

print(inserty(a_list))
