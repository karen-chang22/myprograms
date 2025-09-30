# Special Day
# Feb 18th is a special day for CCC

#input
month = int(input())
day = int(input())

# processing & output
if (month, day) == (2, 18):
    print("Special.")
elif (month, day) < (2, 18):
    print("Before.")
else:
    print("After.")

# if month == 2 and day == 18:
#     print("Special.")
# else:
#     if month < 2:
#         print("Before.")
#     elif month > 2:
#         print("After.")
#     else: # in the month of Feb
#         if day < 18:
#             print("Before.")
#         else:
#             print("After.") 

# note: faster to just use else than if

