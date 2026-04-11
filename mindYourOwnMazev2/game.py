from gridSize import printGrid
from player import placePlayer, playerMovement, getPlayerInput
from screenClear import clearScreen
from health import loseLife, checkGameOver, resetLives, showLives

def gameLoop(grid):
    player_pos = placePlayer(grid)

    while True:
        clearScreen()          # ← clears screen before drawing
        printGrid(grid)

        direction = getPlayerInput()
        if direction:
            playerMovement(grid, player_pos, direction)

            # Example: health check (optional)
            if checkGameOver():
                break
            else:
                showLives() 

