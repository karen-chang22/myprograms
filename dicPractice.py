# simple dic exercise
def factors(x):
    result = []
    for n in range(1, x+1):
        if x % n == 0:
            result.append(x)
    return result

num = int(input("enter the number: "))
table = {}
for n in range(2, num+1):
    table[n] = factors(n)
    # n is the address/key; value is the result of factors(n)
