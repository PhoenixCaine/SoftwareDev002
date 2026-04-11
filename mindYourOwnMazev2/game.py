from gridSize import printGrid
from player import Player
from gameState import GameState
from hiddenItems import placeItem, placeTraps
from screenClear import clearScreen

def handleTrap(game):
    game.player.loseLife()
    print("You stepped on a trap!")

    if game.player.isDead():
        print("You died.")
        game.reveal = True
        game.running = False

def handleItem(game):
    print("You found the treasure!")
    game.reveal = True
    game.running = False

def process_movement(direction, game):
    p = game.player
    p.move(direction, game.rows, game.cols)

    if game.player_on_trap():
        handleTrap(game)
        return

    if game.player_on_item():
        handleItem(game)

def gameLoop(grid):
    player = Player()
    item = placeItem(grid, player)
    traps = placeTraps(grid, player, item)
    game = GameState(grid, player, item, traps)

    while game.running:
        clearScreen()
        printGrid(grid, game)

        direction = input("Move (w/a/s/d) or h for hint: ").lower()

        if direction in ("w", "a", "s", "d"):
            process_movement(direction, game)
            continue

        if direction == "h":
            print("Hint coming soon…")
            continue

        print("Invalid input.")
