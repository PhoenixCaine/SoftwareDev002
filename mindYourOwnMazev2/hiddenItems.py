import random

def random_empty_cell(rows, cols, forbidden):
    """Return a random (r, c) not in forbidden."""
    while True:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if (r, c) not in forbidden:
            return (r, c)

def placeItem(grid, player):
    rows, cols = len(grid), len(grid[0])
    forbidden = {(player.row, player.col)}

    while True:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if (r, c) not in forbidden:
            return (r, c)

def placeTraps(grid, player, item_pos, n=3):
    rows, cols = len(grid), len(grid[0])
    forbidden = {(player.row, player.col), item_pos}
    traps = set()

    while len(traps) < n:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if (r, c) not in forbidden and (r, c) not in traps:
            traps.add((r, c))

    return list(traps)


