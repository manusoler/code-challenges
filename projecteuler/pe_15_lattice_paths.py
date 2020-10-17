import os
from utils.decorators import timer
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def num_diff_paths(height, width):
    # Build the matrix (right and bottom vortex has 1 because they only have 1 path to reach the end)
    grid = [[0 if x != width and y != height else 1 for x in range(width+1)] for y in range(height+1)]
    # Starting from the end, we calculate num of diff paths for each cell (sum of his neighbours)
    for i in reversed(range(height)):
        for j in reversed(range(width)):
            # Fill each cell with the sum of his neighbours
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
    # grid 0,0 has num of diff paths 
    return grid[0][0]


@timer
def main():
    print(num_diff_paths(20,20))


if __name__ == "__main__":
    main()