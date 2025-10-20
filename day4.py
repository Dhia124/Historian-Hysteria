# Advent of Code 2024 - Day 4: Ceres Search (Parts 1 & 2)

def part1(grid):
    """Count all occurrences of 'XMAS' in 8 directions."""
    # Determine the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    # The word we are searching for
    word = "XMAS"
    # Define the 8 possible directions: down, up, right, left, down-right, up-left, down-left, up-right
    dirs = [
        (1, 0), (-1, 0),   # vertical
        (0, 1), (0, -1),   # horizontal
        (1, 1), (-1, -1),  # diagonal ↘ ↖
        (1, -1), (-1, 1)   # diagonal ↙ ↗
    ]
    # Initialize the counter for valid occurrences
    count = 0

    # Iterate over every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Try each direction from the current cell
            for dr, dc in dirs:
                # Check if the word can be formed starting at (r, c) in direction (dr, dc)
                if all(
                    0 <= r + i * dr < rows and  # Ensure row index stays within bounds
                    0 <= c + i * dc < cols and  # Ensure column index stays within bounds
                    grid[r + i * dr][c + i * dc] == word[i]  # Check character match
                    for i in range(len(word))  # Loop over each character in 'XMAS'
                ):
                    count += 1  # If all characters match, increment the count
    return count


def part2(grid):
    """Count all 'X-MAS' patterns: two MAS (or SAM) diagonals crossing on 'A'."""
    # Store number of rows and columns in shorter variables
    R, C = len(grid), len(grid[0])

    # Helper function to check if two characters are 'M' and 'S' in any order
    def ms_pair(a, b):
        return (a == 'M' and b == 'S') or (a == 'S' and b == 'M')

    # Initialize counter for valid X-MAS patterns
    total = 0
    # Iterate over inner cells (excluding borders since we need neighbors)
    for r in range(1, R - 1):
        for c in range(1, C - 1):
            # The center of the X must be 'A'
            if grid[r][c] != 'A':
                continue
            # Extract the two diagonal pairs
            d1 = (grid[r - 1][c - 1], grid[r + 1][c + 1])  # Top-left to bottom-right diagonal
            d2 = (grid[r - 1][c + 1], grid[r + 1][c - 1])  # Top-right to bottom-left diagonal
            # Check if both diagonals form M-S or S-M pairs
            if ms_pair(*d1) and ms_pair(*d2):
                total += 1  # Valid X-MAS pattern found
    return total


# --- main ---
if __name__ == "__main__":
    # Open and read the input file, stripping whitespace and ignoring empty lines
    with open("input4.txt") as f:
        grid = [line.strip() for line in f if line.strip()]

    # Run and print results for both parts
    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))
