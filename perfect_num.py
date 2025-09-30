# perfect number function

def perfectNum(num):
    counter = 1
    sum = 0
    while counter < num:
        if num % counter == 0:
            sum += counter
        counter += 1
    return sum == num

# local

number = int(input("enter a number: "))
if perfectNum(number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")

# global code area