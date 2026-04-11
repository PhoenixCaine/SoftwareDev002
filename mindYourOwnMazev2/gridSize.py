def createGrid(rows, cols):
    return [["." for _ in range(cols)] for _ in range(rows)]


def cell_symbol(r, c, player, reveal, traps, item_pos):
    if r == player.row and c == player.col:
        return "P"
    if reveal and (r, c) == item_pos:
        return "T"
    if reveal and (r, c) in traps:
        return "X"
    return "."


def printGrid(game_state):
    rows, cols = game_state.rows, game_state.cols
    player = game_state.player
    reveal = game_state.reveal
    traps = game_state.traps
    item_pos = game_state.item_pos

    print("┌" + "─" * (cols * 2 + 1) + "┐")

    for r in range(rows):
        row_display = [
            cell_symbol(r, c, player, reveal, traps, item_pos)
            for c in range(cols)
        ]
        print("│ " + " ".join(row_display) + " │")

    print("└" + "─" * (cols * 2 + 1) + "┘")


def selectGridSize():
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