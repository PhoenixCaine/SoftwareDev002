from titleScreen import titleScreen
from gridSize import createGrid, printGrid, selectGridSize
from maze import makeMaze
from game import gameLoop

def main():
    titleScreen()
    rows, cols = selectGridSize()
    grid = createGrid(rows, cols)
    makeMaze(grid)
    gameLoop(grid)

if __name__ == "__main__":
    main()