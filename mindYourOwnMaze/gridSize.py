def createGrid(rows, cols):
    return [["." for _ in range(cols)] for _ in range(rows)]


def printGrid(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Top border
    print("┌" + "─" * (cols * 2 + 1) + "┐")

    # Middle rows
    for row in grid:
        print("│ " + ' '.join(str(cell) for cell in row) + " │")

    # Bottom border
    print("└" + "─" * (cols * 2 + 1) + "┘")


def selectGridSize():
    while True:
        try:
            size = int(input("Press 1 for a 5x5 grid, 2 for an 8x8 grid: "))
            if size == 1:
                return 5, 5
            elif size == 2:
                return 8, 8
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")