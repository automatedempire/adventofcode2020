#!/usr/bin/env python3
from copy import deepcopy

puzzle_input = 'input/day11'

with open(puzzle_input, 'r') as puzz_in:
    initial_state = puzz_in.read().strip().split('\n')

#This will generate a clean sim state
def create_new_grid():
    new_grid = []
    for line in initial_state:
        new_start = []
        for character in line:
            new_start.append(character)
        new_grid.append(new_start)
    return new_grid

occupied = '#'
empty = 'L'
floor = '.'
x_len = len(initial_state[0])
y_len = len(initial_state)
max_dim = max(x_len, y_len)
print(f'Grid is {x_len} x {y_len}')

#Build the list of directions to explore
north = (0, -1)
northeast = (1, -1)
east = (1, 0)
southeast = (1, 1)
south = (0, 1)
southwest = (-1, 1)
west = (-1, 0)
northwest = (-1, -1)
directions = [north, northeast, east, southeast, south, southwest, west, northwest]

def count_neighbors(x, y, current_state, adjacent_only=True):
    global occupied
    global floor
    global max_dim
    max_search = 2 if adjacent_only else max_dim
    seats = []
    for direction in directions:
        for i in range(1, max_search): #Explore outward along the directions
            #offsets will be multiples of the unit directions
            x_off, y_off = [d * i for d in direction]
            x_pos = x + x_off
            y_pos = y + y_off
            #if either component is out of bounds, stop exploring this direction.
            if not 0 <= x_pos < x_len or not 0 <= y_pos < y_len:
                break

            if current_state[y_pos][x_pos] != floor:
                #Found closest seat in this direction
                seats.append(current_state[y_pos][x_pos])
                break
    return seats.count('#')

def process_round(current_state, max_neighbors, adjacent_only=True):
    global occupied
    global empty
    global floor
    changed = 0
    next_state = deepcopy(current_state)
    for y in range(y_len): #iterate lines
        for x in range(x_len): #iterate positions in a line
            this_pos = current_state[y][x]
            if this_pos != floor: #Floor positions can be ignored.
                neighbors = count_neighbors(x, y, current_state, adjacent_only)
                if this_pos == empty and neighbors == 0:
                    next_state[y][x] = occupied
                    changed += 1
                    continue
                if this_pos == occupied and neighbors >= max_neighbors:
                    next_state[y][x] = empty
                    changed += 1
                    continue

    return changed, next_state

def print_grid(grid):
    for line in grid:
        print(''.join(line))

def run_sim(max_neighbors=4, adjacent_only=True, print_board=False):
    current_state = create_new_grid()
    rounds = 0
    while True:
        rounds += 1
        changed, next_state = process_round(current_state, max_neighbors, adjacent_only)
        if changed != 0:
            current_state = next_state
            if print_board:
                print(f'\nRound {rounds}:')
                print_grid(current_state)
        else:
            total_occupied = sum([x.count('#') for x in current_state])
            print(f'Total occupied: {total_occupied}')
            break

        #if rounds > 10:
        #    break
    return rounds, current_state

#Part 1: I don't want 4 or more adjacent neighbors
part1_rounds, part1_final_state = run_sim(max_neighbors=4, adjacent_only=True)
print(f'Part 1 Total rounds: {part1_rounds}')

#Part 2: I don't want 5 or more neighbors I can see
part2_rounds, part2_final_state = run_sim(max_neighbors=5, adjacent_only=False, print_board=False)
print(f'Part 2 Total rounds: {part2_rounds}')

