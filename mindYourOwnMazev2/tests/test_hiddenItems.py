import pytest
from unittest.mock import patch
from hiddenItems import placeItem, placeTraps
from gridSize import createGrid
from player import Player

# ---------------------------
# Test for placeItem function
# ---------------------------

@patch("random.randint", side_effect=[0,0,1,1,2,2])
def test_placeItem_not_on_player(mock_rand):
    grid = createGrid(3, 3)
    p = Player(0, 0)
    item = placeItem(grid, p)
    assert item != (0, 0)

# ---------------------------
# Test for placeTraps function
# ---------------------------

@patch("random.randint", side_effect=[0,1,2,0,1,2,2,1,0])
def test_placeTraps_no_overlap(mock_rand):
    grid = createGrid(3, 3)
    p = Player(0, 0)
    item = (1, 1)
    traps = placeTraps(grid, p, item, n=3)
    assert item not in traps
    assert (0, 0) not in traps
    assert len(traps) == 3
    assert len(set(traps)) == 3