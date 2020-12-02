#!/usr/bin/env python3

filename="input/day1"

with open(filename,'r') as i:
    expenses = i.read().split('\n')
    expenses.pop() #Remove the last value, which is blank
    expenses = [int(x) for x in expenses] #Convert to ints

#Part 1: 2 numbers that sum to 2020
print([(x, y, x*y) for i,x in enumerate(expenses) for j,y in enumerate(expenses) if j > i and x+y == 2020][0])

#Part 2: 3 numbers that sum to 2020
print([(x, y, z, x*y*z) for i,x in enumerate(expenses) for j,y in enumerate(expenses) for k,z in enumerate(expenses) if j > i and k > j and x+y+z == 2020][0])
