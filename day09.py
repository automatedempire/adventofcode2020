#!/usr/bin/env python3

puzzle_input = 'input/day09'

with open(puzzle_input, 'r') as puzz_in:
    XMAS = puzz_in.read().strip().split('\n')

XMAS = [int(x) for x in XMAS]

def generate_valid_numbers(sublist):
    valid = [x + y for i,x in enumerate(sublist) for j,y in enumerate(sublist) if j > i]
    #Use set for faster inclusion testing
    return set(valid)

#Part 1
def find_invalid(data_stream):
    preamble_len = 25
    for pos in range(preamble_len, len(data_stream)):
        start = pos - preamble_len
        valid_cypher = generate_valid_numbers(data_stream[start:pos])
        if data_stream[pos] not in valid_cypher:
            print(f'Found invalid number {data_stream[pos]} at position {pos}')
            return data_stream[pos]

invalid_key = find_invalid(XMAS)

#Part 2
def find_weakness(data_stream, invalid):
    for i in range(len(data_stream) - 1):
        for j in range(1, len(data_stream) - i):
            if invalid == sum(data_stream[i:i+j]):
                print(f'Found the range: {i} : {i+j}')
                smallest = min(data_stream[i:i+j])
                largest = max(data_stream[i:i+j])
                return smallest + largest

weakness = find_weakness(XMAS, invalid_key)
print(f'Encryption weakness: {weakness}')

