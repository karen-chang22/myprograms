# String Checklist
# 1. Create an empty string
empty_string = ""
ver2 = ''

# 2. Determine if a string is empty
    #method 1
if not str_var:
    print('str_var is empty!')
    #method 2
if len(str_var) == 0:
    print('str_var is empty!')

# 3. Format a string to contain dynamic data
name = "Fluffington"
str_var = f'Hello {name}'

# 4. Access individual characters/items in a string
print(name[0]) # --> F
print(name[-2]) # --> o

# 5. Access the first, access the last item in a sting
print(name[0]) # zero index is always the first
print(name[len(name[-1])]) # this gives last
print(name[-1]) # --> also gives last

# 6. Join two/multi strings together
a = 'poo'
b = 'poo'
c = a+B
print(c) # we expect poopoo --> concatenation

# 7. Reverse a string
temp = 'park'
reverse = temp[:: -1]
v2 = ''.join(reversed(temp))

# 8. Create a copy of a string
temp = 'hydroflask'
tempCopy = temp[:] #starts at beginning, goes to the end
another_copy = temp

# 9. Compare strings for equality
a = 'marshall'
b = 'dog'
status = a == b #outputs: False/True

# 10. Determine the minimum and maximum value within a string
temp = 'hydroflask'
print(max(temp)) # grabs the biggest ASCII value
print(min(temp)) # grabs smallest
print(max('hello', 'goodbye')) # hello is bigger
print(min('1', '2', '3', '!')) # ! is the smallest out of the given arguments

# 11. Determine if an item or a pattern exists within a string
word = 'poopooplatter'
if 'poo' in word:
    print("THERE IS POO!")

# 12. Locate the index of an item or a pattern within a string
poo_location = word.find('poo') # doesnt crash out if it isn't find
poop_location = word.index('poop') # index WOULD crash out if not found

# 13. Count how often an item or a pattern occurs within a string
poop_count = word.count('poo')

# 14. Convert all items in a string to uppercase/lowercase
yellHello = 'hello'.upper()
calmHello = yellHello.lower()

# 15/16. Determine if the string can be convereted to an integer; converts a string to an integer
strNum = '67'
if strNum.isdigit(): # checks if the string is only composed of digits
    num = int(strNum)

# 17. Determine if a string only contains alphabetical characters
word = 'shsm'.isalpha()

# 18. Remove non-alphabetical characters from a string; sometimes its easier to create than remove
gibberish = "!sdfouwertn193&23$234j)g&"
clean = ''
i = 0
while i < len(gibberish):
    if gibberish[i].isalpha():
        clean += gibberish[i]
    i += 1 # growing/creating an empty string to eliminate/remove certain characters

# 19. Remove all alphabetical characters from a string
gibberish = "!sdfouwertn193&23$234j)g&"
clean = ''
i = 0
while i < len(gibberish):
    if gibberish[i].isalpha() == False:
        clean += gibberish[i]
    i += 1 

# 20. Remove all whitespaces from a string
example = 'h h h h        e l  l oo'
example = example.replace(' ', '') # not removing, just replacing spaces with nothing

# 21. Sort a string in ASCII order or reverse-ASCII order
# 22. Determine if a string follows a ruleset

