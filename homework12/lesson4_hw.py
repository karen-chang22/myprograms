# Painting fences 9/18

# input
section1 = input("enter section 1: ")
section2 = input("enter section 2: ")
section3 = input("enter section 3: ")

# import statement
from math import ceil
# processing
cans = len(section1) + len(section2) + len(section3) # counting total number of F's
boxes = ceil(cans/12)
totalCost = 14.95 * boxes
leftover = 12 * boxes - cans

# output
print(f"we needed {cans} paint cans.")
print(f"we have {leftover} leftover.")
print(f"the project costs ${totalCost}.")
