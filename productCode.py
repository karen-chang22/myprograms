# CCC practice question - Product Codes

def cleaner(text):
    # text kinda looks like cG23mH-9s
    # we want GH14
    upper_case = ""
    positives = ""
    negatives = ""
    total_sum = 0
    for item in text:
        if item.isalpha() and item.isupper():
            upper_case += item
            if len(positives) > 0: # to see if 'positives' is empty
                total_sum += int(positives)
                positives = "" # empty it so we can track future postives
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = ""
            # pretty much just to check how many digts are together (keeping it as 12 rather than 1 and 2)
        elif item == "-":
            if len(negatives) > 0:
                total_sum += int(negatives)
                negatives = "-" # making sure that every digit after the '-' is negative
            else: 
                negatives = "-"
        elif item.isdigit():
            if len(negatives) > 0:
                negatives += item
            else:
                positives += item
    # end of for
    # if text ended with digits
    if len(positives) > 0:
        total_sum += int(positives)

    if len(negatives) > 0:
        total_sum += int(negatives)

    productCode = upper_case + str(total_sum)
    return productCode

# end of function

code = input()
print(cleaner(code))


 # MY CODE

# original = input(f"enter the product code: ")
# new = ""
# digitSum = 0
# finalCode = ""
# for c in original:
#     if c.isalpha() and c.isupper():
#         new += c
#     elif c.isdigit():
#         digitSum += int(c)

# finalCode = new + str(digitSum)
# print(finalCode)


