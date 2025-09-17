# Factors of a Number 9/17

print("enter the number: ")
num = int(input())
while num <= 0:
    print("please enter a positive number")
    num = int(input())

count = 1
factor_count = 0
while count <= num:
    if num % count == 0:
        print(f"{count}")
        factor_count += 1
    count = count +1
print(f"num has {factor_count} factors")
if factor_count > 2:
    print(f"{num} is a composite number")
else:
    print(f"{num} is a prime number")

# a faster method !!!
import math
count = 1
num = int(intpu("enter a value: "))

factor_count = 0
new_stop = int(math.sqrt(num)) + 1
while count < new_stop:
    if num % count == 0:
        dividend = num // count
        if count != divident:
            factor_count += 2 #perfect square (ex: 5 & 25)
        else:
            factor_count += 1
    count += 1
print(f"{num} has {factor_count} factors.")


