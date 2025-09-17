# Donuts 9/16

donuts_available = int(input("how many donuts do we have at the beginning? "))
events = int(input("enter the number of events: "))

#w we stop when no donut or no event
current_event = 1
while current_event <= events and donut_count >= 0:
    event_type = input("+ or -?: ")
    donut_amount = int(input("enter donut count: "))
    if event_type == "+":
        donuts_available = donuts_available + donuts_amount
        # OR donuts_available += donuts_amount
    elif event_type == "-":
        donuts_available = donuts_available - donuts_amount
        if donuts_available <= 0:
            print("sorry, not enough donuts for you...")
    else: 
        print("sorry, invalid input")
        print("enter again: ")
        event_type = int(input())

# end of while loop
print(f"At the end of our events, we have {donuts_available} donuts. ")
        
        
