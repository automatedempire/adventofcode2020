#!/usr/bin/env python3
import re

filename='input/day02'

with open(filename,'r') as i:
    passwords = i.read().strip().split('\n')

first_valid = 0
second_valid = 0
for entry in passwords:
    bounds, letter, pword = entry.split(' ')
    low, high = (int(x) for x in bounds.split('-'))
    letter = letter[0] #drop the semicolon

    #Part 1
    #Total instances of letter must be between the bounds, inclusive
    matches = len(re.findall(letter, pword))
    if low <= matches <= high:
        first_valid += 1

    #Part 2
    #One or the other must contain the letter, but not both: XOR operation.
    #Offset character place by 1 for not using a 0 index.
    if (pword[low-1] == letter) ^ (pword[high-1] == letter):
        second_valid += 1

print(f'Total first valid: {first_valid}')
print(f'Total second valid: {second_valid}')
