# CCC '00 S4 - Golf
import math

# Dynamic Programming
def golf(clubs, target):
    distances = [0] + [math.inf] * target
    for current in range(len(distances)):
        for c in clubs:
            new_loc = current + c
            if new_loc <= target:
                distances[new_loc] = min(distances[current]+1, distances[new_loc])
    return distances[target]


