#!/usr/bin/env python3

filename = 'input/day05'

seat_ids = []
seats = {}
with open(filename, 'r') as scanned_passes:
    for bpass in scanned_passes:
        bpass = bpass.strip()
        row = bpass[:7] #First 7 characters are row ID
        col = bpass[-3:] #Last 3 characters are column

        #Convert row and col info to binary
        row = row.replace('F','0').replace('B','1')
        col = col.replace('L','0').replace('R','1')

        #Late realization: the whole string acts as one binary number.
        main_id = row + col

        #convert the binary numbers to int
        col = int(col, 2)
        row = int(row, 2)
        main_id = int(main_id, 2)

        seats[main_id] = (row,col)

        #Create a list of seat IDs
        seat_id = row * 8 + col #Protip: This math works out to be main_id.
        seat_ids.append(seat_id)

#Part 1: Max seat id
seat_ids = sorted(seat_ids)
print(f'Max seat id: {seat_ids[-1]}')

#Part 2: What's my seat?
#All seats are full so mine will be the only one missing from the list.
#In a sorted list, this means the ID of the next seat will be 2 higher than the current.
#My seat, then, will be one higher than the current.
for i, main_id in enumerate(seat_ids[:-1]):
    if seat_ids[i+1] == seat_ids[i] + 2:
        my_seat = seat_ids[i] + 1
        print(f'My seat id is {my_seat}, which means I sit at row {int(my_seat/8)} column {my_seat % 8}')
        print(seats[seat_ids[i]])
        print(seats[seat_ids[i+1]])
        break
