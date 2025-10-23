# Prime Factor Finder
# find the largest prime factor for this num: 600851475143

num = int(input("enter a number: "))
num_copy = num
largest = 0
while num % 2 == 0: 
    num = num // 2 #or //=
    
    largest = max(largest, 2)

# in here, we are checking if its divisible by 2, then continuously shrinking it by dividing it by 2, ultimately become an odd number

if num != 1:
    # we still have to check other primes
    factor = 3
    while num != 1:
        if num % factor == 0: 
            #found a prime factor
            largest = max(largest, factor)
            num //= factor
        else:
            factor += 2 #check the next odd number, its guaranteed to be a prime if we were to execute the if statement


print(f'the largest prime factor for {num_copy} is {largest}')

