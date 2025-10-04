# Factorial Calculator
# ! operator in math ... !5 = 5 x 4 x 3 x 2 x 1 ... !n = n x (n-1) x (n-2) x n-3 ... x 1

# input
num = int(input("enter the number: "))

# solution 1 (while loop)
multiplier = 1
factorial = 1
while multiplier <= num:
    factorial = multiplier * factorial
    multiplier += 1
print(f"factorial of {num}: {factorial}")

# solution 2 (for loop) [N, 0)
factorial2 = 1
for i in range(num, 0, -1):
    # i is the iterating variable, representing each value in the sequence
    # going from [N] to (0) and decreasing by 1 each time (stepping value)
    # if step is not identified, its assumed to be 1
    factorial2 = factorial * 1
print(f"for loop answer: {factorial2}")



