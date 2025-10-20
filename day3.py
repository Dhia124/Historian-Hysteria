# Advent of Code 2024 - Day 3  (Parts 1 & 2)

import re  # import the regular-expression module for pattern matching

def load(path="input3.txt"):  # define a helper to read the puzzle input file
    with open(path, "r", encoding="utf-8") as f:  # open the file in text mode with UTF-8 encoding
        return f.read()  # read the entire contents and return as one string

def part1(s: str) -> int:  # solve part 1: sum every valid mul(X,Y) instruction
    # valid mul(X,Y) where X,Y are 1-3 digits
    return sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", s))  # find all mul(X,Y) patterns, convert digits to ints, multiply, and sum

def part2(s: str) -> int:  # solve part 2: obey do()/don't() enable/disable flags
    total = 0  # running total of enabled multiplications
    enabled = True  # start with mul instructions enabled
    # scan in order: mul(...), do(), don't()
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")  # regex that matches either a mul instruction or a do()/don't() directive
    for m in pattern.finditer(s):  # iterate over every match in the order they appear
        if m.group(0) == "do()":  # if the match is exactly "do()", enable future mul instructions
            enabled = True
        elif m.group(0) == "don't()":  # if the match is exactly "don't()", disable future mul instructions
            enabled = False
        else:  # otherwise it's a mul(X,Y) instruction
            if enabled:  # only process the multiplication if currently enabled
                a, b = int(m.group(1)), int(m.group(2))  # extract the two 1-3 digit numbers
                total += a * b  # multiply them and add to running total
    return total  # return the final sum after processing the entire string

if __name__ == "__main__":  # run only when this script is executed directly
    s = load("input3.txt")  # load the puzzle input into string s
    print("Part 1:", part1(s))  # compute and print part 1 result
    print("Part 2:", part2(s))  # compute and print part 2 result
