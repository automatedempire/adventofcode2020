#!/usr/bin/env python3

puzzle_input = 'input/day10'

with open(puzzle_input, 'r') as puzz_in:
    adapters = puzz_in.read().strip().split('\n')

#Add the outlet voltage to the list
adapters.append(0)
#Convert everything to int and order the list
adapters = sorted([int(x) for x in adapters])
#Add the laptop voltage to the list
adapters.append(adapters[-1]+3)

chain = { 1: [], 2: [], 3: [] }
current = 0 #Outlet starts at 0
pos = 1
while pos < len(adapters):
    chain[adapters[pos]-current].append(adapters[pos])
    current = adapters[pos]
    pos += 1

one_jolt = len(chain[1])
three_jolt = len(chain[3])
product = one_jolt * three_jolt
print(f'1 jolt ({one_jolt}) * 3 jolt ({three_jolt}): {product}')

#Part 2: Find all paths
#Create an adjacency list
adjacent = {}
for i, adapter in enumerate(adapters):
    adjacent[adapter] = []
    for j in range(1,4):
        if i + j < len(adapters) and adapters[i+j] <= adapters[i] + 3:
            adjacent[adapter].append(adapters[i+j])
        else:
            break
    if len(adjacent[adapter]) == 0:
        adjacent.pop(adapter)

#This will act as a memory of counts we've already computed
paths_from = {}
#Depth first search
def count_paths(node, goal):
    global paths_from

    #Shortcut cache. We've already calculated this, so we know the value.
    if node in paths_from:
        return paths_from[node]

    if node == goal:
        return 1
    else:
        paths = 0
        for next_hop in sorted(adjacent[node]):
            #Allows for subpaths to be calculated
            if next_hop > goal:
                break
            paths += count_paths(next_hop, goal)
            #Store the count of the paths from this node
            paths_from[node] = paths
    return paths

paths = count_paths(adapters[0], adapters[-1])
print(f'Total paths: {paths}')
print(paths_from)

