import pytest
from mindYourOwnMazeV2.gridSize import createGrid, selectGridSize, printGrid
from mindYourOwnMazeV2.player import Player
from mindYourOwnMazeV2.gameState import GameState

# ---------------------------
# Test for grid creation
# ---------------------------

def test_createGrid_dimensions():
    g = createGrid(5, 8)
    assert len(g) == 5
    assert len(g[0]) == 8

# ---------------------------
# Test for player symbol on grid
# ---------------------------

def test_printGrid_shows_player(capsys):
    grid = createGrid(3, 3)
    p = Player(1, 1)
    gs = GameState(grid, p, (2, 2), [])
    printGrid(gs)
    out = capsys.readouterr().out
    assert "P" in out

# ---------------------------
# Test for item symbol on grid when reveal is True
# ---------------------------

def test_printGrid_reveals_item_when_reveal_true(capsys):
    grid = createGrid(3, 3)
    p = Player(0, 0)
    gs = GameState(grid, p, (1, 1), [])
    gs.reveal = True
    printGrid(gs)
    out = capsys.readouterr().out
    assert "T" in out