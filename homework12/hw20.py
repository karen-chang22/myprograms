# sum of perfect number under 10,000
# proper divisor: factors of a number that doesn't include the number itself
# perfect number: sum of a number's proper divisors equal to the number itself

totalSum = 0

for num in range(1, 10000):
    factorSum = 0
    for divider in range(1, num): # counting sum of factors
        if num % divider == 0:
            factorSum += divider
    if factorSum == num: # a perfect number
        totalSum += num
        print(f"{num}")

print(f"the sum of perfect numbers under 10000 is {totalSum}")



