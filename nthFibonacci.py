# Finding fibonacci number

def fib(nth):
    if nth in {0, 1}:
        return nth
    else:
        location = 2
        previous1 = 0
        previous2 = 1
        sum = 0
        while location <= nth:
            sum = previous1 + previous2
            previous2 = previous1
            previous1 = sum
            location += 1
        return sum
# to understand variable updating
# the key takeaway is how we update our variables
i = 0
nthFib = int(input())
while i <= nthFib:
    print(f"N: {i} fib(N): {fib(i)}")
    i += 1


