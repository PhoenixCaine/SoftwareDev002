from gridSize import printGrid
from player import Player
from gameState import GameState
from hiddenItems import placeItem, placeTraps
from screenClear import clearScreen

# Handle trap and item interactions

def handleTrap(game):
    game.player.loseHealth()

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
            print("Hint coming soon…")
            continue

        print("Invalid input.")
    
    # After the loop ends, reveal everything
    clearScreen()
    game.reveal = True
    printGrid(game)
    print("Game over.")

