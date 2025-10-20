# Advent of Code 2024 - Day 2 (Parts 1 & 2)

def is_safe(levels):
    # Build a list of differences between every pair of adjacent levels
    d = [b - a for a, b in zip(levels, levels[1:])]
    # Check if all differences are between 1 and 3 (strictly increasing)
    inc = all(1 <= x <= 3 for x in d)
    # Check if all differences are between -3 and -1 (strictly decreasing)
    dec = all(-3 <= x <= -1 for x in d)
    # Report is safe if it is either purely increasing or purely decreasing
    return inc or dec

def is_safe_with_dampener(levels):
    # First see if the report is already safe without any removals
    if is_safe(levels):
        return True
    # If not, try removing each single level one at a time
    for i in range(len(levels)):
        # Create a new list without the level at index i
        cand = levels[:i] + levels[i+1:]
        # Only check safety if at least two levels remain
        if len(cand) >= 2 and is_safe(cand):
            return True
    # No single removal made the report safe
    return False

def parse(path="input2.txt"):
    # Open the input file and read all non-empty lines
    with open(path) as f:
        # Convert each line into a list of integers
        return [list(map(int, line.split())) for line in f if line.strip()]

def solve(path="input2.txt"):
    # Read and parse all reports from the file
    reports = parse(path)
    # Count how many reports are safe without dampener (Part 1)
    part1 = sum(is_safe(r) for r in reports)
    # Count how many reports are safe with dampener (Part 2)
    part2 = sum(is_safe_with_dampener(r) for r in reports)
    # Display the results
    print("Part 1:", part1)
    print("Part 2:", part2)

if __name__ == "__main__":
    # Run the solver using the default input file when script is executed directly
    solve("input2.txt")
