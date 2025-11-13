# method 1
def collatz(num): # 1000 000
    longestDigit = 0 # value that is the longest
    longestValue = 0
    for item in range(1, num + 1, 2):
        counter = 0
        value = item
        while value != 1:
            counter += 1
            if value % 2 == 0:
                value = value // 2
            else:
                value = value * 3 + 1
        if counter > longestValue:
            longestDigit = item
            longestValue = counter

    return longestDigit

getNum = int(input("enter the number: "))
print(collatz(getNum))


# IDEA:
# store the length of sequence of each number somewhere, pull them up so when item reaches that specific value, it can just 
# retrieve the designated length without calculating

