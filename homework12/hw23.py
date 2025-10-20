# Average Calculator

loop = True
totalSum = 0
markCount = 0
while loop:
    user_input = (input("enter the mark ('exit' to stop inputting): "))

    if user_input.lower() == 'exit':
        loop = False
        break # exit the loop
    elif user_input.isdigit():
        mark = int(user_input)
        if 0 <= mark <= 100:
            totalSum += mark
            markCount += 1
        else:
            print("invalid input")
    else:
        print("invalid input")
# end of while

average = totalSum / markCount
print(f"Your calculated average for {markCount} marks is {average}")

