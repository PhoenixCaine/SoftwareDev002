import random

def makeMaze(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Fill the grid with empty spaces
    for r in range(rows):
        for c in range(cols):
            grid[r][c] = "."

#   # Set start and end points
#   grid[0][0] = "S"
#   grid[rows - 1][cols - 1] = "E"

    return grid

