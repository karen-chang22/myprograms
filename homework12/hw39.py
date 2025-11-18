# Greatest Common Divisor
# find the gcd of two given integers

def gcd(num1, num2):
    gcd = 1
    for n in range(1, (min(num1, num2))+1):
        if num2 % n == 0 and num1 % n == 0:
            if n > gcd:
                gcd = n
            
    return gcd

i = int(input("num1: "))
j = int(input("num2: "))
print(gcd(i, j))

