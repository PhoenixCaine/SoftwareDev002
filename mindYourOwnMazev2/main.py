from titleScreen import titleScreen
from gridSize import createGrid, selectGridSize
from maze import makeMaze
from hiddenItems import placeItem, placeTraps
from game import gameLoop
from player import Player
from screenClear import clearScreen


def main():
    titleScreen()
    while True:
        rows, cols = selectGridSize()
        grid = createGrid(rows, cols)
        makeMaze(grid)

        tempPlayer = Player()

        item = placeItem(grid, tempPlayer)
        traps = placeTraps(grid, tempPlayer, item)

        gameLoop(grid, item, traps)

# Restart game option after game ends for win or lose

        choice = input("\nWould you like to play again? (y/n): ").lower()

        if choice == "y":
            clearScreen()
            continue  # restart the game

        print("Thanks for playing!")
        break  # exit the loop and end the program



if __name__ == "__main__":
    main()