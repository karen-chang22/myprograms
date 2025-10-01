# Prime Number Function
# def primeNum(number):
#     counter = 2
#     isPrime = True
#     while (counter < number):
#         if (number % counter == 0):
#             isPrime = False
#         counter += 1
#     return isPrime

# num = 1
# while (num < 100):
#     if (primeNum(num)):
#         print(f"{num}")
#     num += 1

def isPrime(num):
    if num <= 1: # 1 is not a prime number
        return False
    elif num == 2: # 2 is a prime number
        return True
    elif num % 2 == 0: # odd numbers cannot be prime numbers
        return False
    else: # left with odd numbers now
        divider = 3 
        upperLimit = int(num**0.5) + 1 # the +1 guarantees that it runs up and including the square
        # root divisor
        while divider < max(upperLimit, 3):
            if num % divider == 0:
                return False
            divider += 2
        return True # if we can't prove its a composite number, then it must be prime

number = 1
while (number < 100):
    if (isPrime(number)):
        print(f"{number}")
    number += 1