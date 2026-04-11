from titleScreen import titleScreen
from gridSize import createGrid, selectGridSize
from maze import makeMaze
from hiddenItems import placeItem, placeTraps
from game import gameLoop
from player import Player

def main():
    titleScreen()
    rows, cols = selectGridSize()
    grid = createGrid(rows, cols)
    makeMaze(grid)

    tempPlayer = Player()

    item = placeItem(grid, tempPlayer)
    traps = placeTraps(grid, tempPlayer, item)

    gameLoop(grid, item, traps)

if __name__ == "__main__":
    main()