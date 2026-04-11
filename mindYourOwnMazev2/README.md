# Magic Maze – *Mind Your Own Maze!*

## Requirements

To run the game, you need:

- **Python 3.10+**
- The following Python packages:
  - `pyfiglet`
  - `pytest` (for testing only)

Install dependencies using:

```bash
pip install pyfiglet pytest pytest-rich pytest-cov
```

## Example test Commands

```bash
pytest -v --rich
pytest --cov-report=term-missing
```

## How to run the game

- Open a terminal in the project root directory (the folder containing main.py).
- Run the game with:

```python
python main.py
```

- Follow the on‑screen instructions:

1. Choose a grid size
2. Move using W/A/S/D
3. Press H for a BFS hint
4. Avoid traps and find the treasure

## Report

## Introduction

This report will document the design, development, testing and evaluation of a Python maze navigation game. The assessment learning outcomes were focussed on developing a structured solution to a simple problem ensuring good code readability and maintainability with appropriate testing of the code to ensure robustness and future upgradeability.
The assessment brief required the designing and development of a python single-player maze game. The game uses a two-dimensional grid in which the player navigates around the grid to find hidden treasure while avoiding traps that reduce health. We also had to include a search algorithm to help with finding the best path of the hidden treasure I chose to use breadth first search.

## Program Design and Implementation

To enhance player engagement and offer some customisation, the game allows the player to select the size of grid before gameplay starts. Each grid is represented a list of lists which allows efficient indexing and manipulation of cell states required to display accurate item and player placement.
Initially the movement, health, and win-lose conditions were all bundled up in the player.py and gridSize.py files. As I iterated during development I decided on a modular approach to coding as this ensures maintainability and future upgradeability. I had a strong focus on flattening the code, so it did not use as many indentations. This greatly improved the readability of my code.
In early development health was hard coded inside the player.py file as a default value//magic number (health=3) and was reduced directly in the trap handling function. This caused a problem when changing grid size as it also required manually updating health in multiple places which was cumbersome. To improve this for version two the player.py file no longer stores health as it is calculated in GameState only. Magic numbers were removed and replaced with clear rules where a five-by-five grid would have three health and an eight-by-eight grid would have five health. There is also a formula for possible future sizes s as an upgrade path. These changes centralised the game rules, greatly improved code maintainability and removed unnecessary duplication.

## Search Algorithm (BFS or DFS)

Breadth first search (BFS) is used for the search algorithm this was chosen as it always finds the shortest path in an unweighted grid. This ensures that the player receives hints with the shortest distance within the maze. BFS does this by exploring the grid in a predictable layer by layer method this means that it finds the shortest route possible on the first time finding the treasure. This algorithm works perfectly with a 2D grid represented as a list of lists as each cell is a node and each movement is an edge. BFS is also much easier to debug as it has fewer moving parts. This aligned with the main focus on code readability maintainability and structured problem solving.

## Testing

To ensure the readability maintainability and correctness of the maze navigation a comprehensive testing strategy was used. The assessment heavily focussed on structured problem solving so testing was integrated throughout development rather than as a final step. This ensured that correctness and reliability were maintained through each iteration. Both unit tests and manual play testing were used to validate functionality identify errors and confirm the game behaved as expected across the different grid sizes.
Automated testing was done using the Pytest framework due to its readability and simplicity. It is most suitable for modular Python applications such as this. Each module was tested independently to ensure that the individual components worked before integrating it into the full game.
Some of the key areas tested were grid generation to verify that the different grid sizes were created correctly and ensured the traps and treasures were placed within the bounds of the map. These tests also ensured that the player and items did not overlap unless intended. The use of mock data was used to account for user inputs such as clearing the screen. This allowed the focus to remain on function behaviour rather than terminal interactions. Lastly, manual play testing was conducted to evaluate the overall user experience for the player with a focus on improving pacing, responsiveness of movement, usefulness of the BFS hints and clarity of game instructions.  

## Challenges and Improvements

This assessment I encountered technical and structural challenges that required iterative refinement and problem solving. As the version one movement logic and health management were spread across multiple files this made it difficult to maintain the code and led to confusing interactions between modules. Refactoring the project into a modular structure required planning and attention to detail to maintain functionality. There were also issues when running the version two files as I still had version one within the project file structure. VS Code would systematically run the version one files before the version two files which meant my pathing had to be refactored.

## Future Improvements

- Add more trap types
- Add multiple treasure items
- Add colour‑coded terminal output
- Add a menu system and difficulty mode