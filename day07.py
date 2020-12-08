#!/usr/bin/env python3
import re

puzzle_input = 'input/day07'

with open(puzzle_input, 'r') as puzz_in:
    rules = puzz_in.read().strip().split('\n')

my_bag = 'shiny gold'

r_bags = re.compile(r' bags?')
r_contain = re.compile(r' contain ')
haversacks = {}

for rule in rules:
    rule = re.sub(r_bags, '', rule) #All "bags" are filler. Ha. Get it?
    rule = rule[:-1] #Strip the last character, a period.
    bag_type, contents = re.split(r_contain, rule)

    #Quick data analysis (1)
    #haversacks[bag_type] = {}
    if 'no other' in rule:
        haversacks[bag_type] = {}
        continue

    bag_can_hold = contents.strip().split(',')
    bag_holds = [bag.strip().split(' ', 1) for bag in bag_can_hold]
    bags_fit = {bag_name: int(qty) for qty, bag_name in bag_holds}

    haversacks[bag_type] = bags_fit

#Quick data analysis (2)
#print(f'Total rules: {len(rules)}') #594
#print(f'Total unique keys: {len(haversacks)}') #594
#Each rule is only on one line, so I can set rather than append.

#Smaller input for debugging
#haversacks = {x: haversacks[x] for x in list(haversacks.keys())[0:200]}

#Part 1: It's just bags all the way down.
paths = []
def bagception(current_bag, current_path = []):
    new_path = current_path
    new_path.append(current_bag) #Always add the current bag to the path
    current_bag_in_others = False
    for bag_type in haversacks: #Loop through the list of all bags
        #Is current_bag able to be held in this bag_type?
        if current_bag in haversacks[bag_type]:
            current_bag_in_others = True
            #print(f'Found {current_bag} in {bag_type}. Path: {new_path}')
            #Check if this bag type can be used in other bags
            bagception(bag_type, new_path)

    if not current_bag_in_others: #Terminal node
        paths.append(new_path)

bagception(my_bag)

print(f"Just curious - total full paths: {len(paths)}")
#Flatten and remove duplicates from the list
any_contain = set([bag for all_bags in paths for bag in all_bags])
if my_bag not in haversacks[my_bag]: #If my bag can't hold the same color...
    any_contain.remove(my_bag) # remove it from the count.
print(f"Total bags that can contain {my_bag}: {len(any_contain)}")


#Part 2: I heard you like bags, so I put bags in your bag.
def stuff_my_bag(current_bag):
    bag_stuffing = 0
    if len(haversacks[current_bag]) == 0:
        return 0

    for bag in haversacks[current_bag]:
        bag_qty = haversacks[current_bag][bag]
        bag_stuffing += bag_qty + bag_qty * stuff_my_bag(bag)

    return bag_stuffing

total_bags = stuff_my_bag(my_bag)
print(f"Total bags I have to put in my {my_bag} bag: {total_bags}")

