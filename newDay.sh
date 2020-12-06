#!/bin/bash

day=$1
day_format=$(printf "%02d" $day)
fname=day${day_format}
puzzle_input="input/$fname"
py_file=${fname}.py

wget --load-cookies cookies.txt https://adventofcode.com/2020/day/$day/input -O ${puzzle_input}

echo -e "#!/usr/bin/env python3\n\npuzzle_input = '${puzzle_input}'\n\nwith open(puzzle_input, 'r') as puzz_in:\n" > ${py_file}
chmod 755 ${py_file}
