#!/usr/bin/env python3
from copy import deepcopy

puzzle_input = 'input/day08'

with open(puzzle_input, 'r') as puzz_in:
    instructions_raw = puzz_in.read().strip().split('\n')

main_instructions = []
for ins in instructions_raw:
    op, val = ins.split(' ')
    val = int(val)
    main_instructions.append([op, val])

def nop(accumulator, curr_pos, val):
    return accumulator, curr_pos + 1

def acc(accumulator, curr_pos, val):
    accumulator += val
    return accumulator, curr_pos + 1

def jmp(accumulator, curr_pos, val):
    return accumulator, curr_pos + val

ops = {
    "nop": nop,
    "acc": acc,
    "jmp": jmp,
}

def execute(instructions):
    accumulator = 0
    curr_pos = 0
    executed_lines = []

    while True:
        #Part 1: prevent infinite loop
        if curr_pos in executed_lines:
            return accumulator, False
        executed_lines.append(curr_pos)

        op, val = instructions[curr_pos]
        accumulator, curr_pos = ops[op](accumulator, curr_pos, val)
        #Part 2: Program terminates when it would execute an instruction out of range
        if curr_pos >= len(instructions):
            return accumulator, True

#Part 1: Find the value before the infinite loop
final_val_infinity, finished = execute(main_instructions)
print(f"Final val before infinite loop: {final_val_infinity}")

#Part 2: Solve the Halting problem.
for i in range(len(main_instructions)):
    #List of lists requires deep copy to maintain integrity
    new_instructions = deepcopy(main_instructions)

    #Accumulator is correct. No change, so don't run
    if new_instructions[i][0] == 'acc':
        continue

    if new_instructions[i][0] == 'nop':
        new_instructions[i][0] = 'jmp'
    else: #turn jmp to nop
        new_instructions[i][0] = 'nop'

    final_val, finished = execute(new_instructions)
    if finished:
        print(f"Line {i} was broken. Final accumulator value: {final_val}")
        break

