# Squares problem from CCC 2004

# input
tiles = int(input())

# import statement
from math import sqrt, floor

# processing
# ans = tiles ** 0.5
ans = floor(sqrt(tiles))
# ans = floor(ans)

# output
print(f"the largest square had side length {ans}")
