# Advent of Code 2024 - Day 1: Historian Hysteria (Part 1)
with open("input.txt") as f:              # Open the input file for reading
    left, right = [], []                  # Initialize empty lists for left and right columns
    for line in f:                        # Iterate over each line in the file
        a, b = map(int, line.split())     # Split the line into two integers
        left.append(a)                      # Append the first integer to the left list
        right.append(b)                     # Append the second integer to the right list

# Sort lists
left.sort()                               # Sort the left list in ascending order
right.sort()                              # Sort the right list in ascending order

total_distance = sum(abs(a - b) for a, b in zip(left, right))  # Calculate the sum of absolute differences between paired elements
print(total_distance)                     # Print the total distance
