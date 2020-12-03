#!/usr/bin/env python3

filename='input/day03'

with open(filename,'r') as in_file:
    map_grid = in_file.read().strip().split('\n')

#Pattern repeats infinitely.
pattern_length = len(map_grid[0]) #31

#Part 1: Starting at 0,0. Slope is right 3, down 1.
first_trees = 0
for i, terrain in enumerate(map_grid[1:]): #Skip line 0. Not checked.
    pos = 3 * (i + 1) % pattern_length
    #print(f'Checking position [{pos}, {i+1}]')
    if '#' == terrain[pos]:
        first_trees += 1

print(f'First slope trees: {first_trees}')

#Part 2: But wait, there are more slopes!
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

arboreal_carnage = []
for slope in slopes:
    right, down = slope
    slope_trees = 0
    for i, terrain in enumerate(map_grid[down::down]): #start on down value line, traverse by down value
        pos = right * (i + 1) % pattern_length
        #print(f'{i} ({pos}, {terrain[pos]}) {terrain}')
        if '#' == terrain[pos]:
            slope_trees += 1
    arboreal_carnage.append(slope_trees)

#print(arboreal_carnage)
import numpy
print(f'Product of all trees: {numpy.prod(arboreal_carnage)}')
