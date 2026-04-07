from SoftwareDev002.mindYourOwnMaze.titleScreen import titleScreen
from SoftwareDev002.mindYourOwnMaze.gridSize import createGrid, printGrid, selectGridSize
from SoftwareDev002.mindYourOwnMaze.maze import makeMaze
from SoftwareDev002.mindYourOwnMaze.game import gameLoop

def main():
    titleScreen()
    rows, cols = selectGridSize()
    grid = createGrid(rows, cols)
    maze = makeMaze(grid)
    gameLoop(maze)

if __name__ == "__main__":
    main()