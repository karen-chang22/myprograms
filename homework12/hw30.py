# String Pattern Maker
# returns a string of 1s and 0s based on the argument

def create_line(num):
    text = ''
    for n in range(1, num+1):
        if n % 2 == 0:
            text += "0"
        else:
            text += "1"
    return text

def output_pattern(num):
    for i in range(1, num+1):
        print(create_line(i))

v = output_pattern(5) #must give num a value

