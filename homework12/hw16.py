# FizzBuzz

# num = 1
# while num < 51:
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif:
#         if num % 3 == 0:
#             print("Fizz")
#     else:
#         if num % 5 == 0:
#             print("Buzz")

for num in range(0, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(f"{num}")


