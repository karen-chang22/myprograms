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
new_stop = int(math.sqrt(num)) + 1 # num=27
while count < new_stop: # 1 < 27
    if num % count == 0: # if 27 % 1 == 0
        dividend = num // count # divident = 27 // 1 (divide then round down)
        if count != divident: # if they don't equal, it means num isn't a perfect sqr
            factor_count += 2 #(ex: 3 x 9 --> 2 factors)
        else:
            factor_count += 1 # meaning num is a perfect sqaure, so we only add the factor once
            #perfect square (ex: 5 x 5 = 25)
    count += 1
print(f"{num} has {factor_count} factors.")


