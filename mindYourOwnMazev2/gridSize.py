import sys

try:
    from . import player
except ImportError:
    import player


def createGrid(rows, cols):
    """Return a rows×cols grid filled with '.' placeholders."""
    return [["." for _ in range(cols)] for _ in range(rows)]


def cell_symbol(r, c, player, reveal, traps, item_pos, revealedTraps):
    """Determine which symbol to display for a given cell."""
    if (r, c) == (player.row, player.col):
        return "P"  # Player position
    elif reveal and (r, c) == item_pos:
        return "T" # Treasure revealed
    elif reveal and (r, c) in traps:
        return "X"  # All traps revealed at end of game
    elif (r, c) in revealedTraps:
        return "X"  # Only traps the player has stepped on
    else:
        return "."  # Default empty/unvisited cell


def printGrid(gameState):
    """Render the game grid with borders and appropriate symbols."""
    rows, cols = gameState.rows, gameState.cols
    player = gameState.player
    reveal = gameState.reveal
    traps = gameState.traps
    item_pos = gameState.item_pos

    encoding = (sys.stdout.encoding or "").lower()
    use_unicode = "utf" in encoding

    top_left, top_right, bottom_left, bottom_right, horizontal, vertical = (
        ("┌", "┐", "└", "┘", "─", "│")
        if use_unicode
        else ("+", "+", "+", "+", "-", "|")
    )

    print(top_left + horizontal * (cols * 2 + 1) + top_right)

    for r in range(rows):
        row_display = [
    cell_symbol(r, c, player, reveal, traps, item_pos, gameState.revealedTraps)
    for c in range(cols)
]
        print(vertical + " " + " ".join(row_display) + " " + vertical)

    print(bottom_left + horizontal * (cols * 2 + 1) + bottom_right)


def selectGridSize():
    """Prompt the user to choose between a 5×5 or 8×8 grid."""
    while True:
        try:
            size = int(input("Press 1 for a 5x5 grid, 2 for an 8x8 grid: "))
            if size == 1:
                return 5, 5
            if size == 2:
                return 8, 8
            print("Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")