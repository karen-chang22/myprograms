# 1. create an empty list
fruits = []

# 2. if the string is empty
if not fruits: # truthy falsy
    print("fruits is empty!")
    # or if len(fruits) == 0

# 3. what does len(), sum(), min(), max(), do when the argument is a list
names = [
    'hannah', 'kenny', 'karen', 'howard', 'doris'
] # explicit list, bc we input the vaues ourselves
colours = [
    'red', 'yellow', 'green', 'black'
]
print(len(colours))
print(min(names, colours)) # output: ['hannah', 'kenny', 'karen', 'howard', 'doris']
print(max(names, colours)) # output: ['red', 'yellow', 'green', 'black']
c_list = [3, 1, 4, 1, 5, 9]
print((sum(c_list))) # output: 23

# 4. access individual items in a list
print(colours[-2]) # output: green
print(colours[1:3]) # output: yellow, green

# 6. join two lists together
names.extend(colours) # CANNOT assign to a new variable to hold the new combined lists
# mutates 'names', therefore we have to print 'names' to see
print(names) # output: ['hannah', 'kenny', 'karen', 'howard', 'doris', 'red', 'yellow', 'green', 'black']

total = names + c_list # creates a NEW list, did not manipulate either of the original lists

a = [3,1,4]
for item in c_list:
    a.append(item)

# 7. reverse a list
names.reverse() 
print(names)
reversed_colours = list(reversed(colours)) # since its not printable, we must convert to a list to see it
print(reversed_colours[1]) # output: green

# 8. create a new copy
copy1 = ['im copy 1']
copy2 = ['im copy 2']
print(names.copy() + copy1) # output: ['black', 'green', 'yellow', 'red', 'doris', 'howard', 'karen', 'kenny', 'hannah', 'im copy 1']
print(colours[:] + copy2) # output: ['red', 'yellow', 'green', 'black', 'im copy 2']

# 9. compare lists for equality
print(copy1 == copy2) # output: False

# 10. determine if a item exists within a list
print("kenny" in names) # output: True

# 11. locate the index of an item within a list
print(names.index("kenny")) # output: 7

# 12. count how often an item occurs within a list
nums = [
    99, 7, 2, 23, 2, 8, 12, 2,
] 
print(nums.count(2)) # output: 3

# 13. convert a string to a list
print(list('today')) # output: ['t', 'o', 'd', 'a', 'y']

# 14. sort a list
todayListed = list("today")
todayListed.sort()
print(todayListed)

print(sorted("today"))
# both methods output: ['a', 'd', 'o', 't', 'y']

# 15. sort two lists where the index are attached to each other based on one of the lists


