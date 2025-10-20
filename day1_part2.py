from collections import Counter  # Import Counter to count occurrences in the right list

with open("input.txt") as f:      # Open the input file for reading
    left, right = [], []         # Initialize empty lists for left and right numbers
    for line in f:                # Iterate over each line in the file
        a, b = map(int, line.split())  # Split line into two integers
        left.append(a)            # Append the first number to the left list
        right.append(b)           # Append the second number to the right list

count_right = Counter(right)      # Count how many times each number appears in the right list
similarity = sum(x * count_right[x] for x in left)  # Compute similarity score: sum of left number multiplied by its count in right
print(similarity)                 # Output the final similarity score
