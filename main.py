import sys
import math

# game loop
while True:
    mountain_h = []
    for i in range(8):
        mountain_h.append(int(input()))  # represents the height of one mountain.
    print(mountain_h.index(max(mountain_h)))
