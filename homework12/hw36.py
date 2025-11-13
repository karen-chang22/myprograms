# Factors of a number & is a number prime?
def factor(num):
    factors = []
    for divider in range(1, num+1):
        if num % divider == 0:
            factors.append(divider)

    return factors


def isPrime(num):
    result = factor(num)
    if len(factor(num)) == 2:
        return "is a prime number"

    else: 
        return "is not a prime number"

number = int(input("enter: "))
print(isPrime(number))