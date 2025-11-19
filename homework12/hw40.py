# List of Prime Numbers under N
def isPrime(integer):
    for i in range (2, integer):
        if integer % i == 0:
            return False
    return True


def hehe(integer):
    prime_list = []
    for n in range(2, integer):
        if isPrime(n):
            prime_list.append(n)

    return prime_list

number = int(input("enter the integer: "))
print(hehe(number))

        