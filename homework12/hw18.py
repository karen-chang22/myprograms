# finding factors of a number
# given an integer, print out all its factors

#input
num = int(input("enter integer: "))


for divider in range(1, num+1):
    print(f"divider is: {divider}")

    if num % divider == 0:
        print(f"{divider} is a factor of {num}")
