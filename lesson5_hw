# Selling cookies
# normal cookies cost $1.25; big cookies cost $2.00
# to bake normal cookie it costs $0.50; big one costs $0.75
# Output: 
        #1) total cookies sold
        #2) profit
        #3) total amount of money after (since we started with some money)

# input
startMoney = float(input())
cookiesSold = input()

# processing
bigCookies = 0 #variable intialization
cookies = 0

for currentCookies in cookiesSold: # looking at individual item in currentCookies
    if currentCookies == "c":
        cookies += 1
    elif currentCookies == "b":
        bigCookies += 1
    else:
        print(f"{currentCookies} is not a valid sale item.")
# end of for

# alternative way: using COUNT method
# cookies = cookiesSold.count('c')
# bigCookies = cookiesSold.count('b')

cookiesSold = cookies + bigCookies
profit = (1.25-0.5) * cookies + (2-0.75) * bigCookies
totalMoney = startMoney + profit
print(f"{cookiesSold} cookies were sold.")
print(f"profit made is ${profit}.")
print(f"total money after is ${totalMoney}.")

