try:
    from .gridSize import printGrid
    from .player import Player
    from .gameState import GameState
    from .hiddenItems import placeItem, placeTraps
    from .screenClear import clearScreen
    from .bfs import bfs
except ImportError:
    from gridSize import printGrid
    from player import Player
    from gameState import GameState
    from hiddenItems import placeItem, placeTraps
    from screenClear import clearScreen
    from bfs import bfs

# Handle trap and item interactions

def handleTrap(game):
    game.player.loseHealth()

    game.revealedTraps.add((game.player.row, game.player.col))

    if game.player.isDead():
        print("You hit a trap. You lose a life!")
        print("You died! Game over.")
        input("Press Enter to reveal map...")
        game.reveal = True
        game.running = False
    else:
        print("You hit a trap. You lose a life!")
        print("You have {} health left.".format(game.player.health))
        input("Press Enter to continue...")

def handleItem(game):
    print("You found the treasure. You win!")
    input("Press Enter to reveal map...")
    game.reveal = True
    game.running = False

# Process player movement and check for traps/items

def processMovement(direction, game):
    p = game.player
    p.move(direction, game.rows, game.cols)

    if game.player_on_trap():
        handleTrap(game)
        return

    if game.player_on_item():
        handleItem(game)

# BFS hint system 
def giveHint(game):
    start = (game.player.row, game.player.col)
    goal = game.item_pos
    grid = game.grid

    path = bfs(start, goal, grid)

    if not path or len(path) < 2:
        print("No path found!")
        input("Press Enter to continue...")
        return

    next_step = path[1]  # path[0] is current position

    pr, pc = game.player.row, game.player.col
    nr, nc = next_step

    if nr < pr:
        direction = "w"   # move up
    elif nr > pr:
        direction = "s"   # move down
    elif nc < pc:
        direction = "a"   # move left
    elif nc > pc:
        direction = "d"   # move right

    print(f"Hint: move '{direction}' toward {next_step}")
    input("Press Enter to continue...")

# Main game loop

def gameLoop(grid, item, traps):
    player = Player()
    game = GameState(grid, player, item, traps)

    while game.running:
        clearScreen()
        print(f"Health: {game.player.health}")
        printGrid(game)

        direction = input("Move (w/a/s/d) or h for hint: ").lower()

        if direction in ("w", "a", "s", "d"):
            processMovement(direction, game)
            continue

        if direction == "h":
            giveHint(game)
            continue

        print("Invalid input.")
    
    # After the loop ends, reveal everything
    clearScreen()
    game.reveal = True
    printGrid(game)
    print("Game over.")

