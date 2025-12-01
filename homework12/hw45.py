# More Dictionary Practice

#1: given a list, create a dict where each word is a key assigned to their length (apple : 5)
def length(a_list):
    # result = {}
    # for item in a_list:
    #     result[item] = len(item)

    # return result

    # using dict comprehension; improvise

    return {key : len(key) for key in a_list} #for all the keys(items) in a_list, its acting as a key MUCH SHORTER!!
    # this is called "dictionary comprehension"

print(length(['apple', 'bananas', 'hehehe', 'yay']))


#2: Fibonacci Dict
# assume that the dict starts as: {0:0, 1:1}
# where the next result is the sum of two numbers prior to it
def fibNum(num):
    result = {0:0, 1:1}
    if num in result:
        return result
    else:
        for i in range(2, num+1):
            result[i] = result[i-1] + result[i-2]

        return result

print(f"fib number for 10: {fibNum(10)}")
