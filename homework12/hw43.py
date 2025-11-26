# using the set data type in Python

#1 remove duplicates in a list
# using LIST
def rm_duplicate(a_list):
    result = []
    for item in a_list:
        if item not in result:
            result.append(item)
    return result
# using SET
def duplicates2(a_list):
    set_version = set(a_list) #converts the list into a set
    return list(set_version)
    # this is helpful because set only takes unique values (auto remove duplicates)


#2 unique letters in a given word
#--> takes a list of words and returns a set containing all unique letters used in these words
#a_list contains strings of words
def uniqueLetter(a_list):
    result_set = set() #initialize an empty set; NOT {}
    for word in a_list:
        tmp_set = set(word) #convert the string word into a set WHILE only keeping the unique letters
        result_set = result_set | (tmp_set) # | is union; or .union --> to combine two sets while removing duplicates
    return result_set


#3 set intersection count
#--> takes a list of sets and returns the count of elements that are common to all the sets
def i_count(a_list):
    #a_list contains numerous sets
    if a_list:
        result_set = a_list[0]
        for example_set in a_list[1:]:
            result_set = result_set & example_set # & is the intersection operator

        return len(result_set)

b_list = [{1,4,3}, {3, 4, 5}, {3, 4, 8}]
print(i_count(b_list))

