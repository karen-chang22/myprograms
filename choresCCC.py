# CCC '13 J4 - Time on task

# time = total number of minutes
# chores = total number of chores 
# required_time = number of minutes required to do each chore
# output = max number of chores that can be completed in the given Time

time = int(input())
chores = int(input())
time_list = []
for i in range(chores):
    time_chore = int(input())
    time_list.append(time_chore)

def sort(time_list):
    counter = 0
    sum = 0
    for n in time_list:
        smallest = min(time_list) # min is linear
        if sum + smallest < time:
            result.append(smallest)
            counter += 1
        else:
            break
    return counter


# Setup
time_list = int(input())
chores = int(input())
time_chore = []
for i range(chores):
    time_chore.append(int(input()))

# Maximizing Chores
time_chore.sort() #.sort is based on merge sort
# or bubble/insertion/selection --> quadratic
counter = 0
i = 0
while time > 0 and i < len(time_chore):
    if time_chore[i] <= time:
        time -= time_chore[0]
        counter += 1
        # time_chore.pop(0) #why not .remove? Because .remove VALUE while .pop removes by INDEX
        i += 1
    else:
        break



