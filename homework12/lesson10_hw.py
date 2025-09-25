# Telemarketer or not?

# input
phone = (input("enter the last four digits of the phone number： "))

# processing
# if phone[0] == 8 or phone[0] == 9: 
    # if have a string, list, or tuple; we can access the collection's individual item
    # at a certain location by doing indexing with [ ], always starts from 0
if phone[0] in {'8','9'}:
    if phone[-1] in {'8', '9'}: # last value of string can use negative 1 as index
        if phone[1] == phone[2]:
            print(f"the phone number ending with {phone} is a telemarketer")
        else:
            print(f"the phone number ending with {phone} is not a telemarketer")

    else:
        print(f"the phone number ending with {phone} is not a telemarketer")
else:
    print(f"the phone number ending with {phone} is not a telemarketer")
        
