# longest palindromic number
# find the longest palindromic number from the product of two 3-digit number
# correct ans: 906609
def is_palindrome(text):
    return text == text[::-1]

largest = 0
for n in range (100, 1000, 1):
    for m in range (100, 1000, 1):
        product = n * m
        if is_palindrome(str(product)) and product > largest:
            largest = product

print(largest)




