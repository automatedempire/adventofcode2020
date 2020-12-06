#!/usr/bin/env python3

puzzle_input = 'input/day06'

with open(puzzle_input, 'r') as puzz_in:
    answers = puzz_in.read().split('\n')

total_answers = 0
total_all_yes_answers = 0

current_group = ""
current_group_len = 0
for answer in answers:
    if answer:
        current_group += answer
        current_group_len += 1
    else: #Blank line, process current group
        sorted_answers = sorted(current_group)

        #Part 1: Find total answers
        unique_answers = set(sorted_answers)
        total_answers += len(unique_answers)

        #Part 2: Find answers that are yes for the whole group
        answer_dict = dict.fromkeys(unique_answers, 0)
        for letter in sorted_answers:
            answer_dict[letter] += 1

        for k in unique_answers:
            if answer_dict[k] == current_group_len:
                total_all_yes_answers += 1

        current_group = ""
        current_group_len = 0

print(f"Total unique answers: {total_answers}")
print(f"Total all yes answers: {total_all_yes_answers}")
