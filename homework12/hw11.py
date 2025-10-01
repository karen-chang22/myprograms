# Quadrant Selection
# given (x, y), determine the quadrant it is in

# input
# original input
# x = int(input())
# y = int(input())

# modified input
point = input() # in a form of: "10 -11"

point = point.split(" ") # we are running a .split() method from the string object class, and 
#the argument being a space --> ["10", "-11"]
# .split() method splits the string characters when it encounters the given patter, here is the 
# whitespace; only works for string

""" a long form of solution to converting a list of numeric strings to a list of integers
fixed_point[]
for value in fixed_point:
    fixed_point.append(int(value))
"""
point = list(map(int, point)) # point is: ["10", "-11"] --> iterable(10, -11) --> [10, -11]
# map(): applies the function (int type casting) to every individual item in a collection 
# here is a list (point)
# map() doesn't create a new list, but create a new object: iterable obect
# we want a list back, so we convert all the iterable objects into a list
print(point)

# variable unpacking
x, y = point 
print(f"x is {x}")
print(f"y is {y}")

# quadrant selection
if x > 0:
    # pass # a placeholder in python
    if y > 0:
        print(f"the point of {x} and {y} is in Quadrant 1.")
    else: # y is negative
        print(f"the point of {x} and {y} is in Quadrant 4.")
else: # x is negative
    if y > 0:
        print(f"the point of {x} and {y} is in Quadrant 2.")
    else: 
        print(f"the point of {x} and {y} is in Quadrant 3.")

